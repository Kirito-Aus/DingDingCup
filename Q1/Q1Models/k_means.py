import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ----------------KMeans聚类—----------------

# 读取CSV文件
data = pd.read_csv('normalizedAndCleanedWithZ.csv')

# 选择要聚类的特征列
X = data[['duration', 'up_and_down_flow']]

# 创建KMeans模型并拟合数据
kmeans = KMeans(n_clusters = 5).fit(X)

# 将聚类结果添加到数据集中
data['cluster'] = kmeans.labels_

# 输出聚类结果
print(data.head(50))

# 将DataFrame存储为CSV文件
data.to_csv('kmeans_results.csv', index = False)

# 统计cluster列中每个类别的数量
cluster_counts = data['cluster'].value_counts()

# 输出类别数量统计结果
print(cluster_counts)

# 创建一个散点图对象
fig, ax = plt.subplots()

# 绘制散点图
sns.scatterplot(data = data, x = 'duration', y = 'up_and_down_flow', hue = 'cluster')

# 添加标题和标签
plt.title('KMeans Clustering')
plt.xlabel('duration')
plt.ylabel('up_and_down_flow')

# 显示图形
plt.show()

