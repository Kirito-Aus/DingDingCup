import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# 读取30天的APP使用情况数据
filtered_user_app_usage_df = pd.read_excel('all_30day_app_use_prepared_data_normalized_part.xls')

# 构建用户-APP矩阵
#app_features = ['avg_up_and_down_flow_each_time', 'avg_duration_each_time']
app_features = 'avg_duration_each_time'
user_app_matrix = filtered_user_app_usage_df.pivot_table(index='uid', columns='appid', values=app_features, aggfunc=np.sum, fill_value=0)

# 计算用户之间的相似性（余弦相似度）
user_sim_matrix = cosine_similarity(user_app_matrix)

# 为每个用户推荐APP
def recommend_apps(user_id, top_n=5):
    user_index = user_app_matrix.index.get_loc(user_id)
#    user_index = np.where(user_app_matrix[:, 0] == user_id)[0]
    user_sim_scores = user_sim_matrix[user_index]
    similar_users_indices = user_sim_scores.argsort()[::-1][1:]  # 排除自身，取相似度最高的用户
    similar_users_scores = user_sim_scores[similar_users_indices]

    # 对相似用户的APP进行加权累加
    app_scores = user_app_matrix.values[similar_users_indices] * similar_users_scores[:, None]
    app_scores = app_scores.sum(axis=0)

    # 获取推荐排名前top_n的APP
    top_app_indices = app_scores.argsort()[::-1][:top_n]
    top_app_ids = user_app_matrix.columns[top_app_indices]

    return top_app_ids.tolist()

# 为用户X推荐APP
filtered_user_app_usage_df = filtered_user_app_usage_df.drop_duplicates(subset=['uid'])
for index, row in filtered_user_app_usage_df.iterrows():
    user_id = row['uid']
    recommended_apps = recommend_apps(user_id)
    print("Recommended Apps for User", user_id, ":", recommended_apps)
