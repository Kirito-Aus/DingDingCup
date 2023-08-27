import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ----------------用户分类筛选—----------------

# 读取CSV文件
df = pd.read_csv('kmeans_results.csv')

# 根据列uid和列cluster进行分组，并计算列count的总和
df_grouped = df.groupby(['uid', 'cluster'])['count'].sum().reset_index()

# 将列count的总和添加到DataFrame中
df['sum_count'] = df.apply(lambda row: df_grouped.loc[(df_grouped['uid'] == row['uid']) & (df_grouped['cluster'] == row['cluster']), 'count'].iloc[0], axis=1)

# 将DataFrame存储为CSV文件
df.to_csv('kmeans_output1.csv', index = False)

# 根据列uid和列cluster进行去重
df.drop_duplicates(subset=['uid', 'cluster'], keep='first', inplace = True)

# 将DataFrame存储为CSV文件
df.to_csv('kmeans_output2.csv', index = False)

# 根据列uid进行分组，并保留列sum_count数值最大的行
df = df.loc[df.groupby('uid')['sum_count'].idxmax()]

# 将DataFrame存储为CSV文件
df.to_csv('kmeans_output3.csv', index = False)