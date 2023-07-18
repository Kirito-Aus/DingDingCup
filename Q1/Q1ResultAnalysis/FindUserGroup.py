import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 找到每一个用户所属的组别

# 判断所选的算法
algorithm = 'DBSCAN'
# kmeans
# GMM
# DBSCAN

# 读取数据
df = pd.read_csv(f'../Model/Results/{algorithm}_results.csv')

# 对每一个数据行（即图上的一个点，一个用户使用一类APP的情况），进行分数计算
df['score'] = df['duration'] + df['up_and_down_flow'] + df['count']
# df.to_csv('df1.csv')

# 按照用户和cluster进行聚类，对score取sum，可计算出用户属于某一个Cluster的分数
sc = df.groupby(['uid', 'cluster'], as_index=False).agg({
    'score': "sum",
    'duration': "mean",
    "up_and_down_flow": "mean"
})

# sc.to_csv('df2.csv', index=True)
  #  ['score'].sum()

# 取其中最高的一个作为用户的cluster
idx = sc.groupby(['uid'])['score'].idxmax()

# 索引
result = sc.loc[idx]

# 输出结果
result.to_csv(f'./UserCluster/{algorithm}_UserCluster.csv', index=False)

# 统计cluster列中每个类别的数量
cluster_counts = result['cluster'].value_counts()

# 输出类别数量统计结果
print(cluster_counts)

# 创建一个散点图对象
fig, ax = plt.subplots()

# 绘制散点图
sns.scatterplot(data = result, x = 'duration', y = 'up_and_down_flow', hue = 'cluster')

plt.title(f'{algorithm} User Clustering')
plt.xlabel('duration')
plt.ylabel('up_and_down_flow')
plt.savefig(f'./UserCluster/{algorithm}UserCluster.png')

# 显示图形
plt.show()

