import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore")

# 读取 CSV 文件
df = pd.read_csv('class_1.csv')

# 提取需要的列
X = df.iloc[:, 2:-2].to_numpy()
# selected_columns = ['total_duration', 'avg_start_time', 'avg_end_time', 'total_up_and_down_flow', 'used_app_num', 'avg_app_use_daytime']
# X = df[selected_columns].to_numpy()
selected_columns = ['used_class']
y = df[selected_columns].to_numpy()

# PCA降维
k = 4        # [！2-10选取最适合的维度]
pca = PCA(n_components = k)  # 指定降维后的维度
X = pca.fit_transform(X)

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

# [！其他的模型试试]
# [1] 训练决策树模型
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)
dt_y_pred = dt_model.predict(X_test)
dt_accuracy = accuracy_score(y_test, dt_y_pred)
print('决策树模型的准确率：', dt_accuracy)


# [2] 训练随机森林模型
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_y_pred = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_y_pred)
print('随机森林模型的准确率：', rf_accuracy)

# [3] 训练支持向量机模型
svc_model = SVC(kernel = 'linear')  # [！不同的kernel]
svc_model.fit(X_train, y_train)
svc_y_pred = svc_model.predict(X_test)
svc_accuracy = accuracy_score(y_test, svc_y_pred)
print('支持向量机模型的准确率：', svc_accuracy)
