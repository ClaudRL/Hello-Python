`groupby()` 是 Pandas 中非常强大的数据分组函数，允许用户按一个或多个键对数据进行分组，并对分组后的数据应用聚合函数。下面是 `groupby()` 的所有关键参数及其用法：

### 1. **`by`**
   - **含义**：指定按哪些列或序列来分组。
   - **类型**：可以是单列（字符串）、多列（列表）、或者自定义函数、Series 等。
   - **示例**：
     ```python
     # 按 'department' 列分组
     df.groupby('department')
     
     # 按 'department' 和 'gender' 列同时分组
     df.groupby(['department', 'gender'])
     ```

### 2. **`axis`**
   - **含义**：指定沿哪个轴进行分组，默认是 `axis=0`（按行分组）。
   - **类型**：`0` 或 `1`，`0` 表示按行分组，`1` 表示按列分组。
   - **示例**：
     ```python
     # 按行（axis=0）分组，默认
     df.groupby('department', axis=0)
     
     # 按列（axis=1）分组
     df.groupby('department', axis=1)
     ```

### 3. **`level`**
   - **含义**：对多层索引（MultiIndex）进行分组时，指定使用哪个层级（`level`）进行分组。
   - **类型**：`int` 或 `list of int`（层级的索引）。
   - **示例**：
     ```python
     # 按 MultiIndex 的第一级分组
     df.groupby(level=0)
     
     # 按 MultiIndex 的第一级和第二级同时分组
     df.groupby(level=[0, 1])
     ```

### 4. **`as_index`**
   - **含义**：控制分组键是否作为结果 DataFrame 的索引，默认 `True`。
   - **类型**：`bool`，`True` 或 `False`。
   - **示例**：
     ```python
     # 分组键作为索引（默认行为）
     df.groupby('department', as_index=True).agg({'salary': 'mean'})
     
     # 分组键保留为普通列
     df.groupby('department', as_index=False).agg({'salary': 'mean'})
     ```

### 5. **`sort`**
   - **含义**：控制分组键是否按顺序排序，默认 `True`。`False` 可加快计算速度。
   - **类型**：`bool`，`True` 或 `False`。
   - **示例**：
     ```python
     # 按分组键排序（默认行为）
     df.groupby('department', sort=True)
     
     # 不按分组键排序，性能更好
     df.groupby('department', sort=False)
     ```

### 6. **`group_keys`**
   - **含义**：控制分组键是否包含在结果的索引中，默认 `True`。如果为 `False`，键不包含在结果索引中。
   - **类型**：`bool`，`True` 或 `False`。
   - **示例**：
     ```python
     # 默认，group_keys=True
     df.groupby('department', group_keys=True).apply(lambda x: x.head(2))
     
     # group_keys=False，不包含分组键
     df.groupby('department', group_keys=False).apply(lambda x: x.head(2))
     ```

### 7. **`observed`**
   - **含义**：针对 `categorical` 类型的数据，控制是否仅显示在分组数据中实际出现的分类。默认 `False` 会显示所有分类，即使某些分组没有数据。
   - **类型**：`bool`，`True` 或 `False`。
   - **示例**：
     ```python
     # 默认，显示所有分类（包括未出现的）
     df.groupby(['department', 'gender'], observed=False).agg('mean')
     
     # 只显示出现的分类
     df.groupby(['department', 'gender'], observed=True).agg('mean')
     ```

### 8. **`dropna`**
   - **含义**：控制是否丢弃所有值为 `NaN` 的分组，默认 `True`（丢弃 `NaN` 分组）。`False` 则保留 `NaN`。
   - **类型**：`bool`，`True` 或 `False`。
   - **示例**：
     ```python
     # 默认，丢弃所有分组键为 NaN 的行
     df.groupby('department', dropna=True).agg('sum')
     
     # 保留 NaN 的分组
     df.groupby('department', dropna=False).agg('sum')
     ```

### 示例：完整 `groupby()` 用法

假设有如下 DataFrame：

```python
import pandas as pd

data = {
    'department': ['HR', 'IT', 'HR', 'IT', 'HR', 'IT'],
    'gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Female'],
    'salary': [60000, 75000, 50000, 80000, 62000, 70000],
    'age': [25, 28, 32, 30, 40, 26]
}
df = pd.DataFrame(data)
```

#### 1. **按单列分组并计算平均值**
```python
df.groupby('department').agg({'salary': 'mean'})
```

#### 2. **按多列分组并计算总和**
```python
df.groupby(['department', 'gender']).agg({'salary': 'sum'})
```

#### 3. **保留分组键为普通列**
```python
df.groupby('department', as_index=False).agg({'salary': 'mean'})
```

#### 4. **按多层索引分组**
```python
# 先设置一个多层索引
df_multi = df.set_index(['department', 'gender'])
# 按第一层（department）分组
df_multi.groupby(level=0).agg({'salary': 'mean'})
```

#### 5. **只按出现的分类进行分组**
```python
df['gender'] = pd.Categorical(df['gender'], categories=['Male', 'Female', 'Other'])
df.groupby(['department', 'gender'], observed=True).agg({'salary': 'mean'})
```

### 总结：
`groupby()` 通过结合不同参数，可以灵活地进行分组计算，适用于各种复杂的数据分析场景。