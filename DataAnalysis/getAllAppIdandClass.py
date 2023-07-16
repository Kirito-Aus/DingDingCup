import pandas as pd
import numpy as np
# 读取每天的数据
data = []
for day in range(1, 22):
    day_str = str(day).zfill(2)
    filename = f'C:/Users/N33/Desktop/钉钉杯/2023年第二届钉钉杯大学生大数据挑战赛初赛题目/A题/初赛数据集/day{day_str}.txt'
    # filename = f'C:/Users/N33/Desktop/钉钉杯/2023年第二届钉钉杯大学生大数据挑战赛初赛题目/A题/初赛数据集/day{day_str}.txt'
    # filename = f'C:/Users/N33/Desktop/Data/day{day_str}.txt'
    # 使用header=None表示不用表头，需要appid和apptype列的数据（索引从0开始）
    df = pd.read_csv(filename, sep=',', usecols=[1, 2], header=None)
    print(f'读取第{day}天的数据')
    # 不需要删除表头
    # df = df.iloc[1:]
    data.append(df)

print('合并每天的数据')
# 合并每天的数据
df = pd.concat(data, axis=0)
# 修改df的表头的名称
df.columns = ['appid', 'app_type']
key = df.drop_duplicates(subset='appid')

print('进行join')
# 读取app分类数据
app_class = pd.read_csv('C:/Users/N33/Desktop/Data/app_class.csv', header=None)
# 修改app_class的表头名称
app_class.columns = ['appid', 'app_class']

# join操作,进行左连接，保留df中的所有数据
df = pd.merge(key, app_class, on='appid', how='left').fillna('z')

# keys = df[['appid', 'app_class']].drop_duplicates()
# 对数据进行聚合
# grouped = df.groupby(by=['appid']).
# grouped = grouped.reset_index()
df.to_csv('AllAppIdAndAppClass.csv', index=False)

# print(df)
