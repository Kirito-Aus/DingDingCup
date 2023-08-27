import pandas as pd
from sklearn.mixture import GaussianMixture
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

# 读取CSV文件
data = pd.read_csv('normalizedAndCleanedWithZ.csv')

# 选择要聚类的特征列
X = data[['duration', 'up_and_down_flow']]

# # ----------------肘部法选择K值—----------------

# 计算不同 k 值下的 SSE
sse = []
for k in range(1, 11):
    gmm = GaussianMixture(n_components = k).fit(X)
    sse.append(gmm.score(X))

# 绘制 SSE-K 折线图
plt.plot(range(1, 11), sse)
plt.xlabel('Number of clusters')
plt.ylabel('SSE')
plt.show()

# ----------------BIC选择K值—----------------

# # 计算不同 k 值下的 BIC
# bic_scores = []
# for k in range(1, 11):
#     gmm = GaussianMixture(n_components = k)
#     gmm.fit(X)
#     bic_scores.append(gmm.bic(X))

# # 绘制 BIC-K 折线图
# plt.plot(range(1, 11), bic_scores)
# plt.xlabel('Number of clusters')
# plt.ylabel('BIC')
# plt.show()