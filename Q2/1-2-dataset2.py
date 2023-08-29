import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error, mean_absolute_error
import xgboost as xgb
import warnings
warnings.filterwarnings("ignore")
from sklearn.decomposition import PCA

for i in range(1, 21):
    print("class_", str(i), "处理中...")
    filename = "first_15days_prepared_and_first_15days_daily_use_time/class_" + str(i) + ".csv"
    train_df = pd.read_csv(filename)

    filename = "last_15days_prepared_and_last_15days_daily_use_time/class_" + str(i) + ".csv"
    test_df = pd.read_csv(filename)

    # 提取特征和标签
    X_train = train_df.drop(['daily_duration_label', 'uid'], axis = 1)
    y_train = train_df['daily_duration_label']

    X_test = test_df.drop(['daily_duration_label', 'uid'], axis = 1)
    y_test = test_df['daily_duration_label']


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
