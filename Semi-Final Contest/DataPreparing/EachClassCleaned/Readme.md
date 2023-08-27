# 一、数据预处理

## 数据清理
1）删除有缺失值的行
2）删除异常使用时长
- 剔除使用时长为0的行
- 处理异常流量，如果上下行流量为0，则认为没有使用，对于上下行流量为0的，则可能是一些系统工具，认为对用户的使用分析没有影响

## 开始进行类型转换
- 开始进行流量转化
- df['up_flow_mb'] = df['up_flow'] / 1024 / 1024  # 上行流量（MB）

# 二、特征工程
生成一些新的特征，以用户视角进行统计
## 1）计算出用户每次使用APP的情况
- 统计用户在每次使用APP的一些情况
- 使用所有APP的总时长、每次使用APP的平均时长
- 每次使用APP的平均开始时长
- ...
- 统计总计使用过的所有APP的总数，使用过的所有class的总类型
```
        {'duration': ['sum', 'mean'],
         'start_time': 'mean',
         'end_time': 'mean',
         'up_flow': ['sum', 'mean'],
         'down_flow': ['sum', 'mean'],
         'up_and_down_flow': ['sum', 'mean'],
         'appid': 'nunique',
         'class': 'nunique'
         }
```

## 2）计算出用户每天使用APP的情况
- 每个人每天使用的总流量、总时长、上下行流量、使用的App的类型，使用的APP的class类型
- 统计每天的均值
```        {
            'duration': 'sum',
            'up_flow': 'sum',
            'down_flow': 'sum',
            'up_and_down_flow': 'sum',
            'appid': 'nunique',
            'app_type': 'nunique'
        }
```

## 3）计算出用户使用每个APP的平均使用情况，使用跨度、使用总天数等
- 计算出用户使用各个APP的使用天数，并找出最大值、最小值、平均值
```
 'min', 'max', 'mean'
```

# 三、归一化
MinMaxScaler
