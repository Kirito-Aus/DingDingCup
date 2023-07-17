# 数据预处理部分
## 未进行数据清洗的结果文件
UserUseSituation.csv文件中
- 对于无app_class的应用没有统计在内，直接删除
- 每个用户有若干行，每一行对应一种类型的应用
- 添加了一列总流量，对于duration、上下行流量、总流量、使用次数计数 都是均值-> 是每人每天使用的量的均值

UserUseSituationWithZ.csv文件中
- 与上面的区别是：对于无app_class的应用将其类型全部设为Z，并且进行统计

## 进行了数据清洗和数据预处理的结果数据
### NormalizedAndCleaned
- 在UserUseSituation的基础上进行了数据归一化和数据清洗，利用Turkey箱线图计算异常值的方法去除了异常值，并且将数据归一化到[0,1]的区间

### NormalizedAndCleanedWithZ
- 在UserUseSituationWithZ的基础上进行了数据归一化和数据清洗，利用Turkey箱线图计算异常值的方法去除了异常值，并且将数据归一化到[0,1]的区间
