import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings("ignore")
from sklearn.decomposition import PCA

for i in range(1, 21):
    print("class_", str(i), "处理中...")
    filename = "first_15days_prepared_and_first_15days_use_situation/class_" + str(i) + ".csv"
    train_df = pd.read_csv(filename)
    train_df['is_used_app_label'] = train_df['is_used_app_label'].apply(lambda x: 0 if x != 1 else 1)

    filename = "last_15days_prepared_and_last_15days_use_situation/class_" + str(i) + ".csv"
    test_df = pd.read_csv(filename)
    test_df['is_used_app_label'] = test_df['is_used_app_label'].apply(lambda x: 0 if x != 1 else 1)

    # 提取特征和标签
    X_train = train_df.drop(['is_used_app_label', 'uid'], axis = 1)
    y_train = train_df['is_used_app_label']

    X_test = test_df.drop(['is_used_app_label', 'uid'], axis = 1)
    y_test = test_df['is_used_app_label']


    # [1] 决策树模型
    dt_model = DecisionTreeClassifier(random_state = 42)
    dt_model.fit(X_train, y_train)
    dt_y_pred = dt_model.predict(X_test)
    dt_accuracy = accuracy_score(y_test, dt_y_pred)
    print('DecisionTree Accuracy: ', dt_accuracy)

    # [2] 随机森林模型
    rf_model = RandomForestClassifier(n_estimators = 100, random_state = 42)
    rf_model.fit(X_train, y_train)
    rf_y_pred = rf_model.predict(X_test)
    rf_accuracy = accuracy_score(y_test, rf_y_pred)
    print('RandomForest Accuracy: ', rf_accuracy)

    # [3] 支持向量机模型
    svc_model = SVC(kernel='linear')
    svc_model.fit(X_train, y_train)
    svc_y_pred = svc_model.predict(X_test)
    svc_accuracy = accuracy_score(y_test, svc_y_pred)
    print('SVC Accuracy: ', svc_accuracy)

    # [4] 逻辑回归分类器
    lr_model = LogisticRegression()
    lr_model.fit(X_train, y_train)
    lr_y_pred = lr_model.predict(X_test)
    lr_accuracy = accuracy_score(y_test, lr_y_pred)
    print('LogisticRegression Accuracy: ', lr_accuracy)

    # [5] K近邻分类器
    kn_model = KNeighborsClassifier(n_neighbors = 9)
    kn_model.fit(X_train, y_train)
    kn_y_pred = kn_model.predict(X_test)
    kn_accuracy = accuracy_score(y_test, kn_y_pred)
    print('KNeighbors Accuracy: ', kn_accuracy)