# 为每个Class的APP的使用创建一个文件
import pandas as pd

# 数据读入
print('开始读入数据')
# 1）首先读入用户前15天使用情况表
print('1）开始读入用户前15天使用情况统计表')
first_15day_df = pd.read_csv('./Results/first_15day_app_use_prepared_data_cleaned.csv')

# 2）读入用户后15天使用APP情况统计表
print('2）开始读入用户后15天使用App情况统计表')
last_15day_df = pd.read_csv('./Results/last_15day_app_use_situation.csv')
last_15day_df = last_15day_df.set_index('uid')
print('开始为每个类型APP创建一张表')
# 开始为每个类型的App创建一张表
for num in range(1, 21):
    print(f'开始创建APP = {num}')
    # 分别为每个类型产生一个表
    # 遍历表1的每一行
    each_day_df = first_15day_df
    each_day_df['used_class'] = False
    # print('开始遍历每一行')
    # for idx, row in each_day_df.iterrows():
    #     uid_value = row['uid']
    #
    #     # 检查条件：A值在表2中存在，且对应行的B值为固定值X
    #     if (uid_value in last_15day_df.index) & (last_15day_df.loc[uid_value, 'class'] == num):
    #         each_day_df.at[idx, 'used_class'] = True

    # 获取满足条件的A值
    matching_values = last_15day_df[last_15day_df['class'] == num].index

    # 将满足条件的行的C列设置为True
    each_day_df.loc[each_day_df['uid'].isin(matching_values), 'used_class'] = True

    print(f'开始写出{num}')
    each_day_df.to_csv(f'./Results/EachClass1/class_{num}.csv', index=False)
