  # 数据预处理部分

  UserUseSituation.csv文件中
  - 对于无app_class的应用没有统计在内
  - 每个用户有若干行，每一行对应一种类型的应用

  UserUseSituationWithZ.csv文件中
  - 对于无app_class的应用将其类型全部设为Z，并且进行统计
  - 每个用户有若干行，每一行对应一种类型的应用

  UserUseSituationWithZWithType.csv文件中
  - 对于无app_class的应用将其类型全部设为Z，并且进行统计,且增加一个Type列
  - 每个用户有若干行，每一行对应一种类型的应用
