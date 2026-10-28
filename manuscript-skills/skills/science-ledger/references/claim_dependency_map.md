# Claim Dependency Map｜主张、关系与必要检查

用于 `BUILD` 与 `READINESS`；`UPDATE` 只改受影响的节点。主张与所需检查沿用 [check_record_schema.md](check_record_schema.md)，阻断汇总见 [review_status_rules.md](review_status_rules.md)。下表是索引，不能用一项PASS代表整个主张。

| claim_id | 精确主张 / claim_basis | 适用条件与证据位置 | 论证功能 | required check_id / record links | depends_on（仅REQUIRES索引） |
|---|---|---|---|---|---|
| C1 | | | | | |

## 关系表：先分类，再判断影响

| source_claim | relation_type | target_claim / affected_claim_aspect | 必要性或关联依据 / scope | independence_record_ref（适用时） |
|---|---|---|---|---|
| | UNKNOWN | | | |

三元组按通常英文语义读取：`A REQUIRES B`是“A必须依赖B”，因此B受阻向A传播；`A SUPPORTS B`、`A EXPLAINS B`则分别是“A支持B”“A解释B”。图上关系箭头与阻断传播方向可能不同，必须标类型，不能只凭箭头推断。affected_claim_aspect写清实际受影响的观测、导出量或机制归因。

| 类型 | 含义与阻断处理 |
|---|---|
| REQUIRES | source的该结论必须以target成立为前提；target关键要求失败或未决，向依赖它的source传播HOLD。辅助成功检查不能覆盖它。 |
| SUPPORTS | 增加支持但非必要；不自动传播先决阻断。支持失效后仍须复核target自己的证据是否充分，不能因这个标签保留实际已无依据的结论。 |
| CROSS_CHECKS | 两条证据作交叉核对；分别审查各自有效性、可比范围及独立性。关系名称不证明它们独立或正确，也不自动相互传递PASS/HOLD。 |
| CONTRADICTS | 在声称的共同范围内存在冲突；先查参数、定义、误差与适用范围。实际影响主贡献且未裁决的冲突导致HOLD，但不自动判双方都错。 |
| EXPLAINS | source为观测/结果提供解释；source受阻则解释不可通过，不自动否定独立观测。将“观察到现象”与“已证实该机制”拆成主张；后者若逻辑上需要source，应另列REQUIRES。 |
| UNKNOWN | 旧记录或材料不足尚不能分类；若可能是必要关系或主贡献冲突，先HOLD并最小化判别，不能自动降为SUPPORTS。 |

对主张A，`depends_on`只列已确认的`A REQUIRES B`中的B。旧列表不能批量解释成必要或非必要关系：依据原始推理分类；无法确认则保留UNKNOWN。论证功能PREREQUISITE/DECISIVE/EXPLANATORY/VALIDATION/EXTENSION不是关系类型，也不自动决定传播。

## Required-check inventory

| claim_id | check_id / requirement | criticality | required_for_main_claim | applicability_reason | check_status / check_record_id | source_version |
|---|---|---|---|---|---|---|
| | | MAJOR | UNKNOWN | | NOT_CHECKED / | |

如果理论证明待核，数值响应在指定模型内的复现、独立实验的原始观测可以各自按证据审查；将实验解释为该理论机制的主张仍可能受阻。若实验量本身由该理论作校准或反演，导出量也有真正的REQUIRES，不能只凭PHYSICAL_MEASUREMENT标签声称独立。

最终列出受阻节点及关系路径、仍有证据的独立结果、未决冲突和最小下一步。保留主贡献含受阻解释时整体仍HOLD；收窄/移除前先按 [strongest_claim.md](strongest_claim.md) 找成立范围；之后更新图、检查清单与贡献判断并重审，不自动删除失败记录或继承旧PASS。
