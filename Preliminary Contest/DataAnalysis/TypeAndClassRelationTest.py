import pandas as pd
from scipy.stats import chi2_contingency

# 读取离散变量数据
data = pd.read_csv('AllAppIdAndAppClass.csv')

# 生成列联表
contingency_table = pd.crosstab(data['app_type'], data['app_class'])

# 将结果输出
contingency_table.to_csv("TypeAndClassRelation.csv", index=True)

# 进行卡方检验
chi2, p_value, dof, expected = chi2_contingency(contingency_table)


# 输出卡方检验结果
print('卡方值：', chi2)
print('p-value：', p_value)
print('自由度：', dof)
print('期望值：', expected)