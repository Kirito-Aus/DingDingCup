#coding：utf8
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# 选择一个支持中文的字体，比如SimSun
plt.rcParams['font.sans-serif'] = ['SimSun']
# 假设你的数据集保存为data.csv文件
data = pd.read_csv('day01.csv')

# 计算属性之间的相关系数矩阵
correlation_matrix = data.corr()

# 绘制关系热力图
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('数据集特征间关系热力图')
plt.savefig('heatmap.png')
plt.show()