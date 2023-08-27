# models_Classification.py 三个模型联合结果，好像结果也没有更好

分类问题的模型：决策树、支持向量机、逻辑回归、K近邻

决策树：models_Classification_DecisionTree.py

支持向量机：models_Classification_SVM.py

逻辑回归：models_Classification_LogisticRegression.py

K近邻：models_Classification_KNN.py


## 1）特征选择过程

选择'duration', 'up_and_down_flow', 'count', 'count_day_column', 'flow_pers_avg'组合的准确度最高

以逻辑回归，random=42为例

1) 'duration', 'up_and_down_flow', 'count', 'count_day_column', 'flow_pers_avg'

Accuracy: 0.7713052858683926

2) 'duration', 'up_and_down_flow', 'count', 'count_day_column'

Accuracy: 0.7709970719679458

3) 'up_and_down_flow', 'count', 'count_day_column'

Accuracy: 0.7708429650177223

4) 'duration', 'count', 'count_day_column'

Accuracy: 0.7705347511172754

5) 'up_and_down_flow', 'count', 'count_day_column', 'flow_pers_avg'
Accuracy: 0.7689936816150409

6) 'duration', 'count', 'count_day_column', 'flow_pers_avg'

Accuracy: 0.7689936816150409

7) 'duration', 'up_and_down_flow', 'count_day_column', 'flow_pers_avg'

Accuracy: 0.7614424410540915

8) 'duration', 'up_and_down_flow', 'count_day_column'

Accuracy: 0.7614424410540915

9) 'duration', 'up_and_down_flow', 'count'

Accuracy: 0.7418708583757128

10) 'duration', 'up_and_down_flow', 'count', 'flow_pers_avg'

Accuracy: 0.7415626444752659

## 2）模型选择结果

以'duration', 'up_and_down_flow', 'count', 'count_day_column', 'flow_pers_avg'，random=42为例

**逻辑回归** *准确度最高*

Accuracy: 0.7713052858683926

**SVM**

Accuracy: 0.7418708583757128

采用不同核函数结果相同

原因总结：数据集中的类别之间具有高度线性可分性时，使用不同的核函数可能不会显著改变分类结果；

如果数据集非常小或者噪声很大，使用不同的核函数也可能会得到相似的分类结果

**决策树**

Accuracy: 0.6920943134535368

**K近邻**

Accuracy: 0.746031746031746

## 3）测试集训练集划分系数 models_Classification_LogisticRegression_SelectTestsize.py

以逻辑回归为例，0.3为最佳

## 4）KNN的K值选择 models_Classification_KNN_SelectK.py
K=9为最佳


# models_Regression.py
回归问题的模型：
线性回归、支持向量机、决策树、随机森林、神经网络
