# Independence Profile｜独立于什么，共享什么

只在使用独立验证主张、交叉核对或判断共因风险时填写；普通局部写作无需新增此表。每条记录比较两条明确版本的证据，不能给单一论文一个笼统“独立性分数”。

| 字段 | 内容 |
|---|---|
| independence_record_id | 中性唯一记录ID；供independence_record_ref引用 |
| compared_evidence / source_versions | 两条证据ID、版本、范围及正在比较的主张方面 |
| assumption_independence | SHARED / PARTLY_DISTINCT / DISTINCT / UNKNOWN / NOT_APPLICABLE，并列实际假设差异 |
| implementation_independence | 同上；说明求解器、算法、库、代码来源及共同实现环节 |
| data_independence | 同上；说明样本/原始信号/标定/训练测试/预处理是否共享 |
| shared_premises | 实际共享的边界条件、本构、几何、参数、数据处理或校准；未知项明确UNKNOWN |
| evidence_locations / check_record_refs | 支持上述判断的可定位材料；没查过不能填DISTINCT |
| verification_target / remaining_common_error | 本次试图核对什么、仍无法排除什么共同错误 |

三个维度分别判断，无序位，不加总。相同合法假设下的独立实现对实现错误仍有价值，但不能排除共同错误假设；不同数据也可能共享同一失效标定或反演模型。不同作者、软件名、文件路径、专家身份或实验标签本身均不足以证明独立性。

DISTINCT只覆盖具体方面和声明范围，不意味着所有前提独立；NOT_APPLICABLE须说明该维度在所比较目标中为何不适用，不能代替未知。存在共享前提不自动使比较无价值，报告它能排除和不能排除的错误类别。若保留的核心验证主张需要某维度独立，而该维度未知/共享或未核验，则按对应必需检查维持HOLD；若只是辅助对照，则收窄为实际支持范围，不强制整篇升级审查。

旧independence_level标签继续兼容，但仅描述证据来源，不是互斥等级。PHYSICAL_EXPERIMENT不自动意味着假设/数据独立；DISTINCT_IMPLEMENTATION不自动意味着物理正确；INDEPENDENT_EXPERT不替代具体复核记录或任何人的批准。读到旧标签不能自动给三个维度填DISTINCT。
