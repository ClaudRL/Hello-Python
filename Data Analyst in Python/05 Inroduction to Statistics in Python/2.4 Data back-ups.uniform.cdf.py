# Exercise
# Data back-ups
# The sales software used at your company is set to automatically back itself up, but no one knows exactly what time the back-ups happen. It is known, however, that back-ups happen exactly every 30 minutes. Amir comes back from sales meetings at random times to update the data on the client he just met with. He wants to know how long he'll have to wait for his newly-entered data to get backed up. Use your new knowledge of continuous uniform distributions to model this situation and answer Amir's questions.

# 1. To model how long Amir will wait for a back-up using a continuous uniform distribution, save his lowest possible wait time as min_time and his longest possible wait time as max_time. Remember that back-ups happen every 30 minutes.
# Min and max wait times for back-up that happens every 30 min
min_time = 0
max_time = 30

# 2.  Min and max wait times for back-up that happens every 30 min
# Min and max wait times for back-up that happens every 30 min
min_time = 0
max_time = 30

# Import uniform from scipy.stats
from scipy.stats import uniform

# Calculate probability of waiting less than 5 mins
prob_less_than_5 = uniform.cdf(5,min_time,max_time)
print(prob_less_than_5)


# 3. Calculate the probability that Amir has to wait more than 5 minutes, and store in a variable called prob_greater_than_5.
# Min and max wait times for back-up that happens every 30 min
min_time = 0
max_time = 30

# Import uniform from scipy.stats
from scipy.stats import uniform

# Calculate probability of waiting more than 5 mins
prob_greater_than_5 = 1 - uniform.cdf(5, min_time, max_time - min_time)
print(prob_greater_than_5)

# 4. Calculate the probability that Amir has to wait between 10 and 20 minutes, and store in a variable called prob_between_10_and_20.
# Min and max wait times for back-up that happens every 30 min
min_time = 0
max_time = 30

# Import uniform from scipy.stats
from scipy.stats import uniform

# Calculate probability of waiting 10-20 mins
prob_between_10_and_20 = uniform.cdf(20, min_time, max_time - min_time) - uniform.cdf(10, min_time, max_time - min_time)
print(prob_between_10_and_20)


`uniform.cdf` 是 SciPy 中的一个函数，用于计算均匀分布的累积分布函数（CDF，Cumulative Distribution Function）。均匀分布是一种概率分布，在指定的区间内，每个值出现的概率是相等的。

`uniform.cdf` 返回的值表示在给定范围内，随机变量取值小于等于某个特定值的概率。

### 语法：
```python
scipy.stats.uniform.cdf(x, loc=0, scale=1)
```

### 参数解释：
- `x`：要计算的点，表示随机变量的某个值。
- `loc`：均匀分布的最小值（区间的左端点），即分布的起始位置（默认为 0）。
- `scale`：均匀分布的范围长度，即最大值和最小值之差（默认为 1）。

### 公式：
在区间 `[loc, loc + scale]` 内，CDF 的计算方式为：
\[ F(x) = \frac{x - loc}{scale} \]

当 `x < loc` 时，CDF 的值为 0；
当 `x > loc + scale` 时，CDF 的值为 1。

### 示例：
假设我们有一个均匀分布的随机变量，值的范围是 0 到 30，那么要计算小于等于 10 的概率：
```python
from scipy.stats import uniform

# 区间 [0, 30]，求小于等于 10 的概率
prob = uniform.cdf(10, loc=0, scale=30)
print(prob)  # 输出：0.3333
```

### 解释：
- 这个例子中，均匀分布在区间 [0, 30] 上。
- `uniform.cdf(10, loc=0, scale=30)` 表示计算从 0 到 10 的概率，结果是 0.3333，表示有 33.33% 的概率随机变量的值小于等于 10。

`uniform.cdf` 适用于计算均匀分布区间内任意值的累积概率。