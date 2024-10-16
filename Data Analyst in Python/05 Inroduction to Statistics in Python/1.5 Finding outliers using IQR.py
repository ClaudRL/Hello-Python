# Exercise
# Finding outliers using IQR
# Outliers can have big effects on statistics like mean, as well as statistics that rely on the mean, such as variance and standard deviation. Interquartile range, or IQR, is another way of measuring spread that's less influenced by outliers. IQR is also often used to find outliers. If a value is less than 
#  or greater than 
# , it's considered an outlier. In fact, this is how the lengths of the whiskers in a matplotlib box plot are calculated.

# Diagram of a box plot showing median, quartiles, and outliers

# In this exercise, you'll calculate IQR and use it to find some outliers. pandas as pd and numpy as np are loaded and food_consumption is available.

# 1. Calculate the total co2_emission per country by grouping by country and taking the sum of co2_emission. Store the resulting DataFrame as emissions_by_country.

# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')['co2_emission'].agg('sum')

print(emissions_by_country)

# 2. Compute the first and third quartiles of emissions_by_country and store these as q1 and q3.
# Calculate the interquartile range of emissions_by_country and store it as iqr.

# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()
print(emissions_by_country)
# Compute the first and third quartiles and IQR of emissions_by_country
q1 = np.quantile(emissions_by_country,0.25)
q3 = np.quantile(emissions_by_country,0.75)
iqr = q3 - q1


# 3. Calculate the lower and upper cutoffs for outliers of emissions_by_country, 
# and store these as lower and upper.

# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()

# Compute the first and third quantiles and IQR of emissions_by_country
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1

# Calculate the lower and upper cutoffs for outliers
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# 4. Subset emissions_by_country to get countries with a total emission 
# greater than the upper cutoff or a total emission less than the lower cutoff.

# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()

# Compute the first and third quantiles and IQR of emissions_by_country
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1

# Calculate the lower and upper cutoffs for outliers
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# Subset emissions_by_country to find outliers
outliers = emissions_by_country[(emissions_by_country < lower) | (emissions_by_country >upper)]
print(outliers)

#-------------------------------------------------------------------------------------
将上述 Python 代码转换为 SQL 查询，可以使用窗口函数来计算四分位数和 IQR。
这里是 SQL 查询的一个可能实现，假设你使用的是一个支持窗口函数的 SQL 数据库（如 PostgreSQL、MySQL 8.0+等）：

```sql
WITH emissions AS (
    -- 计算每个国家的总 CO2 排放量
    SELECT country, SUM(co2_emission) AS total_co2_emission
    FROM food_consumption
    GROUP BY country
),
quartiles AS (
    -- 计算第一和第三四分位数
    SELECT
        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY total_co2_emission) AS q1,
        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY total_co2_emission) AS q3
    FROM emissions
),
iqr AS (
    -- 计算 IQR
    SELECT 
        q1,
        q3,
        (q3 - q1) AS iqr
    FROM quartiles
)
-- 查找异常值
SELECT e.country, e.total_co2_emission
FROM emissions e
JOIN iqr i ON 1=1
WHERE e.total_co2_emission < (i.q1 - 1.5 * i.iqr) OR 
      e.total_co2_emission > (i.q3 + 1.5 * i.iqr);
```

### SQL 查询解释：
1. **第一个 CTE（公用表表达式）`emissions`**:
   - 计算每个国家的总 CO2 排放量，结果包含 `country` 和 `total_co2_emission` 两列。

2. **第二个 CTE `quartiles`**:
   - 使用 `PERCENTILE_CONT` 函数计算第一和第三四分位数（Q1 和 Q3）。

3. **第三个 CTE `iqr`**:
   - 计算 IQR（Q3 - Q1）。

4. **最终查询**:
   - 将 `emissions` 表与 `iqr` 表连接，并筛选出 CO2 排放量在异常值范围内的记录，结果包含国家名称和对应的总 CO2 排放量。

这个 SQL 查询的逻辑与 Python 代码中的计算相同，能够找到 CO2 排放量的异常值。