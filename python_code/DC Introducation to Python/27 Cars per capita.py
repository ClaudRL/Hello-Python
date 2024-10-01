# Exercise
# Cars per capita (2)
# Remember about np.logical_and(), np.logical_or() and np.logical_not(), the NumPy variants of the and, or and not operators? You can also use them on Pandas Series to do more advanced filtering operations.

# Take this example that selects the observations that have a cars_per_cap between 10 and 80. Try out these lines of code step by step to see what's happening.

# cpc = cars['cars_per_cap']
# between = np.logical_and(cpc > 10, cpc < 80)
# medium = cars[between]
# Instructions
# 100 XP
# Use the code sample provided to create a DataFrame medium, that includes all the observations of cars that have a cars_per_cap between 100 and 500.
# # Print out medium.

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
medium = cars['cars_per_cap']
between = np.logical_and(cars['cars_per_cap'] > 100, cars['cars_per_cap'] < 500)
medium =cars[between]

# Print medium
print(medium)

# 解释：
# 布尔掩码（Boolean Mask）：

# python
# Copy code
# between = np.logical_and(cars['cars_per_cap'] > 100, cars['cars_per_cap'] < 500)
# cars['cars_per_cap'] 选择 cars DataFrame 中的 cars_per_cap 列。
# 使用 np.logical_and() 创建一个布尔掩码，检查每一行的 cars_per_cap 是否在 100 到 500 之间。
# 过滤 DataFrame：

# python
# Copy code
# medium = cars[between]
# 使用布尔掩码 between 对 cars 进行行筛选，只保留满足条件的行。
# 输出筛选结果：

# print(medium) 会输出 cars_per_cap 在 100 到 500 之间的观测数据。
# 这样就能实现对 cars_per_cap 在一定范围内的行进行筛选并输出结果。