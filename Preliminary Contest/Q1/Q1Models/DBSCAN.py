import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

# ----------------DBSCAN聚类—----------------

# 读取CSV文件
data = pd.read_csv('normalizedAndCleanedWithZ.csv', nrows = 10000)

# 选择要聚类的特征列
X = data[['duration', 'up_and_down_flow']]

# 创建DBSCAN对象
dbscan = DBSCAN(eps = 0.001, min_samples = 9).fit(X)

# 预测标签
labels = dbscan.labels_
data['cluster'] = labels

# 输出聚类结果
print(data.head(50))

# 将DataFrame存储为CSV文件
data.to_csv('DBSCAN_results.csv', index = False)

# 统计cluster列中每个类别的数量
cluster_counts = data['cluster'].value_counts()

# 输出类别数量统计结果
print(cluster_counts)

# 创建一个散点图对象
fig, ax = plt.subplots()

# 绘制散点图
sns.scatterplot(data = data, x = 'duration', y = 'up_and_down_flow', hue = 'cluster')

# 添加标题和标签
plt.title('DBSCAN Clustering')
plt.xlabel('duration')
plt.ylabel('up_and_down_flow')

# 显示图形
plt.show()

