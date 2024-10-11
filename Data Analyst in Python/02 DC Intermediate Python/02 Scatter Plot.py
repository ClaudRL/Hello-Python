# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()

# 代码解释
# plt.scatter(gdp_cap, life_exp)：

# 该行使用 Matplotlib 的 scatter() 函数来创建一个散点图。
# gdp_cap 是 x 轴的数据，表示人均国内生产总值 (GDP per capita)。
# life_exp 是 y 轴的数据，表示预期寿命 (Life Expectancy)。
# 散点图用于表示数据集中每个观测点的 gdp_cap 和 life_exp 的关系。
# plt.xscale('log')：

# 该行将 x 轴的刻度设置为对数刻度。
# 对数刻度用于可视化数据范围较大或包含指数增长的数据。例如，GDP per capita 数据可能有较大的差异，因此使用对数刻度可以更清晰地展示低值和高值之间的差异。
# plt.show()：

# 该行用于显示生成的图表。
# 当 plt.show() 被调用时，所有之前的绘图命令（如 plt.scatter()）就会被渲染并显示出来。
# 总结
# 散点图用于查看两个变量（gdp_cap 和 life_exp）之间的关系，每个点表示一个国家或地区的 GDP 和预期寿命。
# 使用对数刻度可以更好地查看 GDP 数据的差异，尤其是当数据差异较大时。
# 最终图表的展示提供了对 GDP 与预期寿命之间关系的直观理解，可以帮助发现任何模式或趋势，比如经济发展程度和寿命之间的相关性。