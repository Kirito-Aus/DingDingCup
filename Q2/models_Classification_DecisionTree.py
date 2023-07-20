from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('Q2_Classify_Input_Normalized.csv')

# 提取需要的列
selected_columns = ['duration', 'up_and_down_flow', 'count', 'count_day_column', 'flow_pers_avg']
X = df[selected_columns].to_numpy()
selected_columns = ['use_situation']
y = df[selected_columns].to_numpy()

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)


# ---------------- 决策树模型 ----------------

# 创建决策树分类器
clf = DecisionTreeClassifier()

# ---------------- 决策树模型 ----------------

# 训练模型
clf.fit(X_train, y_train.ravel())

# 预测结果
y_pred = clf.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
# for i in range(50):
#     print(X_test[i])
#     print(y_test[i])
#     print(y_pred[i])
print("Accuracy:", accuracy)

# 将预测结果添加到测试集数据中
df = pd.DataFrame(X_test)
df["true_label"] = y_test
df["pred_label"] = y_pred

# 将DataFrame保存到CSV文件中
df.to_csv("predictions.csv", index = False)
