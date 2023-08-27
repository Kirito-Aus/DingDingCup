import pandas as pd
import time
import datetime
import pytz
from concurrent.futures import ThreadPoolExecutor

# 是否需要将原来没有ClassType的数据改成Z类型
modifiedZ = True
max_workers_num = 8

# 读取app分类数据
app_class = pd.read_csv('C:/Users/N33/Desktop/Data/app_class.csv', header=None)
# 修改app_class的表头名称
app_class.columns = ['appid', 'app_class']


# 定义一个函数，将datetime对象转换为带有北京时区信息的时间戳
def convert_to_timestamp_with_tz(dt):
    tz = pytz.timezone('Asia/Shanghai')
    dt_with_tz = tz.localize(dt)
    # 北京和上海是同一个时区
    beijing_tz = pytz.timezone('Asia/Shanghai')
    dt_with_beijing_tz = dt_with_tz.astimezone(beijing_tz)
    return int(dt_with_beijing_tz.timestamp())

# 对一个group内的数据进行抽样，并计算时间
def sample_and_time_cal(group):
    # print(f'当前group的长度为{len(group)}')
    if len(group) > 100:
        # 需要进行抽样
        group = group.sample(frac=0.3)
        # print(f'需要进行抽样，抽样过后长度为{len(group)}')
    elif len(group) > 300:
        group = group.sample(frac=0.1)
    # 接着对该组（抽样）的数据进行时间计算
    # print(f' 1）增加一个新列表示使用的中间时间的时间戳, 当前时间')
    # # 使用 apply() 方法计算新列的值
    date_time = '2000-01-01 '
    group['start_time_with_date'] = date_time + group['start_time']
    time_tuples = pd.to_datetime(group['start_time_with_date']).apply(lambda x: convert_to_timestamp_with_tz(x))
    group['start_timestamp'] = time_tuples
    mid_time_stamp = time_tuples + group['duration'] / 2
    # 获取某个时间戳
    day2_timestamp = 946742400
    mid_time_stamp = mid_time_stamp.apply(lambda x: x - 86400 if x > day2_timestamp else x)
    group['mid_time_stamp'] = mid_time_stamp
    return group

# 读取每天的数据
def process_data(day):
    day_str = str(day).zfill(2)
    # filename = f'C:/Users/N33/Desktop/Data/day{day_str}.txt'
    filename = f'C:/Users/N33/Desktop/钉钉杯/2023年第二届钉钉杯大学生大数据挑战赛初赛题目/A题/初赛数据集/day{day_str}.txt'
    print(f'正在处理{day_str}的数据')
    # 使用header=None表示不用表头
    print(f'开始读入{day_str}的数据')
    df = pd.read_csv(filename, header=None)
    # 修改df的表头的名称
    df.columns = ['uid', 'appid', 'app_type', 'start_day', 'start_time', 'end_day', 'end_time', 'duration', 'up_flow',
                  'down_flow']

    df = df.drop([ 'up_flow', 'down_flow'], axis=1)

    # join操作,进行左连接，保留df中的所有数据
    print(f'对{day_str}的数据进行join操作,进行左连接')
    if modifiedZ:
        # 需要修改
        df = pd.merge(df, app_class, on='appid', how='left').fillna('z')
    else:
        # 不需要修改
        df = pd.merge(df, app_class, on='appid', how='left')
        # 如果不需要修改的话，则需要将Type有缺失值的行进行删除
        cols_to_check = ['app_class']
        df = df.dropna(subset=cols_to_check, how='any')

    # 对时间进行处理，获得开始时间和结束时间的时间戳
    # 1、增加一个新列表示使用的中间时间

    now = datetime.datetime.now()

    # 对数据进行聚合
    print(f'对{day_str}数据进行聚合, 当前时间为{now}')
    grouped = df.groupby(['uid', 'app_class', 'app_type'], as_index=False).apply(sample_and_time_cal)
    grouped_agg = grouped.groupby(['uid', 'app_class', 'app_type'], as_index=False).agg({
        'mid_time_stamp': 'mean'
    })
    now = datetime.datetime.now()
    print(f'{day_str}处理完成, 当前时间为{now}')
    print('------------')
    return grouped

# 多线程处理任务
def multi_processor_do_preprocessingOnlyForTime():
    # 创建线程池
    executor = ThreadPoolExecutor(max_workers=max_workers_num)

    # 提交任务到线程池中
    tasks = [executor.submit(process_data, day) for day in range(1, 22)]

    # 等待所有任务完成
    results = [task.result() for task in tasks]

    # 合并每天的数据
    now = datetime.datetime.now()
    print('所有任务完成，开始合并每天的数据, 当前时间为:', now)
    df = pd.concat(results, axis=0)

    # 需要对输出的结果再进行一次合并
    grouped = df.groupby(['uid', 'app_class', 'app_type']).agg({
        'mid_time_stamp': 'mean'
    })


    # 将时间戳转换为时间元组
    grouped['mid_time'] = grouped['mid_time_stamp'].apply(lambda x: time.strftime("%H:%M:%S", time.localtime(x)))

    grouped = grouped.drop('mid_time_stamp', axis=1)


    # 将结果写入文件
    if modifiedZ:
        # 需要修改
        grouped.to_csv('UserUseSituationWithClassZOnlyTime.csv', index=True)
    else:
        # 不需要修改
        grouped.to_csv('UserUseSituationOnlyTime.csv', index=True)

multi_processor_do_preprocessingOnlyForTime()