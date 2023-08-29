import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings("ignore")
from sklearn.decomposition import PCA

# 读取day01作为训练集
train_df = pd.read_excel('day01_features.xlsx')
train_df['category'] = train_df['category'].apply(lambda x: 0 if x != 1 else x)
print(train_df['category'].value_counts())
# 读取day20作为测试集
test_df = pd.read_excel('day20_features.xlsx')
test_df['category'] = test_df['category'].apply(lambda x: 0 if x != 1 else x)
print(test_df['category'].value_counts())

# 提取特征和标签
X_train = train_df.drop(['category','uid','appid'], axis = 1)
y_train = train_df['category']

X_test = test_df.drop(['category','uid','appid'], axis = 1)
y_test = test_df['category']

pca = PCA(n_components=4)  # 指定降维后的维度
X_train = pca.fit_transform(X_train)
X_test = pca.fit_transform(X_test)

# 训练决策树模型
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)
dt_y_pred = dt_model.predict(X_test)
dt_accuracy = accuracy_score(y_test, dt_y_pred)
print('决策树模型的准确率：', dt_accuracy)