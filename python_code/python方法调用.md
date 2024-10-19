在 Python 中，尤其是使用 Pandas 处理数据时，不同的操作和方法有不同的结构和调用方式。以下是总结 Python 代码结构时，常见的调用规则以及 `.x()` 和 `df['']` 的使用场景：

### 1. **方法调用：`df.x()`**
   使用 `.x()` 的格式是直接调用对象的方法。Pandas DataFrame 和 Series 提供了许多内置方法，可以对整个数据框或某些列执行操作。

   - **何时使用：**
     - 当你想使用 DataFrame 的内置方法时，例如统计、转换、筛选等。
     - 这些方法大多可以在 DataFrame 或 Series 上直接调用，操作整个表或列。
   
   - **常见例子：**
     - `df.head()`：查看前几行数据。
     - `df.describe()`：查看数据的描述性统计信息。
     - `df.groupby('column').sum()`：按列分组并汇总。
     - `df.dropna()`：删除空值。
     - `df.sort_values('column')`：根据某一列排序。
   
   - **例子：**
     ```python
     # 查看数据框的前 5 行
     df.head()
     
     # 根据某列排序
     df.sort_values('age')
     
     # 删除缺失值
     df.dropna()
     ```

### 2. **列访问：`df['column']`**
   使用 `df['column']` 是一种获取 DataFrame 中某一列的常用方式，返回的是一个 Pandas Series。

   - **何时使用：**
     - 当你想访问特定列时，尤其是在你需要进一步对某列数据进行操作时（如筛选、统计等）。
     - 可以用 `df['column']` 来提取某列，然后对其进行计算或处理。
     - 还可以用 `df[['col1', 'col2']]` 来选择多列（注意双层方括号，返回一个 DataFrame）。
   
   - **常见例子：**
     - `df['column']`：访问特定的列。
     - `df['column'].mean()`：计算某列的平均值。
     - `df['column'].value_counts()`：统计某列中唯一值的频率。

   - **例子：**
     ```python
     # 访问某一列
     age_series = df['age']
     
     # 计算某列的均值
     mean_age = df['age'].mean()
     
     # 统计某列的频率分布
     product_counts = df['product'].value_counts()
     ```

### 3. **区别和选择：**
   - **`.x()`** 是方法调用，用于执行某些特定的操作。比如 `df.mean()` 是计算整个数据框的平均值，而 `df['age'].mean()` 是计算某一列的平均值。
   - **`df['column']`** 是一种从数据框中选择某列的方式。选择列后，你可以进一步对该列进行操作。

### 4. **方法和列访问结合使用：**
   很多情况下，列选择和方法调用是连在一起使用的，比如：
   
   - **连贯操作：**
     ```python
     # 访问列并调用统计方法
     mean_price = df['price'].mean()
     
     # 访问列并调用分类统计方法
     unique_products = df['product'].value_counts()
     ```

### 总结：
- **`.x()`**：适用于调用 DataFrame 或 Series 对象上的方法，常用于数据操作、变换和统计。
- **`df['column']`**：用于选择某一列或多列数据，并常与 `.x()` 方法链式调用，对列进行进一步操作。

### 案例对比：
```python
# 使用方法提取列并操作
mean_age = df['age'].mean()

# 使用方括号提取列
age_series = df['age']
mean_age = age_series.mean()

# 直接方法操作
mean_values = df.mean()
``` 

两者相辅相成，根据场景和需求合理选择即可。