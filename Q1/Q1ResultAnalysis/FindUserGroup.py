import pandas as pd

# 找到每一个用户所属的组别

# 读取数据
df = pd.read_csv('../Model/ClusterResult.csv')

# 对每一个数据行（即图上的一个点，一个用户使用一类APP的情况），进行分数计算
df['score'] = df['duration'] + df['up_and_down_flow'] + df['count']

# 按照用户和cluster进行聚类，对score取sum，可计算出用户属于某一个Cluster的分数
sc = df.groupby(['uid', 'cluster'], as_index=False)['score'].sum()

# 取其中最高的一个作为用户的cluster
idx = sc.groupby(['uid'])['score'].idxmax()

# 索引
result = sc.loc[idx]

result.to_csv('UserCluster.csv', index=False)

