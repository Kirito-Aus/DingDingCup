import pandas as pd
import numpy as np
import time
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# 读取 CSV 文件
df = pd.read_csv('first_15days_prepared_and_last_15days_daily_use_time/class_1.csv')

# 提取需要的列
X = df.iloc[:, 2:-2].to_numpy()
selected_columns = ['daily_duration_label']
y = df[selected_columns].to_numpy()

def MMSE(y_test, y_pred):
    error = y_test - y_pred
    numerator = np.sum(np.square(error))
    denominator = np.sum(np.square(y_test - np.mean(y_test)))
    mmse = np.sqrt(numerator / denominator)
    return mmse

start = time.time()
accuracy = []  # 存放每次结果的误差平方和
k1 = 3
k2 = 15
for k in range(k1, k2):
    pca = PCA(n_components = k)  # 指定降维后的维度
    Xk = pca.fit_transform(X)

    # 划分数据集
    X_train, X_test, y_train, y_test = train_test_split(Xk, y, test_size=0.3, random_state=42)
    lm_model = LinearRegression()
    lm_model.fit(X_train, y_train)
    lm_y_pred = lm_model.predict(X_test)

    # 评价指标
    lm_mmse = MMSE(y_test, lm_y_pred)
    print("LinearRegression Accuracy:")
    print("MMSE: {:.2f}".format(lm_mmse))
    accuracy.append(lm_mmse)

end = time.time()
print(f'Time: {end-start}s')

plt.figure(figsize = (6, 4))
plt.xlabel('k', fontsize = 10)
plt.ylabel('accuracy', fontsize = 10)
plt.plot(range(k1, k2), accuracy, 'o-')
plt.savefig('PCA降维.png', dpi = 300)
plt.show()
