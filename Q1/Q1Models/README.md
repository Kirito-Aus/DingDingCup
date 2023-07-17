## **（1）KMeans：速度快、稳定直观**

- k_means.py

1）绘制聚类散点图

2）统计每个cluster类别的数量

3）输出cluster标签到kmeans_results.csv文件  

- k_means_SelectK.py：

肘部法选择K值、BIC法选择K值

*注释掉一种方法即可跑另一种

Best K=5

- k_means_UserPortrait.py：

对每一个用户，相同的cluster进行分组计算count的总和，以最大的总和对应的标签作为该用户的标签

1）k_means_output1.csv：分组计算count的总和

2）k_means_output2.csv：对于同一用户，每一个cluster只保留一条数据

3）k_means_output3.csv：对于同一用户，保留count总和最大的一组数据（即只有一个cluster作为该用户的标签）

*注：如果运行所有35w数据，需要的时间会略有一点长

## **（2）GMM：**

- GMM.py：
同KMeans

输出在GMM_results.csv文件

- GMM_SelectK.py：

肘部法选择K值、BIC法选择K值

Best K=4

- GMM_UserPortrait.py：

同KMeans

## **（3）DBSCAN：**

- DBSCAN .py：

同KMeans

输出在DBSCAN _results.csv文件

- DBSCAN _SelectK.py：

肘部法选择K值、可视化方法选择K值

Best eps: 0.1, Best min_samples: 9

- DBSCAN _UserPortrait.py：

同KMeans

## **！！一些问题：**

*输出都在Results文件夹中，但有一些文件过大无法上传*

1、几种模型的分类结果不一致，结果存储在XXX_output3.csv中

2、DBSCAN电脑运存不够可能跑不起来，代码中先选了1w数据跑

3、DBSCAN的自动调参结果是0.1和9，这个跑出来抽象的很，人眼调参结果0.001会更好一些



