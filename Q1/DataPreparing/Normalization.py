import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 是否有Z值
isContainZ = True

# 读取数据
if isContainZ:
    data = pd.read_csv('./UserUseSituationWithClassZ.csv')
else:
    data = pd.read_csv('./UserUseSituation.csv')

# 选择需要处理的列
cols_to_process = ['duration', 'up_flow', 'down_flow', 'up_and_down_flow', 'count']

# 对所选列进行 Min-Max 规范化
# 将数据先归一化到[0,1]之间
data[cols_to_process] = (data[cols_to_process] - data[cols_to_process].min()) / (
            data[cols_to_process].max() - data[cols_to_process].min())

# 绘制散点图
plt.scatter(data['duration'], data['up_and_down_flow'], s=10, alpha=0.5)
# 设置坐标轴范围和标签
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('duration')
plt.ylabel('up_and_down_flow')
# 显示图形
plt.show()

# 使用Turkey方法，基于箱线图的异常值检测
# 计算 Q1、Q3 和 IQR，定义阈值 k
Q1 = data[cols_to_process].quantile(0.25)
Q3 = data[cols_to_process].quantile(0.75)
IQR = Q3 - Q1
k = 1.5

# 使用 Turkey 方法检查异常值，并将数据限制在 [0,1] 范围内
data[cols_to_process] = np.clip(data[cols_to_process], 0, 1)  # 将数据限制在 [0,1] 范围内
data = data[~((data[cols_to_process] < (Q1 - k * IQR)) | (data[cols_to_process] > (Q3 + k * IQR))).any(axis=1)]  # 去除异常值

# 绘制散点图
plt.scatter(data['duration'], data['up_and_down_flow'], s=10, alpha=0.5)
# 设置坐标轴范围和标签
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('duration')
plt.ylabel('up_and_down_flow')
# 显示图形
plt.show()

# 对整个数据集进行 Min-Max 规范化
data[cols_to_process] = (data[cols_to_process] - data[cols_to_process].min()) / (
            data[cols_to_process].max() - data[cols_to_process].min())

# 将数据限制在 [0,1] 范围内
data[cols_to_process] = data[cols_to_process].clip(0, 1)

# 绘制散点图
plt.scatter(data['duration'], data['up_and_down_flow'], s=10, alpha=0.5)
# 设置坐标轴范围和标签
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('duration')
plt.ylabel('up_and_down_flow')
# 显示图形
plt.show()
if isContainZ:
    data.to_csv('normalizedAndCleanedWithZ.csv', index=False)
else:
    data.to_csv('normalizedAndCleaned.csv', index=False)
