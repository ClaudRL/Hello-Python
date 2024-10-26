# Exercise
# Simulating sales under new market conditions
# The company's financial analyst is predicting that next quarter, the worth of each sale will increase by 20% and the volatility, or standard deviation, of each sale's worth will increase by 30%. To see what Amir's sales might look like next quarter under these new market conditions, you'll simulate new sales amounts using the normal distribution and store these in the new_sales DataFrame, which has already been created for you.

# In addition, norm from scipy.stats, pandas as pd, and matplotlib.pyplot as plt are loaded.
# Currently, Amir's average sale amount is $5000. Calculate what his new average amount will be if it increases by 20% and store this in new_mean.
# Amir's current standard deviation is $2000. Calculate what his new standard deviation will be if it increases by 30% and store this in new_sd.
# Create a variable called new_sales, which contains 36 simulated amounts from a normal distribution with a mean of new_mean and a standard deviation of new_sd.
# Plot the distribution of the new_sales amounts using a histogram and show the plot.

# Calculate new average amount
new_mean = 5000*1.20

# Calculate new standard deviation
new_sd = 2000*1.30

# Simulate 36 new sales
new_sales = norm.rvs(new_mean, new_sd, size = 36)

# Create histogram and show
plt.hist(new_sales)
plt.show()

在这个练习中，Amir 的销售额按预测会增加平均值和波动性，借此可以模拟他在新市场条件下的销售情况。这里使用了正态分布和随机数生成的基础知识，步骤如下：

1. **计算新的平均销售额（`new_mean`）**：
   - 现有平均值为 5000 美元，在新条件下预计增加 20%，因此：
     ```python
     new_mean = 5000 * 1.20
     ```
   - 得到新的平均值 `new_mean = 6000`。

2. **计算新的标准差（`new_sd`）**：
   - 当前标准差为 2000 美元，在新市场条件下标准差预计增加 30%：
     ```python
     new_sd = 2000 * 1.30
     ```
   - 得到新的标准差 `new_sd = 2600`。

3. **模拟新的销售额数据**：
   - 使用 `norm.rvs(mean, std, size=n)` 生成正态分布随机数，模拟新的 36 个销售额数据：
     ```python
     new_sales = norm.rvs(new_mean, new_sd, size=36)
     ```

4. **绘制新销售额的分布图**：
   - 用 `plt.hist(new_sales)` 将模拟的数据绘制成直方图，展示其分布情况。

**总结**：
- 使用正态分布模拟数据时，可以通过调整 `mean` 和 `std` 来反映预测中的变化。
- `norm.rvs` 用于生成指定数量（`size`）的模拟数据，用于未来销售趋势的预测分析。
