from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('Q2_Classify_Input_Normalized.csv')

# 提取需要的列
selected_columns = ['duration', 'up_and_down_flow', 'count', 'count_day_column', 'flow_pers_avg']
X = df[selected_columns].to_numpy()
selected_columns = ['use_situation']
y = df[selected_columns].to_numpy()

# 将数据集划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 选择 k 值
k_values = range(1, 11)
scores = []
for k in k_values:
    # 创建 k 近邻分类器
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    # 在测试集上计算准确率
    score = knn.score(X_test, y_test)
    scores.append(score)

# 可视化不同 k 值的准确率
import matplotlib.pyplot as plt
plt.plot(k_values, scores)
plt.xlabel('Value of k for KNN')
plt.ylabel('Testing Accuracy')
plt.show()