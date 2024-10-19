# Calculating probabilities
# You're in charge of the sales team, and it's time for performance reviews, starting with Amir. As part of the review, you want to randomly select a few of the deals that he's worked on over the past year so that you can look at them more deeply. Before you start selecting deals, you'll first figure out what the chances are of selecting certain deals.

# Recall that the probability of an event can be calculated by
 

# Both pandas as pd and numpy as np are loaded and amir_deals is available.



# 1. Count the number of deals Amir worked on for each product type using .value_counts() and store in counts.
# Count the deals for each product
counts = amir_deals['product'].value_counts(normalize=False)
print(counts)

# 2. Calculate the probability of selecting a deal for the different 
# product types by dividing the counts by the total number of deals 
# Amir worked on. Save this as probs.

# Count the deals for each product
counts = amir_deals['product'].value_counts()

# Calculate probability of picking a deal with each product
probs = amir_deals['product'].value_counts(normalize=True)
print(probs)


`normalize=True` 是 `pandas.Series.value_counts()` 方法的一个参数，表示将结果标准化为比例或概率，而不是返回每个类别的绝对计数。

### 详细解释：

- **默认行为 (normalize=False)**：
  `value_counts()` 默认返回的是各个类别（或值）在数据中出现的绝对频数，也就是每个类别出现的次数。

  例如，假设你有一个包含三种产品的交易记录：

  ```python
  import pandas as pd

  amir_deals = pd.Series(['Product A', 'Product B', 'Product A', 'Product C', 'Product A', 'Product B'])

  counts = amir_deals.value_counts()
  print(counts)
  ```

  输出可能是：
  ```
  Product A    3
  Product B    2
  Product C    1
  dtype: int64
  ```

  这表示 `Product A` 出现了 3 次，`Product B` 出现了 2 次，`Product C` 出现了 1 次。

- **使用 normalize=True**：
  当 `normalize=True` 时，`value_counts()` 返回的是每个类别在总数中的相对比例，也就是该类别占整个数据的百分比（或概率）。

  例如：

  ```python
  probs = amir_deals.value_counts(normalize=True)
  print(probs)
  ```

  输出将是：
  ```
  Product A    0.50
  Product B    0.33
  Product C    0.17
  dtype: float64
  ```

  这里的 `0.50` 表示 `Product A` 占所有产品的 50%，`0.33` 表示 `Product B` 占 33%，`0.17` 表示 `Product C` 占 17%。

### 总结：
- **`normalize=False` (默认)**：返回每个类别的绝对出现次数。
- **`normalize=True`**：返回每个类别的相对频率（比例），通常用于计算概率或查看类别分布的比例。

在数据分析中，使用 `normalize=True` 可以方便地查看每个类别的占比，而不需要手动计算比例。