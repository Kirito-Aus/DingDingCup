import string

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

path = 'C:/Users/N33/Desktop/钉钉杯/2023年第二届钉钉杯大学生大数据挑战赛初赛题目/A题/初赛数据集'

def feature_engineering(df):

    print('添加class列，并转换为数字')
    # 特征工程，添加APP类型列，将APP的类型转换成数字，便于后续分析
    letter_to_number = {letter: i + 1 for i, letter in enumerate(string.ascii_lowercase)}
    # 对文档中的字母进行替换
    app_class_df = pd.read_csv(path + '/app_class.csv')
    app_class_df.columns = ['appid', 'class']
    app_class_df['class'] = app_class_df['class'].map(letter_to_number)
    app_class_dict = dict(zip(app_class_df['appid'], app_class_df['class']))
    # 生成分类列
    df['class'] = df['appid'].map(app_class_dict)
    app_class_dict = None
    app_class_df = None

    print('开始进行datetime类型的转换')
    df['start_time'] = pd.to_datetime(df['start_time'])
    df['end_time'] = pd.to_datetime(df['end_time'])

    print('生成一些新的特征，以用户视角进行统计')
    # 生成一些新的特征，以用户视角进行统计
    # 1）计算出用户每次使用APP的情况
    print('1）计算出用户每次使用APP的情况')
    user_use_df = df.groupby('uid').agg(
        {'duration': ['sum', 'mean'],
         'start_time': 'mean',
         'end_time': 'mean',
         'up_flow': ['sum', 'mean'],
         'down_flow': ['sum', 'mean'],
         'up_and_down_flow': ['sum', 'mean'],
         'appid': 'nunique',
         'class': 'nunique'
         }
    )
    user_use_df.columns = ['total_duration', 'avg_duration', 'avg_start_time', 'avg_end_time', 'total_up_flow',
                           'avg_up_flow', 'total_down_flow', 'avg_down_flow', 'total_up_and_down_flow',
                           'avg_up_and_down_flow', 'used_app_num', 'used_app_type']
    # user_use_df.to_csv('./Results/Middle/user_use_df.csv')
    # user_use_df = None

    # 2）计算出用户每天使用APP的情况
    print('2）计算出用户每天使用APP的情况')
    # 每日平均：先求出每日的总使用时长等
    user_daily_use_df = df.groupby(['uid', 'end_day']).agg(
        {
            'duration': 'sum',
            'up_flow': 'sum',
            'down_flow': 'sum',
            'up_and_down_flow': 'sum',
            'appid': 'nunique',
            'app_type': 'nunique'
        }
    )
    # 在统计完每天的数据后求每日的平均值
    user_daily_use_df = user_daily_use_df.groupby('uid').agg(
        {
            'duration': 'mean',
            'up_flow': 'mean',
            'down_flow': 'mean',
            'up_and_down_flow': 'mean',
            'appid': 'mean',
            'app_type': 'mean',
        }
    )
    user_daily_use_df.columns = ['daily_total_duration', 'daily_total_up_flow', 'daily_total_down_flow',
                                 'daily_total_up_and_down_flow', 'daily_used_app_mum', 'daily_used_app_type']
    # user_daily_use_df.to_csv('./Results/Middle/user_daily_use_df.csv')
    # user_daily_use_df = None

    # 3）计算出用户使用每个APP的平均使用情况，使用跨度、使用总天数等
    print('3）计算出用户使用每个APP的平均使用情况，使用跨度、使用总天数等')
    user_app_use_df = df.groupby(['uid', 'appid'])['end_day'].nunique()
    user_app_use_df = user_app_use_df.groupby('uid').agg({
        'min', 'max', 'mean'
    })
    user_app_use_df.columns = ['min_app_use_daytime', 'max_app_use_day_time', 'avg_app_use_daytime']
    # user_app_use_df.to_csv('./Results/Middle/user_app_use_df.csv')
    # user_app_use_df = None

    df = None

    # 将数据进行聚合
    print('开始进行数据的聚合')
    user_use_agg_df = pd.merge(user_use_df, user_daily_use_df, on='uid', how='inner')
    user_use_agg_df = pd.merge(user_use_agg_df, user_app_use_df, on='uid', how='inner')

    # 对聚合后的数据删除有空值的行
    print('对聚合后的数据删除有空值的行')
    user_use_agg_df = user_use_agg_df.dropna()
    return user_use_agg_df

def get_first_15day_app_use_situation():
    # 用户前15天使用情况
    print('开始读入Clean过后的数据')
    df = pd.read_csv('Results/Middle/first_15day_app_use_statistics.csv')
    print('开始进入特征工程处理')
    user_use_agg_df = feature_engineering(df)
    user_use_agg_df.to_csv('./Results/first_15day_app_use_prepared_data.csv')

def add_normalization_pca():
    print('开始读入特征工程结束的数据，进一步处理')
    df = pd.read_csv('./Results/first_15day_app_use_prepared_data.csv')

    print('开始进行datetime类型的转换')
    df['avg_start_time'] = pd.to_datetime(df['avg_start_time'])
    df['avg_end_time'] = pd.to_datetime(df['avg_end_time'])
    # 将datetime类型转换为时间戳（包含秒）
    df['avg_start_time'] = df['avg_start_time'].apply(lambda x: x.timestamp())
    df['avg_end_time'] = df['avg_end_time'].apply(lambda x: x.timestamp())

    # 进行归一化
    # 需要排除的列
    excluded_columns = ['uid', 'appid']

    # 创建MinMaxScaler对象
    scaler = MinMaxScaler()

    # 提取需要归一化的列并进行归一化
    columns_to_normalize = [col for col in df.columns if col not in excluded_columns]
    df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])
    df.to_csv('./Results/first_15day_app_use_prepared_data_cleaned.csv')

    # 进行PCA降维
    # pca = PCA(n_components=10)
    # trainingData = pca.fit_transform(weight)


add_normalization_pca()