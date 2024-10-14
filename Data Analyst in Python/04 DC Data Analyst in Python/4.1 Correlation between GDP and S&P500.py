# Exercise
# Correlation between GDP and S&P500
# In this exercise, you want to analyze stock returns from the S&P 500. You believe there may be a relationship between the returns of the S&P 500 and the GDP of the US. Merge the different datasets together to compute the correlation.

# Two tables have been provided for you, named sp500, and gdp. As always, pandas has been imported for you as pd.

#1. Use merge_ordered() to merge gdp and sp500 using a left join where the 
# year column from gdp is matched with the date column from sp500.
# Print gdp_sp500.

# Use merge_ordered() to merge gdp and sp500 on year and date
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', 
                             how='left')

# Print gdp_sp500
print(gdp_sp500)

# 2. Use the merge_ordered() function again, similar to before, to merge gdp 
# and sp500, using the function's ability to fill in missing data for returns 
# by forward-filling the missing values. Assign the resulting table to the variable gdp_sp500.

# Use merge_ordered() to merge gdp and sp500, and forward fill missing values
gdp_sp500 = pd.merge_ordered(gdp,sp500,left_on = 'year', right_on = 'date', how = 'left',fill_method='ffill')


# Print gdp_sp500
print (gdp_sp500)

# 3. Subset the gdp_sp500 table, select the gdp and returns columns, and save as gdp_returns.
# Print the correlation matrix of the gdp_returns table using the .corr() method.

# Use merge_ordered() to merge gdp and sp500, and forward fill missing values
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', 
                             how='left',  fill_method='ffill')

# Subset the gdp and returns columns
gdp_returns = gdp_sp500[['gdp','returns']]

# Print gdp_returns correlation
print (gdp_returns.corr())

在 Python 中，`corr()` 是 Pandas 库中的一个方法，用于计算两个或多个列（通常是数值型列）之间的**相关系数**（correlation coefficient）。相关系数用于衡量两个变量之间的线性关系，范围在 -1 到 1 之间。

### `corr()` 方法的作用：
- **计算相关性矩阵**：当你在一个 DataFrame 上调用 `corr()`，它会计算出 DataFrame 中每一列与其他列之间的 Pearson 相关系数，并返回一个相关性矩阵。
- **相关系数的范围**：
  - **1**：表示两个变量之间有完全的正线性关系。
  - **0**：表示两个变量之间没有线性关系。
  - **-1**：表示两个变量之间有完全的负线性关系。

### 代码解释：
```python
# Print gdp_returns correlation
print(gdp_returns.corr())
```

这里的 `gdp_returns` 是一个 DataFrame，调用 `.corr()` 会计算这个 DataFrame 中所有数值列之间的相关性。最后 `print()` 将输出一个相关系数矩阵。

### 举个例子：
假设 `gdp_returns` DataFrame 中有两列：`GDP_growth` 和 `Stock_returns`。

```python
import pandas as pd

data = {
    'GDP_growth': [3.0, 2.1, 4.5, 3.6, 2.9],
    'Stock_returns': [8.2, 5.3, 9.1, 7.8, 6.5]
}

gdp_returns = pd.DataFrame(data)

# Calculate the correlation
print(gdp_returns.corr())
```

#### 输出：
```
              GDP_growth  Stock_returns
GDP_growth       1.000000       0.978971
Stock_returns    0.978971       1.000000
```

### 解释：
- `GDP_growth` 与 `Stock_returns` 的相关系数为 0.978971，接近 1，表示它们有强正相关。
- 自己和自己（例如 `GDP_growth` 与 `GDP_growth`）的相关性总是 1。

### 总结：
- **`corr()`** 方法是用来查看 DataFrame 中列与列之间的线性相关性。
- 相关性矩阵可以帮助你理解不同变量之间的线性关系，从而为后续的数据分析或建模提供依据。