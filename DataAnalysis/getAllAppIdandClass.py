# 获取所有出现过的APPId和它们对应的type和Class
# 已对出现的type中异常值进行处理

import pandas as pd

data = []
for day in range(1, 22):
    day_str = str(day).zfill(2)
    filename = f'C:/Users/N33/Desktop/钉钉杯/2023年第二届钉钉杯大学生大数据挑战赛初赛题目/A题/初赛数据集/day{day_str}.txt'
    # filename = f'C:/Users/N33/Desktop/Data/day{day_str}.txt'
    # 使用header=None表示不用表头，需要appid和apptype列的数据（索引从0开始）
    df = pd.read_csv(filename, sep=',', usecols=[1, 2], header=None)
    print(f'读取第{day}天的数据')
    data.append(df)

print('合并每天的数据')
# 合并每天的数据
df = pd.concat(data, axis=0)

# 修改df的表头的名称
df.columns = ['appid', 'app_type']

# 将 'type' 列中的多个值替换为不同的值 预装-> sys， 用户-> usr
replacement_dict = {'预装': 'sys', '用户': 'usr'}
df['app_type'] = df['app_type'].replace(replacement_dict)

print('进行join')
# 读取app分类数据
app_class = pd.read_csv('C:/Users/N33/Desktop/Data/app_class.csv', header=None)
# 修改app_class的表头名称
app_class.columns = ['appid', 'app_class']

# join操作,进行左连接，保留df中的所有数据
df = pd.merge(df, app_class, on='appid', how='left').fillna('z')

# 将重复数据删除
df = df.drop_duplicates(subset=['appid'], keep='first')

# 对数据进行聚合
df.to_csv('AllAppIdAndAppClass.csv', index=False)

# print(df)
