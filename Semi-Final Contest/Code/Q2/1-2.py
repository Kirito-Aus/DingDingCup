import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error
import xgboost as xgb
import warnings
warnings.filterwarnings("ignore")

for i in range(1, 20):
    filename = "class_" + str(i) + ".csv"
    print(filename, "处理中...")

    # 读取 CSV 文件
    df = pd.read_csv(filename)

    # 提取需要的列
    X = df.iloc[:, 2:-2].to_numpy()
    # selected_columns = ['used_app_num', 'daily_total_duration', 'daily_total_up_and_down_flow', 'min_app_use_daytime', 'max_app_use_day_time', 'avg_app_use_daytime']
    # X = df[selected_columns].to_numpy()
    selected_columns = ['daily_duration']
    y = df[selected_columns].to_numpy()

    # PCA降维
    k = 9
    pca = PCA(n_components = k)  # 指定降维后的维度
    X = pca.fit_transform(X)

    # 划分数据集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

    def MMSE(y_test, y_pred):
        error = y_test - y_pred
        numerator = np.sum(np.square(error))
        denominator = np.sum(np.square(y_test - np.mean(y_test)))
        mmse = np.sqrt(numerator / denominator)
        return mmse

    # [1] XGBoost模型
    xgb_model = xgb.XGBRegressor()
    xgb_model.fit(X_train, y_train)
    xgb_y_pred = xgb_model.predict(X_test)

    # 评价指标
    xgb_mmse = MMSE(y_test, xgb_y_pred)
    xgb_mse = mean_squared_error(y_test, xgb_y_pred)
    xgb_rmse = np.sqrt(xgb_mse)
    xgb_mae = mean_absolute_error(y_test, xgb_y_pred)
    xgb_nmse = mean_squared_error(y_test, xgb_y_pred) / np.var(y_test)
    print("XGBRegressor Accuracy:")
    print("MMSE: {:.2f}, RMSE: {:.2f}, MAE: {:.2f}, NMSE: {:.2f}".format(xgb_mmse, xgb_rmse, xgb_mae, xgb_nmse))


    # [2] 线性回归模型
    lm_model = LinearRegression()
    lm_model.fit(X_train, y_train)
    lm_y_pred = lm_model.predict(X_test)

    # 评价指标
    lm_mmse = MMSE(y_test, lm_y_pred)
    lm_mse = mean_squared_error(y_test, lm_y_pred)
    lm_rmse = np.sqrt(lm_mse)
    lm_mae = mean_absolute_error(y_test, lm_y_pred)
    lm_nmse = mean_squared_error(y_test, lm_y_pred) / np.var(y_test)
    print("LinearRegression Accuracy:")
    print("MMSE: {:.2f}, RMSE: {:.2f}, MAE: {:.2f}, NMSE: {:.2f}".format(lm_mmse, lm_rmse, lm_mae, lm_nmse))


    # [3] 决策树回归模型
    dtr_model = DecisionTreeRegressor()
    dtr_model.fit(X_train, y_train)
    dtr_y_pred = dtr_model.predict(X_test)

    # 评价指标
    dtr_mmse = MMSE(y_test, dtr_y_pred)
    dtr_mse = mean_squared_error(y_test, dtr_y_pred)
    dtr_rmse = np.sqrt(dtr_mse)
    dtr_mae = mean_absolute_error(y_test, dtr_y_pred)
    dtr_nmse = mean_squared_error(y_test, dtr_y_pred) / np.var(y_test)
    print("DecisionTreeRegressor Accuracy:")
    print("MMSE: {:.2f}, RMSE: {:.2f}, MAE: {:.2f}, NMSE: {:.2f}".format(dtr_mmse, dtr_rmse, dtr_mae, dtr_nmse))
