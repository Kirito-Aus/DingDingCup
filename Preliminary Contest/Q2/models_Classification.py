from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('Q2_Classify_Input_limit_digits.csv')

# 提取需要的列
selected_columns = ['duration', 'up_and_down_flow', 'count', 'count_day_column', 'flow_pers_avg']
X = df[selected_columns].to_numpy()
selected_columns = ['use_situation']
y = df[selected_columns].to_numpy()

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)


# ---------------- 不同模型 ----------------

# 创建逻辑回归分类器
clf_1 = LogisticRegression()

# 创建决策树分类器
clf_2 = DecisionTreeClassifier()

# 创建SVM分类器
clf_3 = SVC(kernel = 'linear')

# 创建K近邻分类器
clf_4 = KNeighborsClassifier(n_neighbors = 9)

# ---------------- 不同模型 ----------------


# 训练模型
clf_1.fit(X_train, y_train.ravel())
clf_2.fit(X_train, y_train.ravel())
clf_3.fit(X_train, y_train.ravel())
clf_4.fit(X_train, y_train.ravel())

# 预测结果
y_pred_1 = clf_1.predict(X_test)
y_pred_2 = clf_2.predict(X_test)
y_pred_3 = clf_3.predict(X_test)
y_pred_4 = clf_4.predict(X_test)

import numpy as np

y_pred = []
for i in range(len(y_pred_1)):
    count = int(y_pred_1[i]) + int(y_pred_3[i]) + int(y_pred_4[i])
    if count >= 2:
        y_pred.append(True)
    else:
        y_pred.append(False)

accuracy = accuracy_score(y_test, y_pred)

# for i in range(50):
#     print(X_test[i])
#     print(y_test[i])
#     print(y_pred_1[i])
#     print(y_pred_2[i])
#     print(y_pred_3[i])
#     print(y_pred_4[i])
#     print(y_pred[i])
print("Accuracy:", accuracy)

# 将预测结果添加到测试集数据中
df = pd.DataFrame(X_test)
df["true_label"] = y_test
df["pred_label"] = y_pred_1

# 将DataFrame保存到CSV文件中
# df.to_csv("predictions.csv", index = False)
