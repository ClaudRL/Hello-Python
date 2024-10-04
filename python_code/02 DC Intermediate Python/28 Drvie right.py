# Exercise
# Driving right (2)
# The code in the previous example worked fine, but you actually unnecessarily created a new variable dr. You can achieve the same result without this intermediate variable. Put the code that computes dr straight into the square brackets that select observations from cars.

# Instructions
# 100 XP
# Convert the code to a one-liner that calculates the variable sel as before.

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
# dr = cars['drives_right']
# sel = cars[dr]
# sel = cars[cars['drives_right']]
sel = cars[cars['drives_right'] == True]
# Print sel
print(sel)

# 因为 cars['drives_right'] 本身就是布尔 Series，直接用于索引就可以筛选出 True 的行。
# sel = cars[cars['drives_right']]

# 要提取 drives_right 为 False 的行，可以使用以下代码：
# sel = cars[~cars['drives_right']]
# 解释：
# ~ 是布尔反转运算符，表示取反。因此 ~cars['drives_right'] 会返回 drives_right 列中为 False 的行。
# 这样就可以将 False 的行提取出来并存储在 sel 中。