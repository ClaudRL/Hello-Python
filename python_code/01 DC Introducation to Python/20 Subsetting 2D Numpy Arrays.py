import numpy as np

np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49,:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]

# Print out height of 124th player
print(np_baseball[123,0])

# 解释 , 在 np_baseball[49, :] 和 np_baseball[123, 0] 中的作用：
# 在 NumPy 数组中，使用 , 可以指定行和列的索引：
# np_baseball[row_index, column_index]：row_index 表示行的索引，column_index 表示列的索引。
# 1. np_baseball[49, :]
# 49：表示第 50 行，索引从 0 开始，所以索引 49 表示第 50 行。
# :：表示选择所有列。因此，这一行代码的意思是选取第 50 行的所有列。
# 这样可以得到第 50 个球员的所有信息，例如他们的身高和体重。
# 2. np_baseball[:, 1]
# :：表示选择所有行。
# 1：表示选择第 2 列（因为索引从 0 开始，1 表示第二列）。
# 这样可以得到每个球员的体重（假设第 2 列存储的是体重）。
# 3. np_baseball[123, 0]
# 123：表示第 124 行（因为索引从 0 开始，123 表示第 124 行）。
# 0：表示选择第 1 列。因此，这一行代码的意思是选取第 124 个球员的身高（假设第 1 列存储的是身高）。
# 总结：
# , 用于区分行和列的索引。
# : 用于表示所有行或所有列，具体取决于它的位置。
# np_baseball[49, :] 获取第 50 行的所有列。
# np_baseball[:, 1] 获取所有行的第二列。
# np_baseball[123, 0] 获取第 124 个球员的第一列（身高）。
# 这种索引方式在处理多维数组时非常灵活，可以精确地获取数据的行、列或者子数组。
