import pandas as pd

# 是否需要将原来没有ClassType的数据改成Z类型
modifiedZ = True

# 读取app分类数据
app_class = pd.read_csv('C:/Users/N33/Desktop/Data/app_class.csv', header=None)
# 修改app_class的表头名称
app_class.columns = ['appid', 'app_class']

# 读取每天的数据
data = []
for day in range(1, 22):
    day_str = str(day).zfill(2)
    # filename = f'C:/Users/N33/Desktop/Data/day{day_str}.txt'
    filename = f'C:/Users/N33/Desktop/钉钉杯/2023年第二届钉钉杯大学生大数据挑战赛初赛题目/A题/初赛数据集/day{day_str}.txt'
    print(f'正在处理{day_str}的数据')
    # 使用header=None表示不用表头
    df = pd.read_csv(filename, header=None)
    # 修改df的表头的名称
    df.columns = ['uid', 'appid', 'app_type', 'start_day', 'start_time', 'end_day', 'end_time', 'duration', 'up_flow',
                  'down_flow']
    # 添加一个新列
    df['up_and_down_flow'] = df['up_flow'] + df['down_flow']

    # 将 'type' 列中的多个值替换为不同的值 预装-> sys， 用户-> usr
    replacement_dict = {'预装': 'sys', '用户': 'usr'}
    df['app_type'] = df['app_type'].replace(replacement_dict)

    # join操作,进行左连接，保留df中的所有数据
    print('join操作,进行左连接')
    if modifiedZ:
        # 需要修改
        df = pd.merge(df, app_class, on='appid', how='left').fillna('z')
    else:
        # 不需要修改
        df = pd.merge(df, app_class, on='appid', how='left')
        # 如果不需要修改的话，则需要将Type有缺失值的行进行删除
        cols_to_check = ['app_class']
        df = df.dropna(subset=cols_to_check, how='any')

    # 对数据进行聚合
    print('对数据进行聚合')
    grouped = df.groupby(['uid', 'app_class', 'app_type']).agg({
        'duration': 'mean',
        'up_flow': 'mean',
        'down_flow': 'mean',
        'up_and_down_flow': 'mean',
        'start_day': 'count'
    })

    grouped = grouped.rename(columns={'start_day': 'count'})

    # grouped = grouped.reset_index()

    data.append(grouped)
    print('------------')

# 合并每天的数据
print('开始合并每天的数据')
df = pd.concat(data, axis=0)
# # # 输出临时文件进行校验
# df.to_csv('tmpdf.csv', index=True)

# 需要对输出的结果再进行一次合并
grouped = df.groupby(['uid', 'app_class', 'app_type']).agg({
    'duration': 'mean',
    'up_flow': 'mean',
    'down_flow': 'mean',
    'up_and_down_flow': 'mean',
    'count': 'mean'
})

# # grouped = grouped.reset_index()

# 将结果写入文件
if modifiedZ:
    # 需要修改
    grouped.to_csv('UserUseSituationWithClassZ.csv', index=True)
else:
    # 不需要修改
    grouped.to_csv('UserUseSituation.csv', index=True)
