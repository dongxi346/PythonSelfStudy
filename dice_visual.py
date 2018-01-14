import pygal
import matplotlib.pyplot as plt
from die import Die
from random_walk import RandomWalk

# 创建两个D6骰子
# die_1 = Die()
# die_2 = Die()

# 创建两个D8骰子
die_1 = Die(8)
die_2 = Die(8)


# 掷几次骰子，并将结果存储在一个列表中
results = []
# for roll_num in range(1000):
for roll_num in range(100000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

# hist.title = "Results of rolling on D6 1000 times."
# hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '10', '11', '12']
hist.title = "Results of rolling on D8 100000 times."
hist.x_labels = list(range(2, 16))
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8', frequencies)
# hist.add('D6 + D6', frequencies)
# 将图表渲染为一个SVG文件，这种文件的扩展名必须为svg
hist.render_to_file('die_visual.svg')

print(frequencies)

# 创建随机漫步
rw = RandomWalk(10000)
rw.fill_walk()
plt.scatter(rw.x_values,rw.y_values,s=15)
# 因为展示的是随机漫步所以要隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()
