
# 输入数据准备

## Q1分类问题
### Q2_Classify_Input
注意：每人有1-2条数据，分别对应不同的APP_type，但是对于A类来说，Sys的数据非常少，只有1%不到，可以考虑进行处理？
- use_situation为标签：表示12-21Day用户是否使用a类APP
- duration	up_flow	down_flow	up_and_down_flow　表示这个人**每天每次**使用A类APP的平均时间长、上下行流量（一天可能使用若干次）
- count	每人每天使用A类APP的次数
- count_day_column 在1-11天这个人有多少天使用了这个APP
- flow_pers_avg 使用该APP时平均每秒消耗的流量
- mid_time 每次使用过程的中间时刻的平均值


## Q1回归问题
### Q2_Regression_Input
- duration_everyday **平均每日A类总时长（只记录有效的日期，如果没有使用则不记录）**
