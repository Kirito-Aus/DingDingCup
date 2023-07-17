import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn import metrics
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

# 读取CSV文件
data = pd.read_csv('normalizedAndCleanedWithZ.csv', nrows = 10000)

# 选择要聚类的特征列
X = data[['duration', 'up_and_down_flow']]


# # ----------------肘部法选择K值—----------------

# # 不同的参数组合
# eps_range = np.arange(0.1, 1, 0.1)
# min_samples_range = range(2, 10)

# # 存储 SSE 值
# sse_values = []

# # 计算 SSE 值
# for eps in eps_range:
#     for min_samples in min_samples_range:
#         dbscan = DBSCAN(eps=eps, min_samples=min_samples)
#         dbscan.fit(X)
#         # 如果聚类的结果只有一个簇，则跳过当前参数组合
#         if len(set(dbscan.labels_)) == 1:
#             continue
#         sse_values.append([eps, min_samples, metrics.silhouette_score(X, dbscan.labels_)])

# # 绘制 SSE-K 折线图
# sse_values = np.array(sse_values)
# plt.plot(sse_values[:, 0], sse_values[:, 2], 'bx-')
# plt.xlabel('eps')
# plt.ylabel('Silhouette Score')
# plt.title('SSE-K Line Chart')
# plt.show()

# # 选择最优参数
# best_params = sse_values[np.argmax(sse_values[:, 2]), :2]
# print('Best eps: {}, Best min_samples: {}'.format(best_params[0], int(best_params[1])))


# ----------------可视化方法选择K值—----------------

# 调整聚类参数
eps_range = np.linspace(0.1, 1.0, 10)
min_samples_range = range(2, 10)

fig, axs = plt.subplots(len(eps_range), len(min_samples_range), figsize=(15, 15))

for i, eps in enumerate(eps_range):
    for j, min_samples in enumerate(min_samples_range):
        dbscan = DBSCAN(eps=eps, min_samples=min_samples)
        y_pred = dbscan.fit_predict(X)
        axs[i, j].scatter(data = data, x = 'duration', y = 'up_and_down_flow', c=y_pred)
        axs[i, j].set_xticks(())
        axs[i, j].set_yticks(())
        axs[i, j].set_title("eps={:.1f}, min_samples={}".format(eps, min_samples))

plt.tight_layout()
plt.show()