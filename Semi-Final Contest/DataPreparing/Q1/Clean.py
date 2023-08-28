# 读入所有的数据后进行数据清洗
import string

import pandas as pd

path = 'C:/Users/N33/Desktop/钉钉杯/2023年第二届钉钉杯大学生大数据挑战赛初赛题目/A题/初赛数据集'


def read_in_data_and_clean():
    # 读入前面15天每天的数据，进行清洗
    dfs = []
    for day in range(1, 16):
        day_str = str(day).zfill(2)
        filename = path + f'\day{day_str}.txt'
        print(f'正在处理{day_str}的数据')
        # 使用header=None表示不用表头
        df_tmp = pd.read_csv(filename, header=None)
        # 拼接每天的数据
        dfs.append(df_tmp)
        df_tmp = None

    print('开始对多日数据进行拼接')
    df = pd.concat(dfs, axis=0)
    dfs = None

    # 对于所有存在缺失的数据进行删除
    print('删除缺失数据')
    df.dropna(how='any', axis=0)
    # 修改df的表头的名称
    df.columns = ['uid', 'appid', 'app_type', 'start_day', 'start_time', 'end_day', 'end_time', 'duration', 'up_flow',
                  'down_flow']

    print('开始处理异常数据')
    # 处理异常数据，如果只打开了就马上关了，认为没有使用
    print('（1）处理异常使用时长')
    df = df[df['duration'] != 0]  # 剔除使用时长为0的行
    df = df[df['duration'] >= 10]

    print('（2）开始异常处理流量')
    # 判断使用流量，如果上下行流量为0，则认为没有使用
    # 对于上下行流量为0的，则可能是一些系统工具，认为对用户的使用没有影响
    df['up_and_down_flow'] = df['up_flow'] + df['down_flow']
    df = df[df['up_and_down_flow'] != 0]

    # 数据处理
    print('开始进行类型转换')
    print('（1）开始进行时间类型的转化')
    df['start_time'] = pd.to_datetime(df['start_time'])  # 转换为datetime类型
    df['end_time'] = pd.to_datetime(df['end_time'])  # 转换为datetime类型
    print('（2）开始进行流量转化')
    df['up_flow_mb'] = df['up_flow'] / 1024 / 1024  # 上行流量（MB）
    df['down_flow_mb'] = df['down_flow'] / 1024 / 1024  # 下行流量（MB）

    return df





#
# # 使用用户前面用每种APP的使用数据来预测是否使用了A类APP
df = read_in_data_and_clean()
df.to_csv('./Results/Middle/first_15day_app_use_statistics.csv')
