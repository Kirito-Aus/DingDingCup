from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np

# 读取 CSV 文件
df = pd.read_csv('Q2_Regression_Input_Normalized.csv')

# 提取需要的列
selected_columns = ['duration', 'up_and_down_flow', 'count', 'count_day_column', 'flow_pers_avg']
X = df[selected_columns].to_numpy()
selected_columns = ['duration_everyday']
y = df[selected_columns].to_numpy()

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)


# ---------------- 线性回归模型 ----------------

# 创建线性回归模型
lr = LinearRegression()

# ---------------- 线性回归模型 ----------------

# 训练模型
lr.fit(X_train, y_train.ravel())

# 预测结果
y_pred = lr.predict(X_test)

# 计算准确率
nmse = mean_squared_error(y_test, y_pred) / np.var(y_test)

print("NMSE:", nmse)

# 将预测结果添加到测试集数据中
df = pd.DataFrame(X_test)
df["true_label"] = y_test
df["pred_label"] = y_pred

# 将DataFrame保存到CSV文件中
df.to_csv("Regression_predictions.csv", index = False)
