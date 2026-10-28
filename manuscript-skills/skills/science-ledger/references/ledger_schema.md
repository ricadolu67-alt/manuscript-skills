# 科学账本格式 v0.1｜三个 Skill 之间的唯一接口

`science-ledger` 写账本，`paper-author` 读对外层写正文，`paper-editor`（含复核）读正文与账本。账本分两份文件，**文件边界即角色边界**：

| 文件 | 谁写 | 谁读 | 内容 |
|---|---|---|---|
| `LEDGER_PUBLIC.md` | 科学家 | 作者、编辑、复核 | 论文可以说什么、必须带什么条件、不能说什么 |
| `LEDGER_INTERNAL.md`（+ `checks.csv`） | 科学家 | 科学家、复核 | 读过什么、查过什么、疑点、核验状态、改窄记录、评审遗留项 |

作者**不读**内部层。内部的几十项疑虑因此在结构上进不了正文；需要读者知道的，只能以“改变真假的条件”或“开放问题”的形式出现在对外层。

## 一、LEDGER_PUBLIC.md

### P0 头部

`project`、`ledger_version`、`source_versions`（推导/代码/数据/稿件版本或哈希）、`date`。

### P1 核心贡献

- `core_contribution`：一句可证伪的话。
- `reader_change`：读完后同行哪项判断会改变（一句）。

### P2 共享设定（全文只需交代一次）

每条一个 ID（`S1, S2, …`）：模型、算子/预言机、假设、记号约定、全局计账边界。作者在 Setting/Methods 写一次，结论处可引用 ID，不重复。

`S#` 中属于**计账约定**的条目（例如“匹配”在什么意义下成立）标 `accounting: yes`。这类条目帮助作者把握分寸，正文通常只需在第一次用到时用一句自然的话交代，不必升格为正式定义并在每个结论处引用。

### P3 主张

每条主张一个块：

| 字段 | 含义 |
|---|---|
| `id` | `C1, C2, …`，跨版本稳定 |
| `role` | `DECISIVE`（支撑核心贡献）/ `SUPPORTING` / `EXTENSION` / `CLASSICAL`（已有结果，引用不认领） |
| `statement` | **最强成立版本**：量词、参数域、比较对象、结论阶都写清 |
| `basis` | `THEOREM / CONDITIONAL_DERIVATION / ASYMPTOTIC / NUMERICAL / MEASUREMENT / ASSOCIATION / HYPOTHESIS / CONJECTURE` |
| `assertion` | 正文可用的断言强度：`ESTABLISHED`（prove/show/establish）· `CONDITIONAL`（在明示且未证的前提下）· `NUMERICAL`（在所测范围内）· `CONJECTURED`（猜想/候选）|
| `truth_conditions` | 去掉就会使 statement 变假的条件；或引用 `S#`。作者把它们完整放进定理/命题陈述（或模型一节），正文只作自然指代，不逐条搬进摘要和引言 |
| `reader_condition` | 每条主张通常**一条**、至多两条：不写它，普通同行就会误读结论的条件。若写两条，第二条后用括号写一句理由，说明少了它读者会怎样误读。量词属于结论本身（写进 `statement`），不占这里的名额（例如 "against a fixed interior comparator"、"in a complete liquid film"）。没有就写 `none`。这是摘要和引言唯一允许携带的条件；其余 `truth_conditions` 只进定理。只有确无必要读者条件时才写 `none`。超过两条时可合并表达或拆分主张；不得为数量目标删除决定真假的条件 |
| `evidence` | 可定位：定理号/附录/图/表/源文件§ |
| `prior_work` | 最接近先例 + 精确差异（一行） |
| `do_not_say` | 离它最近、但为假的更强说法（一行）。给作者一道明确的栅栏，而不是一团免责 |
| `rescope_note` | 可选：若是改窄后的版本，说明去掉了什么、为何不能回到原版（一行） |
| `plain_reading` | `DECISIVE` 必填：用同行读者的话一句说清它意味着什么，不带量词细节（细节在 `statement`）。例：“即使数据完全无噪声，这种估计器的误差也不会比 n^{-1/2} 下降得更快。” |
| `mechanism` | `DECISIVE` 必填：一句话说清它**为什么**成立——证明里那个让人恍然的关键点，不是引理编号。 |
| `surprise` | 可选：这条结论哪里违反直觉、或推翻了什么常见预期（一句）。 |
| `story_role` | 每条主张都填：`setup`（叙事起点：被打破的零结果、对称或经典基线，**或最简单设定里的具体意外例子**）/ `payoff` / `aside`。CLASSICAL 主张若是论文要打破的基线，标 `setup`。最一般的结论常是 `payoff`，但叙事从 `setup` 开始，摘要也一样。 |

