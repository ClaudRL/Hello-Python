# Exercise
# Subsetting rows
# A large part of data science is about finding which bits of your dataset are interesting. One of the simplest techniques for this is to find a subset of rows that match some criteria. This is sometimes known as filtering rows or selecting rows.

# There are many ways to subset a DataFrame, perhaps the most common is to use relational operators to return True or False for each row, then pass that inside square brackets.

# dogs[dogs["height_cm"] > 60]
# dogs[dogs["color"] == "tan"]
# You can filter for multiple conditions at once by using the "bitwise and" operator, &.

# dogs[(dogs["height_cm"] > 60) & (dogs["color"] == "tan")]
# homelessness is available and pandas is loaded as pd.

# 1. ilter homelessness for cases where the number of individuals is greater than ten thousand, assigning to ind_gt_10k. View the printed result.
# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness['individuals'] > 10000]

# See the result
print(ind_gt_10k)

# 2. Filter homelessness for cases where the USA Census region is "Mountain", assigning to mountain_reg. View the printed result.
# Filter for rows where region is Mountain
mountain_reg = homelessness[homelessness['region'] == "Mountain"]

# See the result
print(mountain_reg)

# 3. Filter homelessness for cases where the number of family_members is less than one thousand and the region is "Pacific", assigning to fam_lt_1k_pac. View the printed result.
# Filter for rows where family_members is less than 1000 
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness['family_members'] < 1000) & (homelessness['region'] == "Pacific")]

# See the result
print(fam_lt_1k_pac)


# 这个代码确实很好地展示了圆括号`()`和方括号`[]`在pandas中的不同用途。让我们逐步分析：

# 1. 方括号 `[]` 的使用：

#    `homelessness[...]` 中的方括号用于在DataFrame中选择行。这里我们使用布尔索引来选择满足特定条件的行。

# 2. 圆括号 `()` 的使用：

#    圆括号在这里有两个作用：
   
#    a. 用于分组逻辑条件：`(homelessness['family_members'] < 1000)` 和 `(homelessness['region'] == "Pacific")`
   
#    b. 包围整个条件表达式：`[(homelessness['family_members'] < 1000) & (homelessness['region'] == "Pacific")]`

# 3. 条件组合：

#    `&` 操作符用于组合两个条件。圆括号确保每个条件被正确计算，然后再进行组合。

# 总结一下使用规则：

# - 使用 `[]` 当：
#   1. 在DataFrame中选择列：`df['column_name']`
#   2. 在DataFrame中使用布尔索引选择行：`df[boolean_condition]`

# - 使用 `()` 当：
#   1. 分组逻辑操作，特别是在复杂的布尔条件中
#   2. 确保操作优先级正确，类似于数学表达式

# - 在复杂的数据选择操作中，通常会同时看到 `[]` 和 `()`，如你提供的例子所示。

# 这种语法可能初看起来有点复杂，但随着使用频率的增加，它会变得更加直观。您对这个解释还有什么疑问吗？

