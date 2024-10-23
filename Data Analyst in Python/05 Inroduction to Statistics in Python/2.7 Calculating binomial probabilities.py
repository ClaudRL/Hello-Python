# Exercise
# Calculating binomial probabilities
# Just as in the last exercise, assume that Amir wins 30% of deals. He wants to get an idea of how likely he is to close a certain number of deals each week. In this exercise, you'll calculate what the chances are of him closing different numbers of deals using the binomial distribution.

# binom is imported from scipy.stats.

# 1. What's the probability that Amir closes all 3 deals in a week? Save this as prob_3.

# Probability of closing 3 out of 3 deals
prob_3 = binom.pmf(3,3,0.3)

print(prob_3)

# 2 .What's the probability that Amir closes 1 or fewer deals in a week? Save this as prob_less_than_or_equal_1.
# Probability of closing <= 1 deal out of 3 deals
prob_less_than_or_equal_1 = binom.cdf(1,3,0.3)

print(prob_less_than_or_equal_1)


# 3. What's the probability that Amir closes more than 1 deal? Save this as prob_greater_than_1.
# Probability of closing > 1 deal out of 3 deals
prob_greater_than_1 = 1- binom.cdf(1,3,0.3)

print(prob_greater_than_1)

### `binom.pmf` 和 `binom.cdf` 归纳总结：

#### 1. **`binom.pmf(k, n, p)`**
- **含义**：概率质量函数（PMF, Probability Mass Function），用于计算在**一次二项分布实验**中，成功次数**正好为 k** 的概率。
  - `k`：期望成功的次数。
  - `n`：实验的总次数（例如，总签单次数）。
  - `p`：每次实验成功的概率（如每次签单成功的概率）。

**示例**:
```python
prob_3 = binom.pmf(3, 3, 0.3)
```
- 在这个例子中，`binom.pmf(3, 3, 0.3)` 表示：在 3 次签单尝试中，正好签 3 单（即全部成功）的概率是多少。

#### 2. **`binom.cdf(k, n, p)`**
- **含义**：累积分布函数（CDF, Cumulative Distribution Function），用于计算在**一次二项分布实验**中，成功次数**小于等于 k** 的概率。
  - `k`：期望成功的次数上限。
  - `n`：实验的总次数。
  - `p`：每次实验成功的概率。

**示例**:
```python
prob_less_than_or_equal_1 = binom.cdf(1, 3, 0.3)
```
- 在这个例子中，`binom.cdf(1, 3, 0.3)` 表示：在 3 次签单尝试中，成功签单**最多 1 次**的概率是多少。

#### 3. **计算大于某个值的概率**
- 如果要计算**成功次数大于某个值 k** 的概率，可以通过 `1 - binom.cdf(k, n, p)` 来计算。
  - **原理**：`binom.cdf(k, n, p)` 计算的是**成功次数小于等于 k** 的概率，`1 - binom.cdf(k, n, p)` 则表示成功次数**大于 k** 的概率。

**示例**:
```python
prob_greater_than_1 = 1 - binom.cdf(1, 3, 0.3)
```
- 这里 `1 - binom.cdf(1, 3, 0.3)` 表示：在 3 次签单尝试中，成功**超过 1 次**的概率是多少。

### 总结：
- **`binom.pmf(k, n, p)`**：计算成功次数**正好等于 k** 的概率。
- **`binom.cdf(k, n, p)`**：计算成功次数**小于等于 k** 的累积概率。
- **计算大于某个值的概率**：通过 `1 - binom.cdf(k, n, p)` 计算成功次数**大于 k** 的概率。