**语言（v0.5）：** 对外层中作者会读的字段——`core_contribution`、`reader_change`、`S#`、`statement`、`truth_conditions`、`plain_reading`、`mechanism`、`surprise`、`prior_work`、`do_not_say`、P4、P6——用**英文**书写，语气是向同行讲述，不是审计记录；内部层与给用户的说明可用中文。

`plain_reading` 与 `mechanism` 是给作者讲故事的原料，不是新的科学断言：它们不得比 `statement` 更强，读起来更直白不等于范围更宽。

**`assertion` 的判定**：只由证据类型和“是否已知有错”决定，**不由独立核验是否完成决定**。一个写出了完整证明、未发现错误的定理是 `ESTABLISHED`；它是否经过独立复核，影响的是内部层的投稿就绪度（gate），不是正文措辞。已发现错误 → 不得 `ESTABLISHED`；证据只是数值 → `NUMERICAL`；推导依赖未证不等式 → `CONDITIONAL`。

### P4 推论与比较（防写弱）

由已有主张直接推出、值得写进论文、且为真的读法（只写结论本身；“与先例的比较尚不完整”“不主张优先权”这类核查缺口记在内部层 I6，不进 P4），例如：上下界在某参数区间匹配 ⇒ Θ；相对先例的改进或分离；一般情形已证却只写了特例。每条：`id (I1…)`、`statement`、`from`（由哪些 C 推出）、`regime`、`why_it_matters`（一行）。

### P5 主张关系（只写影响叙事顺序的）

`C_a REQUIRES C_b`（必须先讲 b）；`C_a CONTRASTS prior` 等。完整依赖图在内部层。

只写依赖与对照，不写重要性排序。像“C5 不能替代 C1+C2 的一般结论”这种句子，作者会把它读成“先讲一般结论”。范围限制写在该主张的 `do_not_say` 里，叙事起点由 `story_role` 决定。

### P6 开放问题

只列真正的科学开放问题（供 Discussion）。内部待办、未执行检查、包装问题**不在此列**。

### P7 证明单元（可选）

作者需要写附录证明时，账本可在此给出可公开使用的证明文本，按主张 ID 分节。只写数学，不写核验状态。

### 对外层的硬约束

1. 正文不得出现对外层没有的科学断言。
2. 每条 `DECISIVE` 主张与每条 P4 推论，都应以其 `assertion` 强度出现在正文（作者可决定顺序与详略，不可悄悄降级）。
3. `truth_conditions` 不得被编辑从定理/命题中删除；可合并措辞、可改为引用共享设定。摘要和引言里只保证 `reader_condition` 在场。
4. 对外层不得包含：检查日志、核验状态枚举、文件名、内部疑虑、免责模板。
5. 同一限定只在一处定义：出现在两条以上主张里的条件，提到 P2 成为 `S#`，各主张的 `truth_conditions` 只引用 ID；`do_not_say` 不复述已在 `S#` 中的条件。写完对外层后自查一次重复。

## 二、LEDGER_INTERNAL.md

| 节 | 内容 |
|---|---|
| I1 材料 | 实际读取的材料及阅读深度（标题/摘要/全文/逐式）；实际执行的计算；未读或不可得项 |
| I2 新颖性初筛 | 按 `templates/novelty_triage.md` |
| I3 检查记录 | `checks.csv`（字段见 `references/check_record_schema.md`），一行一条 claim–check |
| I4 依赖图 | 按 `references/claim_dependency_map.md` |
| I5 改窄与升级日志 | 每条失败或被质疑的主张：原表述 → 失败点 → 尝试过的成立范围 → 结局 `KEEP / RESCOPED / WEAKENED / WITHDRAWN` + 理由；以及防写弱扫描发现的 P4 推论来源 |
| I6 疑点 | 尚未裁决的内部疑虑；每条注明会不会改变某个 C 的真假（会 → 必须进 I3 成为检查项） |
| I7 评审遗留项 | 每条外部评审意见：来源、原文要点、处置 `ADOPTED / DECLINED(理由) / OPEN`、对账本的影响。新一轮修订前必须逐条过一遍 |
| I8 就绪度 | 科学轨 `gate_status`（`references/review_status_rules.md`）及最小解除条件 |

## 三、版本与交接

- 账本更新时提升 `ledger_version`，保留主张 ID；删除的主张在 I5 留痕。
- 作者交付正文时注明所依据的 `ledger_version`。
- 复核做双向检查：正文是否超出对外层（越界），以及 `DECISIVE` 主张与 P4 推论是否被写弱或漏写（不足）；同时检查 I7 中 `OPEN` 项是否仍未处理。
