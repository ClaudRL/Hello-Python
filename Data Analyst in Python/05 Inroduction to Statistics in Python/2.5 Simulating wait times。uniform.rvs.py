# Exercise
# Simulating wait times
# To give Amir a better idea of how long he'll have to wait, you'll simulate Amir waiting 1000 times and create a histogram to show him what he should expect. Recall from the last exercise that his minimum wait time is 0 minutes and his maximum wait time is 30 minutes.

# As usual, pandas as pd, numpy as np, and matplotlib.pyplot as plt are loaded.

# 1. Set the random seed to 334.
# Set random seed to 334
np.random.seed(334)

# 2. Import uniform from scipy.stats.
# Set random seed to 334
np.random.seed(334)

# Import uniform
from scipy.stats import uniform


# 3. Generate 1000 wait times from the continuous uniform distribution that models Amir's wait time. Save this as wait_times.
# Set random seed to 334
np.random.seed(334)

# Import uniform
from scipy.stats import uniform

# Generate 1000 wait times between 0 and 30 mins
wait_times = uniform.rvs(0, 30, size = 1000)

print(wait_times)

# 4. Create a histogram of the simulated wait times and show the plot.
# Set random seed to 334
np.random.seed(334)

# Import uniform
from scipy.stats import uniform

# Generate 1000 wait times between 0 and 30 mins
wait_times = uniform.rvs(0, 30, size=1000)

# Create a histogram of simulated times and show plot
plt.hist(wait_times)
plt.show()


在使用 `plt.hist()` 创建直方图时，应该直接传递数据变量，而不是将变量放在列表中。具体来说，`plt.hist(wait_times)` 是正确的调用方式。下面是修正后的代码：

```python
# Set random seed to 334
np.random.seed(334)

# Import uniform
from scipy.stats import uniform

# Generate 1000 wait times between 0 and 30 mins
wait_times = uniform.rvs(0, 30, size=1000)

# Create a histogram of simulated times and show plot
plt.hist(wait_times, bins=30, edgecolor='black')  # Added bins and edgecolor for clarity
plt.xlabel('Wait Time (minutes)')
plt.ylabel('Frequency')
plt.title('Histogram of Simulated Wait Times')
plt.show()
```

### 修改说明：
1. **`wait_times`** 直接传递给 `plt.hist()`。
2. **`bins=30`** 指定将数据分成 30 个区间，能使直方图更加细致。
3. **`edgecolor='black'`** 给每个条形边缘加上黑色边框，让直方图更清晰。
4. 添加了 **x轴**、**y轴** 和 **标题** 来更好地解释图表。