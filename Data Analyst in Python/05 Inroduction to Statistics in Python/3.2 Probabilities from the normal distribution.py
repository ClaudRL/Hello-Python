# Probabilities from the normal distribution
# Since each deal Amir worked on (both won and lost) was different, each was worth a different amount of money. These values are stored in the amount column of amir_deals and follow a normal distribution with a mean of 5000 dollars and a standard deviation of 2000 dollars. As part of his performance metrics, you want to calculate the probability of Amir closing a deal worth various amounts.

# norm from scipy.stats is imported as well as pandas as pd. The DataFrame amir_deals is loaded.

# 1. What's the probability of Amir closing a deal worth less than $7500?
# Probability of deal < 7500
prob_less_7500 = norm.cdf(7500, 5000, 2000)

print(prob_less_7500)

# 2. What's the probability of Amir closing a deal worth more than $1000?
# Probability of deal > 1000
prob_over_1000 = 1 - norm.cdf(1000, 5000, 2000)

print(prob_over_1000)

# 3. What's the probability of Amir closing a deal worth between $3000 and $7000?
# Probability of deal between 3000 and 7000
prob_3000_to_7000 = norm.cdf(7000, 5000, 2000) -norm.cdf(3000, 5000, 2000)

print(prob_3000_to_7000)


# 4. What amount will 25% of Amir's sales be less than?

# Calculate amount that 25% of deals will be less than
pct_25 = norm.ppf(0.25, 5000, 2000)

print(pct_25)

在这个案例中，使用了 SciPy 库中的 `norm.cdf` 和 `norm.ppf` 函数来计算符合正态分布的概率。以下是对每个步骤的详细解释：

1. **计算小于 $7500 的概率**：  
   使用 `norm.cdf(x, mean, std)` 计算给定值 `x` 以下的概率。
   ```python
   prob_less_7500 = norm.cdf(7500, 5000, 2000)
   ```
   - 这里，`cdf` 表示累积分布函数，返回累积到 `7500` 的概率。

2. **计算超过 $1000 的概率**：  
   使用 `1 - norm.cdf(x, mean, std)` 得到大于某一值的概率。
   ```python
   prob_over_1000 = 1 - norm.cdf(1000, 5000, 2000)
   ```
   - 这里，用 `1 - cdf` 的方式得到比 `1000` 更高的概率。

3. **计算在 $3000 和 $7000 之间的概率**：  
   计算两个值之间的概率可以用 `cdf(上限) - cdf(下限)`。
   ```python
   prob_3000_to_7000 = norm.cdf(7000, 5000, 2000) - norm.cdf(3000, 5000, 2000)
   ```

4. **计算位于前 25% 的销售额**：  
   使用 `ppf` 函数找到前 25% 销售额的临界值。`ppf` 是累积分布函数的逆运算，即给定概率求出对应的值。
   ```python
   pct_25 = norm.ppf(0.25, 5000, 2000)
   ```

**总结**：
- `norm.cdf(x, mean, std)`：计算小于 `x` 的概率。
- `1 - norm.cdf(x, mean, std)`：计算大于 `x` 的概率。
- `cdf(上限) - cdf(下限)`：计算在两个值之间的概率。
- `norm.ppf(p, mean, std)`：给定百分位，找到该百分位对应的值（逆向累积分布函数）。

这种方法非常适合用于分析遵循正态分布的连续数据，在金融、统计等领域被广泛使用。