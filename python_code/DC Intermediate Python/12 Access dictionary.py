# Exercise
# Access dictionary
# If the keys of a dictionary are chosen wisely, accessing the values in a dictionary is easy and intuitive. For example, to get the capital for France from europe you can use:

# europe['france']
# Here, 'france' is the key and 'paris' the value is returned.

# Instructions
# 100 XP
# Check out which keys are in europe by calling the keys() method on europe. Print out the result.
# Print out the value that belongs to the key 'norway'.

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe['norway'])



# 你的代码中有一些错误，主要是使用了不正确的语法来访问字典的键和值。以下是修改后的代码和解释：

# ### 修改后的代码：
# ```python
# # 定义字典
# europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin', 'norway': 'oslo'}

# # 打印字典中的所有键
# print(europe.keys())

# # 打印 'norway' 对应的值
# print(europe['norway'])
# ```

# ### 解释：

# 1. **字典定义**：
#    ```python
#    europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin', 'norway': 'oslo'}
#    ```
#    - 定义了一个名为 `europe` 的字典，其中 `spain`、`france`、`germany` 和 `norway` 是键，对应的值分别是它们的首都。

# 2. **打印字典中的所有键**：
#    ```python
#    print(europe.keys())
#    ```
#    - 使用 `europe.keys()` 打印字典中的所有键 (`'spain'`, `'france'`, `'germany'`, `'norway'`)。
#    - `.keys()` 是字典的方法，用于返回所有键的列表（在 Python 3 中，返回的是 `dict_keys` 视图）。

# 3. **打印 `'norway'` 对应的值**：
#    ```python
#    print(europe['norway'])
#    ```
#    - 使用 `europe['norway']` 访问字典中键为 `'norway'` 的值，这里应该输出 `'oslo'`。
#    - 注意访问字典值的语法是使用 `[]`，而不是 `()`。

# ### 错误解释：

# 1. **`print(keys['spain','france','germany','norway'])`**：
#    - 这里 `keys` 并没有被定义。
#    - 正确的做法是使用 `europe.keys()` 来获取字典的键。

# 2. **`print(keys('norway'))`**：
#    - 访问字典中的值应该使用 `[]`，而不是 `()`。
#    - 应该改为 `print(europe['norway'])`。