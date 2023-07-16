import pandas as pd
import numpy as np
# 是否需要新添加列
needNewCol = True

# 读取数据
data = pd.read_csv('../UserUseSituationWithClassZtmp.csv')

# 如果需要添加新列
data['up_and_down_flow'] = data.apply(lambda row: row['up_flow'] + row['down_flow'], axis = 1)

data.to_csv('tmpUpAndDownFlowTable.csv', index=False)

# 选择需要处理的列
if needNewCol:
    cols_to_process = ['duration', 'up_flow', 'down_flow', 'up_and_down_flow']
else:
    cols_to_process = ['duration', 'up_flow', 'down_flow']


# 对所选列进行 Min-Max 规范化
# 将数据先归一化到[0,1]之间
data[cols_to_process] = (data[cols_to_process] - data[cols_to_process].min()) / (data[cols_to_process].max() - data[cols_to_process].min())

# 使用Turkey方法，基于箱线图的异常值检测
# 计算 Q1、Q3 和 IQR，定义阈值 k
Q1 = data[cols_to_process].quantile(0.25)
Q3 = data[cols_to_process].quantile(0.75)
IQR = Q3 - Q1
k = 1.5

# 使用 Turkey 方法检查异常值，并将数据限制在 [0,1] 范围内
data[cols_to_process] = np.clip(data[cols_to_process], 0, 1) # 将数据限制在 [0,1] 范围内
data = data[~((data[cols_to_process] < (Q1 - k * IQR)) | (data[cols_to_process] > (Q3 + k * IQR))).any(axis=1)] # 去除异常值

# 对整个数据集进行 Min-Max 规范化
data[cols_to_process] = (data[cols_to_process] - data[cols_to_process].min()) / (data[cols_to_process].max() - data[cols_to_process].min())

# 将数据限制在 [0,1] 范围内
data[cols_to_process] = data[cols_to_process].clip(0, 1)

if needNewCol:
    data.to_csv('normalizedAndCleanedAddSumCol.csv', index=False)
else:
    data.to_csv('normalizedAndCleaned.csv', index=False)