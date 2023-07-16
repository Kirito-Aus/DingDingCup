import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN


# 读取CSV文件
data = pd.read_csv('normalizedAndCleanedAddSumCol.csv')

# 选择要聚类的特征列
X = data[['duration', 'up_and_down_flow']]


''' ______________KMEANS模型________________
'''
# 创建KMeans模型并拟合数据
kmeans = KMeans(n_clusters=5, random_state=0).fit(X)

# 将聚类结果添加到数据集中
data['cluster'] = kmeans.labels_

# 输出聚类结果
print(data.head(500))
# print(data[data['cluster'] == 2])

# 统计cluster列中每个类别的数量
cluster_counts = data['cluster'].value_counts()

# 输出结果
print(cluster_counts)
'''
______________KMEANS模型________________'''




''' ______________GMM模型________________
# 创建GMM对象
gmm = GaussianMixture(n_components=5, random_state=42)

# 拟合模型
gmm.fit(X)

# 预测标签
labels = gmm.predict(X)
data['cluster'] = labels

______________GMM模型________________'''





''' ______________DBSCAN模型________________
# 创建DBSCAN对象
dbscan = DBSCAN(eps=0.3, min_samples=5)

# 拟合模型
dbscan.fit(X)

# 预测标签
labels = dbscan.labels_
data['cluster'] = labels



______________DBSCAN模型________________'''



# 创建一个散点图对象
fig, ax = plt.subplots()

# 绘制散点图
sns.scatterplot(data=data[(data['duration'] <= 100000) & (data['up_and_down_flow'] <= 10000)],
                x='duration', y='up_and_down_flow', hue='cluster')

# 添加标题和标签
plt.title('Clustering')
plt.xlabel('duration')
plt.ylabel('up_and_down_flow')

# 显示图形
plt.show()

