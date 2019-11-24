# coding = utf-8
from matplotlib import pyplot as plt

# 创建一组整数列表x，以2开始，2为步长，小于10
x = range(2, 10, 2)
y = [11, 12, 15.8, 14.7]

# 实例化并保存图形figure
# figsize中两参数分别为图形宽、高
# dpi(dot per inch)影响图片清晰度
fig = plt.figure(figsize=(30, 30), dpi=60)

# 绘图
plt.plot(x, y)

# 保存图片（svg为矢量图，放大不会有锯齿）
plt.savefig('./test.png')

#设置X轴刻度
_xticks_ = [i/2 for i in range(4, 21)]
# 间隔取值
plt.xticks(_xticks_[::3])
#设置Y轴刻度
plt.yticks(range(min(y), max(y) + 1))

# 展示
plt.show()
