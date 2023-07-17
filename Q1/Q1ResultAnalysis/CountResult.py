import pandas as pd

# 读取数据
data = pd.read_csv('../Model/ClusterResult.csv')

# 对数据按照分组id进行聚类
clusters = data.groupby('cluster')

# 对某些列的值取平均值
mean_values = clusters['duration', 'up_flow', 'down_flow', 'up_and_down_flow'].mean()

# 对某些离散值的列进行统计
discrete_values = clusters['app_class'].value_counts()

mean_values.to_csv('MeanValueOfGroup.csv')
discrete_values.to_csv('AppClassCountOfGroup.csv')

# 打印结果
print('Mean values:\n', mean_values)
print('Discrete values:\n', discrete_values)