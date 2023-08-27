import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 读取数据
data = pd.read_csv('normalizedAndCleanedAddSumCol.csv')

# 对数据进行随机抽样
sampled_data = data.sample(n=4000)

# 绘制散点图
plt.scatter(sampled_data['duration'], sampled_data['up_and_down_flow'], s=10, alpha=0.5)

# 设置坐标轴范围和标签
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('duration')
plt.ylabel('up_and_down_flow')

# 显示图形
plt.show()