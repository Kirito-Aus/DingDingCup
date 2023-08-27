from sklearn.linear_model import LogisticRegression
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
test_size_values = [0.2, 0.25, 0.3, 0.35, 0.4]
accuracys = []
for test_size in test_size_values:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size, random_state = 42)

    # 创建逻辑回归分类器
    clf = LogisticRegression()

    # 训练模型
    clf.fit(X_train, y_train.ravel())

    # 预测结果
    y_pred = clf.predict(X_test)

    # 计算准确率
    accuracy = accuracy_score(y_test, y_pred)
    print("Test size:", test_size, "Accuracy:", accuracy)
    accuracys.append(accuracy)

# 可视化不同 k 值的准确率
import matplotlib.pyplot as plt
plt.plot(test_size_values, accuracys)
plt.xlabel('test_size')
plt.ylabel('Testing Accuracy')
plt.show()