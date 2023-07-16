# 数据预处理部分
## 未进行数据清洗的结果文件
UserUseSituation.csv文件中
- 对于无app_class的应用没有统计在内
- 每个用户有若干行，每一行对应一种类型的应用

UserUseSituationWithZ.csv文件中
- 对于无app_class的应用将其类型全部设为Z，并且进行统计
- 每个用户有若干行，每一行对应一种类型的应用

UserUseSituationWithZWithType.csv文件中 
- 对于无app_class的应用将其类型全部设为Z，并且进行统计,且增加一个Type列
- 每个用户有若干行，每一行对应一种类型的应用

## 进行了数据清洗和数据预处理的结果数据
### NormalizedAndCleaned
- 在UserUseSituationWithZ的基础上进行了数据归一化和数据清洗，利用Turkey箱线图计算异常值的方法去除了异常值，并且将数据归一化到[0,1]的区间

### normalizedAndCleanedAddSumCol
- 多了一个上行流量+下行流量的总和列，并对其进行了归一化和异常值剔除。

注意：这三个文件的行数各不相同，因为加上Z类型的数据挥笔没有Z的多，而每个用户标记为Z的类型有些是用户安装，有些是系统自带的
