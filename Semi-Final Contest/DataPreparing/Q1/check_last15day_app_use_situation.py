# 获取用户在后15天是否使用某种类型的APP
import string

import pandas as pd

path = 'C:/Users/N33/Desktop/钉钉杯/2023年第二届钉钉杯大学生大数据挑战赛初赛题目/A题/初赛数据集'

def get_use_situation_of_each_type():
    # 首先读取后15天数据，取出使用各个类型APP的使用情况统计
    dfs = []
    for day in range(16, 31):
        day_str = str(day).zfill(2)
        filename = path + f'/day{day_str}.txt'
        print(f'正在处理{day_str}的数据')
        # 使用header=None表示不用表头
        df_tmp = pd.read_csv(filename, header=None)
        df_tmp.columns = ['uid', 'appid', 'app_type', 'start_day', 'start_time', 'end_day', 'end_time', 'duration', 'up_flow', 'down_flow']
        df_tmp = df_tmp.drop(columns=['app_type', 'start_day', 'start_time', 'end_day', 'end_time'], axis=1)
        # 拼接每天的数据
        dfs.append(df_tmp)
        df_tmp = None

    print('开始进行每日数据的拼接')
    df = pd.concat(dfs, axis=0)
    dfs = None
    # # 修改df的表头的名称
    # df.columns = ['uid', 'appid', 'app_type', 'start_day', 'start_time', 'end_day', 'end_time', 'duration', 'up_flow', 'down_flow']
    # df = df.drop(columns=['app_type', 'start_day', 'start_time', 'end_day', 'end_time'], axis=1)

    # 剔除异常值
    df = df.dropna()
    df = df[df['duration'] != 0]  # 剔除使用时长为0的行
    # 判断使用流量，如果上下行流量为0，则认为没有使用
    # 对于上下行流量为0的，则可能是一些系统工具，认为对用户的使用没有影响
    df['up_and_down_flow'] = df['up_flow'] + df['down_flow']
    df = df[df['up_and_down_flow'] != 0]
    df = df[df['duration'] >= 10]

    # 为每条数据添加class列
    # 特征工程，添加APP类型列，将APP的类型转换成数字，便于后续分析
    print('开始为每个class字母进行替换')
    letter_to_number = {letter: i + 1 for i, letter in enumerate(string.ascii_lowercase)}
    # 对文档中的字母进行替换
    app_class_df = pd.read_csv(path + '/app_class.csv')
    app_class_df.columns = ['appid', 'class']
    app_class_df['class'] = app_class_df['class'].map(letter_to_number)
    app_class_dict = dict(zip(app_class_df['appid'], app_class_df['class']))
    # 生成分类列
    df['class'] = df['appid'].map(app_class_dict)

    # 判断使用各类APP的情况，按照APPType和userid进行聚类(统计每一类APP是否有被使用）
    print('开始检查每人对每类APP的使用情况')
    df = df[['class', 'uid']].drop_duplicates()
    # use_app_use_situation = df.groupby(['class', 'uid'], as_index=False)['start_day'].count()
    # use_app_use_situation
    # 获得的结果是后面20天的每个用户的APP使用情况，只有使用过的数据，即出现的每一行该用户都是使用过的
    df = df.dropna(axis=0)
    df.to_csv('./Results/last_15day_app_use_situation.csv', index=False)



    # 获得一个可选的APP类型列表
    # 创建空的 DataFrame
    # app_usable = pd.DataFrame(columns=['class'])
    # # 遍历字母范围并添加到 DataFrame
    # for letter_num in range(1, 21):
    #     app_usable = app_usable.append({'class': letter_num}, ignore_index=True)
    # 然后开始构建输出，为每个用户构建20类APP是否使用的行，如果使用了这个APP，则设置为True


    # use_app_use_situation['key'] = 1
    # app_usable['key'] = 1
    # user_of_all_app = pd.merge(use_app_use_situation, app_usable, on='key').drop('key', axis=1)
    # # 为原有数据添加一列表示是否使用过该APP，默认为False
    # user_of_all_app['used_class'] = False
    # # 根据app_usable去填充user_of_all_app的used_app列
    # user_of_all_app = pd.merge(user_of_all_app, app_usable, on=['uid', 'app_class'], how='left')
    # # 根据使用天数来进行判断，如果非空则认为使用过，否则认为没有，然后再删除这个开始天的列
    # condition = user_of_all_app['start_day'] != ''
    # user_of_all_app.loc[condition, 'used_class'] = True
    # user_of_all_app.drop('start_day')

# 获取后15天每类APP的日军使用时长
def get_use_daily_duration_of_class():
    # 首先读取后15天数据，取出使用各个类型APP的使用情况统计
    dfs = []
    for day in range(16, 31):
        day_str = str(day).zfill(2)
        filename = path + f'/day{day_str}.txt'
        print(f'正在处理{day_str}的数据')
        # 使用header=None表示不用表头
        df_tmp = pd.read_csv(filename, header=None, dtype={1: int})
        df_tmp.columns = ['uid', 'appid', 'app_type', 'start_day', 'start_time', 'end_day', 'end_time', 'duration', 'up_flow', 'down_flow']
        df_tmp = df_tmp.drop(columns=['app_type', 'start_day', 'start_time', 'end_time'], axis=1)
        # 拼接每天的数据
        dfs.append(df_tmp)
        df_tmp = None

    print('开始进行每日数据的拼接')
    df = pd.concat(dfs, axis=0)
    dfs = None

    # 剔除异常值
    df = df.dropna()
    df = df[df['duration'] != 0]  # 剔除使用时长为0的行
    # 判断使用流量，如果上下行流量为0，则认为没有使用
    # 对于上下行流量为0的，则可能是一些系统工具，认为对用户的使用没有影响
    df['up_and_down_flow'] = df['up_flow'] + df['down_flow']
    df = df[df['up_and_down_flow'] != 0]
    df = df[df['duration'] >= 10]

    # 为每条数据添加class列
    # 特征工程，添加APP类型列，将APP的类型转换成数字，便于后续分析
    print('开始为每个class字母进行替换')
    letter_to_number = {letter: i + 1 for i, letter in enumerate(string.ascii_lowercase)}
    # 对文档中的字母进行替换
    app_class_df = pd.read_csv(path + '/app_class.csv')
    app_class_df.columns = ['appid', 'class']
    app_class_df['class'] = app_class_df['class'].map(letter_to_number)
    app_class_dict = dict(zip(app_class_df['appid'], app_class_df['class']))
    # 生成分类列
    df['class'] = df['appid'].map(app_class_dict)

    print('开始统计用户对每类APP的日均使用时长')
    # 获取用户对每一类APP的日均使用时长
    # 1）分别计算每天使用每类APP的使用时长
    df = df.groupby(['uid', 'class', 'end_day'], as_index=False)['duration'].sum()
    # 2）对每天的数据求均值
    df = df.groupby(['uid', 'class'], as_index=False)['duration'].mean()
    # 输出的结果就是用户对该类APP有效日均的使用时长
    df.to_csv('./Results/last_15day_app_daily_use_time.csv', index=False)



get_use_daily_duration_of_class()