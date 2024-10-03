# Exercise
# Indexes and values (1)
# Using a for loop to iterate over a list only gives you access to every list element in each run, one after the other. If you also want to access the index information, so where the list element you're iterating over is located, you can use enumerate().

# As an example, have a look at how the for loop from the video was converted:

# fam = [1.73, 1.68, 1.71, 1.89]
# for index, height in enumerate(fam) :
#     print("person " + str(index) + ": " + str(height))
# Instructions
# 100 XP
# Adapt the for loop in the sample code to use enumerate() and use two iterator variables.
# Update the print() statement so that on each run, a line of the form "room x: y" should be printed, where x is the index of the list element and y is the actual list element, i.e. the area. Make sure to print out this exact string, with the correct spacing.

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for x, y in enumerate(areas) :
    print(f"room {x} : {y}")
    #print("room" + str(x) + ":" + str(y))


# 这段代码是一个Python程序，它使用了enumerate()函数来遍历一个列表并打印出每个房间的面积。让我为您详细解释这段代码：

# ## 代码解析

# 1. 定义列表：
#    ```python
#    areas = [11.25, 18.0, 20.0, 10.75, 9.50]
#    ```
#    这行代码创建了一个名为`areas`的列表，包含了5个浮点数，可能代表5个房间的面积（单位可能是平方米）。

# 2. 使用enumerate()的for循环：
#    ```python
#    for x, y in enumerate(areas):
#    ```
#    - `enumerate(areas)`函数返回一个迭代器，它生成包含索引和值的元组。
#    - `x`获取当前项的索引（从0开始）。
#    - `y`获取当前项的值（即面积）。

# 3. 打印语句：
#    ```python
#    print("room" + str(x) + ":" + str(y))
#    ```
#    这行代码打印出每个房间的信息：
#    - "room"是固定的字符串前缀。
#    - `str(x)`将索引转换为字符串（代表房间号）。
#    - ":"是分隔符。
#    - `str(y)`将面积值转换为字符串。

# ## 运行结果

# 执行这段代码后，输出将类似于：

# ```
# room0:11.25
# room1:18.0
# room2:20.0
# room3:10.75
# room4:9.5
# ```

# 每行显示一个房间的编号（从0开始）和对应的面积。

# ## 代码优化建议

# 1. 可以使用f-字符串来简化打印语句：
#    ```python
#    print(f"room {x}: {y}")
#    ```

# 2. 如果想让房间编号从1开始，可以修改为：
#    ```python
#    for x, y in enumerate(areas, 1):
#        print(f"room {x}: {y}")
#    ```

# 这段代码展示了如何有效地使用`enumerate()`函数来同时获取列表的索引和值，这在处理需要编号的数据时非常有用。

# 为什么是for x, y in enumerate(areas,1) ，而不是for x, y in enumerate(1, areas)

# 您的问题涉及了`enumerate()`函数的正确使用方式。让我解释一下为什么使用`for x, y in enumerate(areas, 1)`而不是`for x, y in enumerate(1, areas)`：

# ## enumerate()函数的参数顺序

# `enumerate()`函数的正确语法是：

# ```python
# enumerate(iterable, start=0)
# ```

# 1. 第一个参数（必需）：是要遍历的可迭代对象（如列表、元组等）。
# 2. 第二个参数（可选）：是开始计数的数字，默认为0。

# ## 正确用法解析

# `for x, y in enumerate(areas, 1)`:

# - `areas`是要遍历的列表（第一个参数）。
# - `1`是起始计数值（第二个参数），表示从1开始计数而不是默认的0。

# ## 错误用法解析

# `for x, y in enumerate(1, areas)`:

# 这种写法是错误的，因为：
# - 它把起始值`1`放在了第一个参数的位置。
# - 把要遍历的列表`areas`放在了第二个参数的位置。

# 这会导致Python解释器尝试对数字`1`进行遍历，而不是对`areas`列表进行遍历，从而引发错误。

# ## 实际应用示例

# 正确的用法：

# ```python
# areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# for x, y in enumerate(areas, 1):
#     print(f"room {x}: {y}")
# ```

# 输出：
# ```
# room 1: 11.25
# room 2: 18.0
# room 3: 20.0
# room 4: 10.75
# room 5: 9.5
# ```

# 这里，房间编号从1开始，而不是默认的0。

# 记住，`enumerate()`函数总是将要遍历的对象作为第一个参数，可选的起始值作为第二个参数。这种设计使得函数在大多数情况下可以只使用一个参数，同时在需要时还能灵活地指定起始值。

# Citations:
# [1] https://www.freecodecamp.org/news/python-enumerate-what-is-the-enumerate-function-in-python/
# [2] https://www.programiz.com/python-programming/methods/built-in/enumerate
# [3] https://www.simplilearn.com/tutorials/python-tutorial/enumerate-in-python
# [4] https://www.w3schools.com/python/ref_func_enumerate.asp
# [5] https://realpython.com/python-enumerate/
# [6] https://learn.microsoft.com/zh-cn/cpp/cpp/assignment-operators?view=msvc-170
# [7] https://www.cnblogs.com/youqc/p/12067854.html
# [8] https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Addition_assignment