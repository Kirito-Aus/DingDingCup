import pandas as pd
from sklearn.mixture import GaussianMixture
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ----------------GMM聚类—----------------

# 读取CSV文件
data = pd.read_csv('normalizedAndCleanedWithZ.csv')

# 选择要聚类的特征列
X = data[['duration', 'up_and_down_flow']]

# 创建GMM对象
gmm = GaussianMixture(n_components = 4).fit(X)

# 预测标签
labels = gmm.predict(X)
data['cluster'] = labels

# 输出聚类结果
print(data.head(50))

# 将DataFrame存储为CSV文件
data.to_csv('GMM_results.csv', index = False)

# 统计cluster列中每个类别的数量
cluster_counts = data['cluster'].value_counts()

# 输出结果
print(cluster_counts)

# 创建一个散点图对象
fig, ax = plt.subplots()

# 绘制散点图
sns.scatterplot(data = data, x = 'duration', y = 'up_and_down_flow', hue = 'cluster')

# 添加标题和标签
plt.title('GMM Clustering')
plt.xlabel('duration')
plt.ylabel('up_and_down_flow')

# 显示图形
plt.show()

