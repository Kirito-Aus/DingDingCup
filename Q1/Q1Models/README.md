（1）KMeans：
· k_means.py
1）绘制聚类散点图
2）统计每个cluster类别的数量
3）输出cluster标签到kmeans_results.csv文件

· k_means_SelectK.py：
肘部法选择K值、BIC法选择K值
*注释掉一种方法即可跑另一种
K=5效果最好

· k_means_UserPortrait.py：
对每一个用户，相同的cluster进行分组计算count的总和，以最大的总和对应的标签作为该用户的标签
1）output1.csv：分组计算count的总和
2）output2.csv：对于同一用户，每一个cluster只保留一条数据
3）output3.csv：对于同一用户，保留count总和最大的一组数据（即只有一个cluster作为该用户的标签）
*注：如果运行所有35w数据，需要的时间会略有一点长

（2）GMM：
· GMM.py：
同KMeans
输出在GMM_results.csv文件

· GMM_SelectK.py：
肘部法选择K值、BIC法选择K值
K=4效果最好

· GMM_UserPortrait.py：
同KMeans

（3）DBSCAN：
· DBSCAN .py：
同KMeans
输出在DBSCAN _results.csv文件

· DBSCAN _SelectK.py：
肘部法选择K值、可视化方法选择K值
Best eps: 0.1, Best min_samples: 9

· DBSCAN _UserPortrait.py：
同KMeans



