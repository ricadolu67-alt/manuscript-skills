"""Check the portable project's structure and integrity without running a model."""

import argparse
import csv
import hashlib
import io
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

SKILLS = ('science-ledger', 'paper-author', 'paper-editor')
IGNORED = {'.git', '__pycache__', '.venv'}
MANIFEST = 'MANIFEST.sha256'


def project_files(root):
    return sorted(
        (p for p in root.rglob('*')
         if p.is_file() and not any(part in IGNORED for part in p.relative_to(root).parts)
         and p.suffix not in {'.pyc', '.pyo'}),
        key=lambda p: p.relative_to(root).as_posix(),
    )


def manifest_text(root):
    return ''.join(
        f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(root).as_posix()}\n'
        for p in project_files(root) if p.name != MANIFEST
    )


def metadata_errors(text, expected_name):
    """Validate the package's deliberately small frontmatter subset."""
    errors = []
    match = re.match(r'\A---\n(.*?)\n---(?:\n|$)', text, re.S)
    if not match:
        return ['missing or malformed frontmatter delimiters']
    header = match.group(1)
    name = re.search(r'^name:\s*([a-z0-9-]+)\s*$', header, re.M)
    if not name or name.group(1) != expected_name:
        errors.append('name does not match the skill directory')
    description = re.search(r'^description:\s*(.*?)(?=\n[^ \t]|\Z)', header, re.S | re.M)
    if not description:
        errors.append('missing description')
    else:
        value = description.group(1).strip()
        if value in {'', '>', '|', '>-', '|-'} or '[TODO:' in value:
            errors.append('empty or unfinished description')
    keys = re.findall(r'^([a-zA-Z][\w-]*):', header, re.M)
    if len(keys) != len(set(keys)):
        errors.append('duplicate frontmatter fields')
    if set(keys) - {'name', 'description', 'metadata', 'license', 'allowed-tools'}:
        errors.append('unsupported frontmatter field in this package')
    return errors


def local_link_error(root, source, target):
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc or target.startswith('#'):
        return None
    raw = unquote(parsed.path)
    if not raw:
        return None
    resolved = (source.parent / raw).resolve()
    try:
        resolved.relative_to(root.resolve())
    except ValueError:
        return f'local link escapes project: {target}'
    if not resolved.exists():
        return f'broken local link: {target}'
    return None


def validate(root, verify_manifest=True):
    root = root.resolve()
    errors = []
    for required in ('README.md', 'LICENSE', 'CONTRIBUTING.md', 'VERSION', 'docs/USAGE.md', '.gitattributes'):
        if not (root / required).is_file():
            errors.append(f'missing required project file: {required}')
    attributes = root / '.gitattributes'
    if attributes.exists() and '* text eol=lf' not in attributes.read_text(encoding='utf-8').splitlines():
        errors.append('missing explicit LF checkout rule')
    entries = list((root / 'skills').iterdir()) if (root / 'skills').is_dir() else []
    if {p.name for p in entries} != set(SKILLS) or any(not p.is_dir() for p in entries):
        errors.append('skills/ must contain exactly the three skill directories')
    for skill in SKILLS:
        license_path = root / 'skills' / skill / 'LICENSE'
        if not license_path.is_file():
            errors.append(f'missing standalone skill license: {skill}')
        elif (root / 'LICENSE').is_file() and license_path.read_bytes() != (root / 'LICENSE').read_bytes():
            errors.append(f'standalone skill license differs: {skill}')
        p = root / 'skills' / skill / 'SKILL.md'
        if not p.is_file():
            errors.append(f'missing skill entrypoint: {skill}')
        else:
            try:
                errors.extend(f'{skill}: {e}' for e in metadata_errors(p.read_text(encoding='utf-8'), skill))
            except UnicodeError:
                errors.append(f'{skill}: entrypoint is not UTF-8')
    for p in project_files(root):
        rel = p.relative_to(root).as_posix()
        if p.is_symlink():
            errors.append(f'symlinks are not packaged: {rel}')
        if p.suffix.lower() in {'.pdf', '.docx', '.zip', '.txt'}:
            errors.append(f'unexpected bundled document or archive: {rel}')
        data = p.read_bytes()
        try:
            text = data.decode('utf-8')
        except UnicodeError:
            errors.append(f'not UTF-8 text: {rel}')
            continue
        if '\x00' in text or '\r' in text or text.startswith('\ufeff'):
            errors.append(f'nonportable text encoding or line endings: {rel}')
        if p.suffix == '.md':
            if re.search(r'\b[A-Za-z]:[/\\]|/(?:Users|home)/[^/\s]+/', text):
                errors.append(f'personal absolute path: {rel}')
            if re.search(r'barrier_omd|−107π/560|thixotropic lubrication|EVAL_R[0-9]|LEASE_ACTIVE|Our drafts \(range\)|exemplars/fluids/|claim_evidence_matrix\.csv', text):
                errors.append(f'private example or internal coordination marker: {rel}')
            if re.search(r'(?im)^\s*(?:generated_by|approved_by|checked_by|detected_by|co-authored-by|author)\s*:', text):
                errors.append(f'automatic attribution or approval field: {rel}')
            if re.search(r'(?i)(?:sk-[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|-----BEGIN .*PRIVATE KEY-----)', text):
                errors.append(f'possible credential: {rel}')
            for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)', text):
                err = local_link_error(root, p, target)
                if err:
                    errors.append(f'{rel}: {err}')
    shared = ('defensive_vs_native.md', 'native_criteria.md', 'ledger_fields.md')
    for name in shared:
        a = root / 'skills/paper-author/references' / name
        b = root / 'skills/paper-editor/references' / name
        if a.is_file() and b.is_file() and a.read_bytes() != b.read_bytes():
            errors.append(f'shared reference differs: {name}')
    checks = root / 'skills/science-ledger/templates/checks.csv'
    if checks.exists():
        rows = list(csv.reader(io.StringIO(checks.read_text(encoding='utf-8'))))
        if not rows or any(len(row) != len(rows[0]) for row in rows[1:] if row):
            errors.append('checks.csv has inconsistent columns')
        elif 'check_status' not in rows[0]:
            errors.append('checks.csv is missing check_status')
        else:
            index = rows[0].index('check_status')
            if any(row[index] != 'NOT_CHECKED' for row in rows[1:] if row):
                errors.append('blank checks template must not predeclare successful checks')
    if verify_manifest:
        path = root / MANIFEST
        if not path.exists():
            errors.append('missing MANIFEST.sha256')
        elif path.read_text(encoding='utf-8') != manifest_text(root):
            errors.append('manifest mismatch: inspect changes before refreshing')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--write-manifest', action='store_true', help='refresh checksums after reviewing intentional changes')
    args = parser.parse_args()
    errors = validate(args.root, verify_manifest=not args.write_manifest)
    if errors:
        for error in errors:
            print(f'ERROR: {error}')
        return 1
    if args.write_manifest:
        (args.root / MANIFEST).write_text(manifest_text(args.root), encoding='utf-8', newline='\n')
        print('Manifest refreshed.')
    else:
        print('PASS: project structure, references, text hygiene and manifest.')
        print('Scope: static checks only; model behavior and scientific correctness are not evaluated.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
