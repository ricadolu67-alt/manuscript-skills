# Check Record Schema｜主张与检查记录的统一字段

本文件是内部层字段和枚举的共同定义；`checks.csv`、依赖图与就绪度汇总沿用这些名称。对外层字段（`statement / assertion / truth_conditions / do_not_say`）见 [ledger_schema.md](ledger_schema.md)。

## 记录单位与覆盖范围

`checks.csv` **一行对应一个 claim–check pair 的一条检查记录**。一个主张通常需要多项检查；相同 `claim_id` 可占多行，`check_id` 标识具体检查要求，`check_record_id` 唯一定位该次记录。同一检查复核时保留不同记录 ID 与版本/日期，明确哪条适用于当前版本，不能挑选过时 PASS 覆盖当前 FAIL。依赖图列出所需检查清单，防止仅登记已通过的检查。

一项检查 PASS 只覆盖该方法、证据、版本与适用条件，**不等于整个主张已核验**。没有对应版本的有效记录时，该要求为 `NOT_CHECKED`。CSV 空白示例行仅是待填模板，不是已执行记录。单独的证据表或依赖图若只显示汇总状态，须链接到记录集合，不能代替明细。

## 字段定义

| 字段 | 定义与填写规则 |
|---|---|
| `claim_id` / `claim_text` | 稳定主张编号与精确主张；限定参数、域、条件和结论强度。 |
| `claim_basis` | 主张所声称的证据形式，枚举见下；不表示已验证。 |
| `criticality` | 该检查失败的后果严重程度，使用 `CRITICAL / MAJOR / MINOR`，见下。 |
| `required_for_main_claim` | `TRUE / FALSE / UNKNOWN`；该检查是否为保留当前主贡献及其关键先决条件所必需。按依赖与科学含义判断，不从严重程度标签自动推定为 FALSE。 |
| `check_id` | 具体检查要求的稳定编号；同一主张的不同检查分别编号。 |
| `check_record_id` | 实际检查记录的唯一标识；不包含自动生成的检查者或批准者身份。 |
| `applicability_reason` | 检查为何适用/不适用及关键性判断的依据；`NOT_APPLICABLE` 必填具体理由、条件与支持位置，不能只写“不需要”。 |
| `evidence_id` / `evidence_location` | 证据编号和可定位的段落、文件、页码、数据、脚本/运行日志等；路径本身不表示已读取或执行。 |
| `evidence_type` | 证据载体：`THEOREM / EQUATION_OR_BOUND / COUNTEREXAMPLE / FIGURE / TABLE / PHYSICAL_MEASUREMENT / NUMERICAL_BENCHMARK / REAL_WORLD_DATA / OTHER`；OTHER 须说明。 |
| `check_method` | 实际实施的方法、输入和覆盖范围；计划与未执行检查明确标注，不能伪装为执行。 |
| `checked_on` | 实际检查日期/时间（ISO 8601，可未知或留空）；不是批准时间。 |
| `source_version` | 实际受检的稿件/推导/代码/数据版本或哈希，不能用当前路径冒充历史版本。 |
| `check_status` | 单项实际检查状态，枚举与含义见下。 |
| `independence_level`（兼容） | 旧来源标签，枚举见下；不是互斥等级，不自动映射三维独立性。 |
| `independence_record_ref`（按需） | 引用[独立性记录](independence_profile.md)中明确比较对象、假设/实现/数据三维及共享前提的记录ID；普通编辑留空，不能编造记录。 |
| `assumptions_scope` | 本条检查成立的假设、域、参数、精度、时间范围等。 |
| `alternative_hypothesis` | 仍相关的竞争解释；不凭空生成已排除的结论。 |
| `allowed_wording` | 仅由当前有效证据支持的最强表述；同步到对外层的 `statement`。找最强版本按 [strongest_claim.md](strongest_claim.md)。 |
| `open_issue` / `next_action` | 未决问题和下一步；拟做检查明确标 PROPOSED。 |
| `confirmation_record_ref`（可选） | 仅引用**已有、真实、获授权且与事项/版本匹配**的确认记录；不是自动填入模型、用户名、检查者或批准者的字段。无记录则省略或标未取得，不生成确认事实。该字段无需强制加入 CSV。 |

## 枚举与判定

- `claim_basis`：`THEOREM_CLAIM / CONDITIONAL_DERIVATION / ASYMPTOTIC_DERIVATION / NUMERICAL_RESULT / PHYSICAL_MEASUREMENT / EMPIRICAL_ASSOCIATION / MECHANISM_HYPOTHESIS`。
- `check_status`：`PASS`（该具体检查与版本有实证通过）、`FAIL`（已发现不满足）、`INCONCLUSIVE`（已检查但证据不足以裁决）、`NOT_CHECKED`（未执行）、`UNAVAILABLE`（所需材料或工具不可得）、`NOT_APPLICABLE`（有依据地不适用于当前主张）。未知不能填 PASS，也不能以“不适用”代替不可访问。
- `independence_level`：`SAME_WORKFLOW / DISTINCT_IMPLEMENTATION / EXTERNAL_BENCHMARK / PHYSICAL_EXPERIMENT / INDEPENDENT_EXPERT / NONE / UNKNOWN`。只作旧来源标签保留，不形成高低排序或三维独立性证明。同源自检不得冒充独立验收；主张独立核验时按需引用independence_record_ref，三个维度及共享前提见[定义](independence_profile.md)。
- `criticality`：`CRITICAL` 表示缺陷会推翻或阻断保留的主贡献/关键先决条件；这类检查的 `required_for_main_claim` 应为 TRUE。`MAJOR` 表示实质性影响可信度、解释或适用范围，**也可能是主贡献必需检查**。`MINOR` 表示不改变主要科学结论的局部表达/完整性问题；若实际会改变主贡献，应纠正严重程度分类。
- `required_for_main_claim` 判断：如果该项失败或持续未决，保留的摘要/结论或其必要依赖还能成立吗？不能则 TRUE；能且说明了不影响原因才为 FALSE；尚不能判断则 UNKNOWN。实质审查中存在可能影响主贡献的 UNKNOWN，不能给 PASS/CONDITIONAL，先 HOLD 并最小化判别。

关口与稿件状态不属于 `check_status`。按 [review_status_rules.md](review_status_rules.md) 汇总；不得把 `SCIENCE_REVIEW_PASS` 写成单项科学检查结果。作者批准、投稿授权与科学审查分开记录，不能相互推导。
