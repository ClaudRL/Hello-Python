# Exercise
# Simulating sales deals
# Assume that Amir usually works on 3 deals per week, and overall, he wins 30% of deals he works on. Each deal has a binary outcome: it's either lost, or won, so you can model his sales deals with a binomial distribution. In this exercise, you'll help Amir simulate a year's worth of his deals so he can better understand his performance.

# numpy is imported as np.

# 1. Import binom from scipy.stats and set the random seed to 10.
# Import binom from scipy.stats
from scipy.stats import binom

# Set random seed to 10
np.random.seed(10)

# 2. Simulate 1 deal worked on by Amir, who wins 30% of the deals he works on.

# Import binom from scipy.stats
from scipy.stats import binom

# Set random seed to 10
np.random.seed(10)

# Simulate a single deal
print(binom.rvs(1, 0.3, size=1))


# 3. Simulate a typical week of Amir's deals, or one week of 3 deals.
# Import binom from scipy.stats
from scipy.stats import binom

# Set random seed to 10
np.random.seed(10)

# Simulate 1 week of 3 deals
print(binom.rvs(3,0.3,size = 1))

# 4. Simulate a year's worth of Amir's deals, or 52 weeks of 3 deals each, and store in deals.
# Print the mean number of deals he won per week.

# Import binom from scipy.stats
from scipy.stats import binom

# Set random seed to 10
np.random.seed(10)

# Simulate 52 weeks of 3 deals
deals = binom.rvs(3,0.3, size = 52)

# Print mean deals won per week
print(deals.mean())

这个代码使用了 **二项分布（Binomial Distribution）** 来模拟一年中 Amir 每周签单的情况，假设他每周有 3 个签单机会，成功率为 30%。

### 二项分布（Binom）的核心概念：
- **n**: 重复试验的次数（每周 3 次签单机会）。
- **p**: 单次试验成功的概率（每次签单的成功率为 30%）。
- **size**: 重复多少次模拟（52 周，每周重复一次实验）。

在这个模拟中，`binom.rvs(3, 0.3, size=52)` 表示：
- 每周 Amir 有 3 个签单机会（即 `n=3`）。
- 每个签单的成功概率是 0.3（即 `p=0.3`）。
- 我们要模拟 52 周的数据（即 `size=52`）。

### 步骤解释：
1. **设置随机种子**：
   - `np.random.seed(10)`：保证每次运行代码时，生成的随机数序列相同，这样你可以得到相同的模拟结果。

2. **模拟 52 周的签单情况**：
   - `binom.rvs(3, 0.3, size=52)`：为每一周生成 3 个签单的模拟结果，模拟一年（52 周）的签单数据。
   - 返回的 `deals` 是一个数组，表示 52 周中每周签单成功的数量（值在 0 到 3 之间）。

3. **计算每周的平均签单成功数**：
   - `deals.mean()`：计算 52 周中每周的平均签单成功数。

### 归纳总结：
- **二项分布** 是用来描述一个**固定次数**的实验中，每次实验有**两个可能结果**（如成功或失败），并且每次实验成功的概率相同的情况。这里用来模拟每周 3 个签单中的成功次数。
- 通过设置 `n=3` 和 `p=0.3`，我们模拟了 Amir 每周 3 次签单的情况，模拟了一年共 52 周的数据，并计算了每周平均成功签单的数量。

**输出的 `deals.mean()`** 表示的是 Amir 每周平均成功签单的数量。