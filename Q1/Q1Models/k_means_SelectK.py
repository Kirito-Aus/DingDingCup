import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

# 读取CSV文件
data = pd.read_csv('normalizedAndCleanedWithZ.csv')

# 选择要聚类的特征列
X = data[['duration', 'up_and_down_flow']]

# # ----------------肘部法选择K值—----------------

# # 计算不同聚类数k对应的SSE值
# sse = []
# for k in range(1, 11):
#     kmeans = KMeans(n_clusters = k).fit(X)
#     sse.append(kmeans.inertia_)

# # 绘制聚类数k与SSE之间的关系曲线
# plt.plot(range(1, 11), sse)
# plt.xlabel('Number of clusters')
# plt.ylabel('SSE')
# plt.show()



# ----------------BIC选择K值—----------------

def gap_statistic(data, k_max):
    reference = np.random.rand(*data.shape)
    reference_sse = []
    for k in range(1, k_max + 1):
        kmeans = KMeans(n_clusters = k).fit(reference)
        reference_sse.append(kmeans.inertia_)

    sse = []
    for k in range(1, k_max + 1):
        kmeans = KMeans(n_clusters = k).fit(data)
        sse.append(kmeans.inertia_)

    gap = np.log(reference_sse) - np.log(sse)
    return gap, np.log(reference_sse), np.log(sse)

# 计算 Gap Statistic
gap, reference_sse, sse = gap_statistic(X, k_max = 10)

# 绘制 Gap Statistic-K 折线图
plt.plot(range(1, 11), gap, '-o')
plt.xlabel('Number of clusters')
plt.ylabel('Gap Statistic')
plt.show()