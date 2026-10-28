"""Regression tests for distribution checks using isolated temporary fixtures."""

import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('validator', Path(__file__).resolve().parents[1] / 'scripts/validate.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class DistributionChecks(unittest.TestCase):
    def setUp(self):
        self.workspace = tempfile.TemporaryDirectory()
        self.addCleanup(self.workspace.cleanup)
        self.root = Path(self.workspace.name)
        for name in ('README.md', 'LICENSE', 'CONTRIBUTING.md', 'VERSION', 'docs/USAGE.md', '.gitattributes'):
            self.write(name, 'Fixture\n')
        self.write('.gitattributes', '* text eol=lf\n')
        for name in validator.SKILLS:
            self.write(f'skills/{name}/LICENSE', 'Fixture\n')
            self.write(f'skills/{name}/SKILL.md', f'---\nname: {name}\ndescription: >\n  A concrete test skill.\n---\n\nFixture\n')
        self.refresh()

    def write(self, name, text):
        p = self.root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding='utf-8', newline='\n')

    def refresh(self):
        self.write(validator.MANIFEST, validator.manifest_text(self.root))

    def test_valid_minimal_project(self):
        self.assertEqual(validator.validate(self.root), [])

    def test_missing_skill_rejected(self):
        self.assertTrue(any('missing skill' in e for e in validator.validate(self.root / 'absent')))

    def test_missing_local_reference_rejected(self):
        self.write('README.md', '[missing](docs/missing.md)\n')
        self.assertTrue(any('broken local link' in e for e in validator.validate(self.root)))

    def test_reference_cannot_escape_project(self):
        self.write('README.md', '[outside](../outside.md)\n')
        self.assertTrue(any('escapes project' in e for e in validator.validate(self.root)))

    def test_normal_external_url_allowed(self):
        self.write('README.md', '[docs](https://example.org/docs)\n')
        self.refresh()
        self.assertEqual(validator.validate(self.root), [])

    def test_content_change_detected(self):
        self.write('docs/USAGE.md', 'Changed after packaging\n')
        self.assertTrue(any('manifest mismatch' in e for e in validator.validate(self.root)))

    def test_mismatched_skill_name_rejected(self):
        self.write('skills/science-ledger/SKILL.md', '---\nname: another-skill\ndescription: A test\n---\n')
        self.assertTrue(any('name does not match' in e for e in validator.validate(self.root)))

    def test_third_party_pdf_rejected(self):
        self.write('paper.pdf', 'a document should not be bundled\n')
        self.assertTrue(any('unexpected bundled document' in e for e in validator.validate(self.root)))

    def test_copied_personal_path_rejected(self):
        self.write('README.md', 'Local source: ' + 'Z:' + '/private/project\n')
        self.assertTrue(any('personal absolute path' in e for e in validator.validate(self.root)))

    def test_unfinished_description_rejected(self):
        text = '---\nname: science-ledger\ndescription: >\n---\n'
        self.assertTrue(validator.metadata_errors(text, 'science-ledger'))

    def test_internal_measurement_table_rejected(self):
        self.write('docs/USAGE.md', '| Our drafts (range) | Human references |\n')
        self.assertTrue(any('internal coordination marker' in e for e in validator.validate(self.root)))

    def test_lf_checkout_rule_required(self):
        self.write('.gitattributes', '* text=auto\n')
        self.assertTrue(any('LF checkout rule' in e for e in validator.validate(self.root)))


if __name__ == '__main__':
    unittest.main()
