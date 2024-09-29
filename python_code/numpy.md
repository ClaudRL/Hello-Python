
NumPy 数据处理方面占有很重要的地位，这里列举了8点，一定先对Numpy有一个全面的认识。多维数组：NumPy的主要数据结构是多维数组（numpy.ndarray），它提供了高效的存储和操作多维数据的功能。在机器学习中，数据通常表示为多维数组，因此NumPy提供了一个方便的方式来操作和处理这些数据。数学函数：NumPy提供了丰富的数学函数，涵盖了基本的数学运算、线性代数、傅立叶变换等。这些函数对于机器学习算法的实现和优化至关重要。快速运算：NumPy的底层实现使用了C语言，因此它的运算速度非常快。在处理大规模数据时，NumPy的高效运算能力非常有帮助。广播功能：NumPy的广播功能允许在不同大小的数组上进行算术运算，使得代码更简洁、可读性更强，并且减少了内存消耗。随机数生成：NumPy提供了强大的随机数生成功能，包括多种分布的随机数生成器。这在模拟数据、初始化模型参数等方面非常有用。与其他库的整合：NumPy与许多其他Python库（如SciPy、Pandas、Matplotlib等）紧密整合，使得它们之间可以方便地交换数据，并共同构建复杂的数据处理和可视化流水线。线性代数操作：NumPy提供了丰富的线性代数操作，如矩阵乘法、求逆、特征值分解等。这对于许多机器学习算法，特别是深度学习算法来说至关重要。内存优化：NumPy的数据结构经过优化，可以更有效地利用内存，特别是对于大规模数据集和计算密集型任务来说，这是至关重要的。现在懂了吧，NumPy在机器学习处理数据中具有不可替代的重要地位。数据的表示、数据的操作和数据的计算，Numpy都提供了强大的工具基础。下面的50个操作，都是最最常用到的，点赞，收藏，后面备用~
1. 创建数组使用 np.array() 将 Python 列表转换为 NumPy 数组。使用方式：import numpy as np

# 创建数组
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print(my_array)
2. 数组形状使用 np.shape、np.reshape() 或 np.ndarray.shape 查看数组形状，使用 np.reshape() 改变数组形状。使用方式：import numpy as np

# 创建数组
my_array = np.array([[1, 2, 3], [4, 5, 6]])

# 查看数组形状
print("数组形状:", my_array.shape)

# 改变数组形状
reshaped_array = np.reshape(my_array, (3, 2))
print("改变形状后的数组:\n", reshaped_array)
3. 数组维度使用 np.ndim 或 np.ndarray.ndim 查看数组维度。使用方式：import numpy as np

# 创建数组
my_array = np.array([[1, 2, 3], [4, 5, 6]])

# 查看数组维度
print("数组维度:", my_array.ndim)
4. 数组大小使用 np.size 或 np.ndarray.size 查看数组大小。使用方式：import numpy as np

# 创建数组
my_array = np.array([[1, 2, 3], [4, 5, 6]])

# 查看数组大小
print("数组大小:", my_array.size)
5. 数组数据类型使用 np.dtype 或 np.ndarray.dtype 查看数组数据类型。使用方式：import numpy as np

# 创建数组
my_array = np.array([[1, 2, 3], [4, 5, 6]])

# 查看数组数据类型
print("数组数据类型:", my_array.dtype)
6. 数组类型转换使用 np.astype() 或 np.ndarray.astype 转换数组数据类型。使用方式：import numpy as np

# 创建数组
my_array = np.array([[1, 2, 3], [4, 5, 6]])

# 转换数组数据类型
float_array = my_array.astype(float)
print("转换后的数组数据类型:", float_array.dtype)
7. 数组填充使用 np.zeros()、np.ones()、np.full() 或 np.empty() 创建特定填充值的数组。使用方式：import numpy as np

# 创建全零数组
zeros_array = np.zeros((2, 3))
print("全零数组:\n", zeros_array)

# 创建全一数组
ones_array = np.ones((2, 3))
print("全一数组:\n", ones_array)

# 创建特定填充值数组
full_array = np.full((2, 3), 5)
print("特定填充值数组:\n", full_array)

# 创建未初始化数组
empty_array = np.empty((2, 3))
print("未初始化数组:\n", empty_array)
8. 数组范围使用 np.arange() 或 np.linspace() 创建指定范围的数组。使用方式：import numpy as np

# 创建指定范围的

数组
arange_array = np.arange(1, 10, 2)  # 步长为2的数组，包含1，不包含10
print("arange数组:", arange_array)

# 创建等间隔的数组
linspace_array = np.linspace(1, 10, 5)  # 从1到10，共5个数，等间隔
print("linspace数组:", linspace_array)
9. 随机数组使用 np.random.rand()、np.random.randn()、np.random.randint() 或 np.random.random() 创建随机数组。使用方式：import numpy as np

# 创建服从均匀分布的随机数组
rand_array = np.random.rand(2, 3)
print("均匀分布的随机数组:\n", rand_array)

# 创建服从标准正态分布的随机数组
randn_array = np.random.randn(2, 3)
print("标准正态分布的随机数组:\n", randn_array)

# 创建指定范围的随机整数数组
randint_array = np.random.randint(1, 10, size=(2, 3))
print("指定范围的随机整数数组:\n", randint_array)

# 创建服从均匀分布的随机数组
random_array = np.random.random((2, 3))
print("均匀分布的随机数组:\n", random_array)
10. 数组索引使用数组索引获取特定元素或行。使用方式：import numpy as np

# 创建数组
my_array = np.array([[1, 2, 3], [4, 5, 6]])

# 获取特定元素
print("第一个元素:", my_array[0, 0])
print("最后一个元素:", my_array[-1, -1])

# 获取特定行
print("第一行:", my_array[0, :])
11. 数组切片使用切片操作获取特定区域的数组元素。使用方式：import numpy as np

# 创建数组
my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 获取子数组
sub_array = my_array[0:2, 1:3]
print("子数组:\n", sub_array)
12. 数组形状改变使用 np.reshape()、np.ravel() 或 np.flatten() 改变数组形状。使用方式：import numpy as np

# 创建数组
my_array = np.array([[1, 2, 3], [4, 5, 6]])

# 改变数组形状
reshaped_array = np.reshape(my_array, (3, 2))
print("改变形状后的数组:\n", reshaped_array)
13. 数组转置使用 np.transpose() 或 np.ndarray.T 对数组进行转置操作。使用方式：import numpy as np

# 创建数组
my_array = np.array([[1, 2, 3], [4, 5, 6]])

# 对数组进行转置操作
transposed_array = np.transpose(my_array)
print("转置后的数组:\n", transposed_array)
14. 数组连接使用 np.concatenate()、np.vstack()、np.hstack() 或 np.column_stack() 连接数组。使用方式：import numpy as np

# 创建数组
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

# 沿水平方向连接数组
hstacked_array = np.hstack((array1, array2))
print("水平连接的数组:\n", hstacked_array)

# 沿垂直方向连接数组
vstacked_array = np.vstack((array1, array2))
print("垂直连接的数组:\n", vstacked_array)
15. 数组拆分使用 np.split()、np.vsplit()、np.hsplit() 或 np.array_split() 对数组进行拆分操作。
简单说明：将数组拆分为多个子数组。使用方式：import numpy as np

# 创建数组
my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 沿垂直方向拆分数组
split_arrays = np.vsplit(my_array, 3)
print("垂直拆分的数组:")
for arr in split_arrays:
    print(arr)

# 沿水平方向拆分数组
split_arrays = np.hsplit(my_array, 3)
print("水平拆分的数组:")
for arr in split_arrays:
    print(arr)
16. 数组重复使用 np.repeat() 或 np.tile() 对数组进行重复操作。使用方式：import numpy as np

# 创建数组
my_array = np.array([1, 2, 3])

# 数组元素重复
repeated_array = np.repeat(my_array, 3)
print("重复后的数组:", repeated_array)

# 数组重复
tiled_array = np.tile(my_array, 3)
print("重复后的数组:", tiled_array)
17. 数组排序使用 np.sort()、np.argsort()、np.lexsort()、np.argmax() 或 np.argmin() 对数组进行排序和获取索引。使用方式：import numpy as np

# 创建数组
my_array = np.array([3, 1, 2, 5, 4])

# 对数组进行排序
sorted_array = np.sort(my_array)
print("排序后的数组:", sorted_array)

# 获取排序后的索引
sorted_indices = np.argsort(my_array)
print("排序后的索引:", sorted_indices)
18. 数组最大最小值使用 np.max()、np.min()、np.argmax() 或 np.argmin() 获取数组的最大最小值及其索引。使用方式：import numpy as np

# 创建数组
my_array = np.array([3, 1, 2, 5, 4])

# 获取数组的最大值和最小值
max_value = np.max(my_array)
min_value = np.min(my_array)
print("数组的最大值:", max_value)
print("数组的最小值:", min_value)

# 获取数组的最大值和最小值的索引
max_index = np.argmax(my_array)
min_index = np.argmin(my_array)
print("数组的最大值索引:", max_index)
print("数组的最小值索引:", min_index)
19. 数组求和使用 np.sum() 或 np.cumsum() 对数组元素求和或进行累积和计算。使用方式：import numpy as np

# 创建数组
my_array = np.array([1, 2, 3, 4, 5])

# 计算数组元素的和
sum_value = np.sum(my_array)
print("数组元素的和:", sum_value)

# 计算数组元素的累积和
cumsum_array = np.cumsum(my_array)
print("数组元素的累积和:", cumsum_array)
20. 数组平均值使用 np.mean() 或 np.average() 计算数组元素的平均值。使用方式：import numpy as np

# 创建数组
my_array = np.array([1, 2, 3, 4, 5])

# 计算数组元素的平均值
mean_value = np.mean(my_array)
print("数组元素的平均值:", mean_value)
21. 数组中值使用 np.median() 计算数组元素的中位数。使用方式：import numpy as np

# 创建数组
my_array = np.array([1, 2, 3, 4, 5])

# 计算数组元素的中位数
median_value = np.median(my_array)
print("数组元素的中位数:", median_value)
22. 数组标准差使用 np.std() 计算数组元素的标准差。使用方式：import numpy as np

# 创建数组
my_array = np.array([1, 2, 3, 4, 5])

# 计算数组元素的标准差
std_value = np.std(my_array)
print("数组元素的标准差:", std_value)
23. 数组方差使用 np.var() 计算数组元素的方差。使用方式：import numpy as np

# 创建数组
my_array = np.array([1, 2, 3, 4, 5])

# 计算数组元素的方差
var_value = np.var(my_array)
print("数组元素的方差:", var_value)
24. 数组行列求和使用 np.sum(axis=0/1) 计算数组的行列和。使用方式：import numpy as np

# 创建数组
my_array = np.array([[1, 2, 3], [4, 5, 6]])

# 计算数组的行和
row_sum = np.sum(my_array, axis=1)
print("数组的行和:", row_sum)

# 计算数组的列和
col_sum = np.sum(my_array, axis=0)
print("数组的列和:", col_sum)
25. 数组指定轴计算使用 np.apply_along_axis() 对数组指定轴应用自定义函数。使用方式：import numpy as np

# 创建数组
my_array = np.array([[1, 2, 3], [4, 5, 6]])

# 自定义函数
def custom_function(x):
    return x * 2

# 对数组指定轴应用自定义函数
new_array = np.apply_along_axis(custom_function, axis=1, arr=my_array)
print("应用自定义函数后的数组:\n", new_array)

26. 数组元素加减乘除使用 np.add()、np.subtract()、np.multiply()、np.divide() 或 np.power() 对数组元素进行加减乘除操作。使用方式：import numpy as np

# 创建数组
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# 数组元素加法
add_result = np.add(array1, array2)
print("数组元素加法:", add_result)

# 数组元素减法
subtract_result = np.subtract(array1, array2)
print("数组元素减法:", subtract_result)

# 数组元素乘法
multiply_result = np.multiply(array1, array2)
print("数组元素乘法:", multiply_result)

# 数组元素除法
divide_result = np.divide(array1, array2)
print("数组元素除法:", divide_result)

# 数组元素幂运算
power_result = np.power(array1, 2)
print("数组元素幂运算:", power_result)
27. 数组元素取余使用 np.mod() 或 np.remainder() 对数组元素进行取余操作。使用方式：import numpy as np

# 创建数组
my_array = np.array([1, 2, 3, 4, 5])

# 对数组元素进行取余操作
mod_result = np.mod(my_array, 2)
print("数组元素取余操作:", mod_result)
28. 数组元素绝对值使用 np.abs() 计算数组元素的绝对值。使用方式：import numpy as np

# 创建数组
my_array = np.array([-1, -2, 3, 4, -5])

# 计算数组元素的绝对值
abs_array = np.abs(my_array)
print("数组元素的绝对值:", abs_array)
29. 数组元素舍入使用 np.round()、np.floor()、np.ceil() 或 np.trunc() 对数组元素进行舍入操作。使用方式：import numpy as np

# 创建数组
my_array = np.array([1.2, 2.7, 3.5, 4.1, 5.9])

# 对数组元素进行舍入操作
round_array = np.round(my_array)
print("数组元素舍入:", round_array)

# 向下取整
floor_array = np.floor(my_array)
print("数组元素向下取整:", floor_array)

# 向上取整
ceil_array = np.ceil(my_array)
print("数组元素向上取整:", ceil_array)

# 截断
trunc_array = np.trunc(my_array)
print("数组元素截断:", trunc_array)
30. 数组元素比较使用 np.equal()、np.not_equal()、np.greater()、np.less()、np.greater_equal() 或 np.less_equal() 进行元素级别的比较操作。使用方式：import numpy as np

# 创建数组
array1 = np.array([1, 2, 3])
array2 = np.array([2, 2, 3])

# 数组元素相等比较
equal_result = np.equal(array1, array2)
print("数组元素相等比较:", equal_result)

# 数组元素不等比较
not_equal_result = np.not_equal(array1, array2)
print("数组元素不等比较:", not_equal_result)

# 数组元素大于比较
greater_result = np.greater(array1, array2)
print("数组元素大于比较:", greater_result)

# 数组元素小于比较
less_result = np.less(array1, array2)
print("数组元素小于比较:", less_result)

# 数组元素大于等于比较
greater_equal_result = np.greater_equal(array1, array2)
print("数组元素大于等于比较:", greater_equal_result)

# 数组元素小于等于比较
less_equal_result = np.less_equal(array1, array2)
print("数组元素小于等于比较:", less_equal_result)
31. 数组逻辑操作使用 np.logical_and()、np.logical_or()、np.logical_xor() 或 np.logical_not() 进行逻辑操作。使用方式：import numpy as np

# 创建数组
array1 = np.array([True, False, True])
array2 = np.array([False, False, True])

# 逻辑与操作
and_result = np.logical_and(array1, array2)
print("逻辑与操作:", and_result)

# 逻辑或操作
or_result = np.logical_or(array1, array2)
print("逻辑或操作:", or_result)

# 逻辑异或操作
xor_result = np.logical_xor(array1, array2)
print("逻辑异或操作:", xor_result)

# 逻辑非操作
not_result = np.logical_not(array1)
print("逻辑非操作:", not_result)
32. 数组元素求和累积使用 np.cumsum() 或 np.cumprod() 对数组元素进行求和或累积操作。使用方式：import numpy as np

# 创建数组
my_array = np.array([1, 2, 3, 4, 5])

# 对数组元素进行求和
cumsum_array = np.cumsum(my_array)
print("数组元素求和累积:", cumsum_array)

# 对数组元素进行累积
cumprod_array = np.cumprod(my_array)
print("数组元素求积累积:", cumprod_array)
33. 数组求幂使用 np.power() 对数组进行幂运算。使用方式：import numpy as np

# 创建数组
my_array = np.array([1, 2, 3, 4, 5])

# 对数组进行幂运算
power_array = np.power(my_array, 2)
print("数组元素求幂:", power_array)
34. 数组逆运算使用 np.reciprocal() 对数组进行逆运算。使用方式：import numpy as np

# 创建数组
my_array = np.array([1, 2, 3, 4, 5])

# 对数组进行逆运算
reciprocal_array = np.reciprocal(my_array)
print("数组逆运算:", reciprocal_array)
35. 数组对数运算使用 np.log()、np.log10() 或 np.log2() 对数组进行对数运算。使用方式：import numpy as np

# 创建数组
my_array = np.array([1, 10, 100])

# 对数组进行自然对数运算
log_array = np.log(my_array)
print("自然对数运算:", log_array)

# 对数组进行以10为底的对数运算
log10_array = np.log10(my_array)
print("以10为底的对数运算:", log10_array)

# 对数组进行以2为底的对数运算
log2_array = np.log2(my_array)
print("以2为底的对数运算:", log2_array)
36. 数组三角函数使用 np.sin()、np.cos()、np.tan()、np.arcsin()、np.arccos()、np.arctan() 对数组进行三角函数运算。使用方式：import numpy as np

# 创建数组
my_array = np.array([0, 30, 45, 60, 90])

# 对数组进行三角函数运算
sin_array = np.sin(np.deg2rad(my_array))  # 将角度转换为弧度
print("正弦值:", sin_array)

cos_array = np.cos(np.deg2rad(my_array))  # 将角度转换为弧度
print("余弦值:", cos_array)

tan_array = np.tan(np.deg2rad(my_array))  # 将角度转换为弧度
print("正切值:", tan_array)

arcsin_array = np.rad2deg(np.arcsin(my_array))
print("反正弦值:", arcsin_array)

arccos_array = np.rad2deg(np.arccos(my_array))
print("反余弦值:", arccos_array)

arctan_array = np.rad2deg(np.arctan(my_array))
print("反正切值:", arctan_array)
37. 数组指数函数使用 np.exp() 或 np.exp2() 对数组进行指数函数运算。使用方式：import numpy as np

# 创建数组
my_array = np.array([1, 2, 3])

# 对数组进行自然指数函数运算
exp_array = np.exp(my_array)
print("自然指数函数:", exp_array)

# 对数组进行以2为底的指数函数运算
exp2_array = np.exp2(my_array)
print("以2为底的指数函数:", exp2_array)
38. 数组双曲函数使用 np.sinh()、np.cosh()、np.tanh()、np.arcsinh()、np.arccosh()、np.arctanh() 对数组进行双曲函数运算。使用方式：import numpy as np

# 创建数组
my_array = np.array([0, 1, 2])

# 对数组进行双曲函数运算
sinh_array = np.sinh(my_array)
print("双曲正弦值:", sinh_array)

cosh_array = np.cosh(my_array)


print("双曲余弦值:", cosh_array)

tanh_array = np.tanh(my_array)
print("双曲正切值:", tanh_array)

arcsinh_array = np.arcsinh(my_array)
print("反双曲正弦值:", arcsinh_array)

arccosh_array = np.arccosh(my_array + 1)  # 避免出现无效值
print("反双曲余弦值:", arccosh_array)

arctanh_array = np.arctanh(my_array)
print("反双曲正切值:", arctanh_array)
39. 数组线性代数运算使用 np.dot()、np.linalg.inv()、np.linalg.det()、np.linalg.eigvals()、np.linalg.solve() 对数组进行线性代数运算。使用方式：import numpy as np

# 创建数组
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

# 数组的点积运算
dot_product = np.dot(array1, array2)
print("数组的点积运算:\n", dot_product)

# 数组的逆运算
inv_array = np.linalg.inv(array1)
print("数组的逆运算:\n", inv_array)

# 数组的行列式
det_array = np.linalg.det(array1)
print("数组的行列式:", det_array)

# 数组的特征值
eigvals_array = np.linalg.eigvals(array1)
print("数组的特征值:", eigvals_array)

# 数组的线性方程组求解
b = np.array([5, 7])
solve_array = np.linalg.solve(array1, b)
print("线性方程组的解:", solve_array)
40. 数组角度转换使用 np.degrees() 或 np.radians() 将角度与弧度进行转换。使用方式：import numpy as np

# 创建数组
radians_array = np.array([0, np.pi / 2, np.pi])

# 将弧度转换为角度
degrees_array = np.degrees(radians_array)
print("弧度转角度:", degrees_array)

# 将角度转换为弧度
radians_array = np.radians(degrees_array)
print("角度转弧度:", radians_array)
41. 数组排序使用 np.sort() 对数组进行排序。使用方式：import numpy as np

# 创建数组
my_array = np.array([3, 1, 2, 5, 4])

# 对数组进行排序
sorted_array = np.sort(my_array)
print("排序后的数组:", sorted_array)
42. 数组去重使用 np.unique() 对数组进行去重。使用方式：import numpy as np

# 创建数组
my_array = np.array([1, 2, 2, 3, 3, 4, 5, 5])

# 对数组进行去重
unique_array = np.unique(my_array)
print("去重后的数组:", unique_array)
43. 数组拼接使用 np.concatenate() 对数组进行拼接。使用方式：import numpy as np

# 创建数组
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# 对数组进行拼接
concatenated_array = np.concatenate((array1, array2))
print("拼接后的数组:", concatenated_array)
44. 数组复制使用 np.copy() 或 np.ndarray.copy() 复制数组。使用方式：import numpy as np

# 创建数组
original_array = np.array([1, 2, 3])

# 使用np.copy()函数复制数组
copied_array1 = np.copy(original_array)
print("使用np.copy()函数复制的数组:", copied_array1)

# 使用np.ndarray.copy()方法复制数组
copied_array2 = original_array.copy()
print("使用np.ndarray.copy()方法复制的数组:", copied_array2)
45. 数组填充使用 np.full() 或 np.fill() 对数组进行填充。使用方式：import numpy as np

# 创建数组
my_array = np.empty((2, 3))

# 使用np.full()函数填充数组
filled_array1 = np.full_like(my_array, 5)
print("使用np.full()函数填充的数组:", filled_array1)

# 使用np.fill()方法填充数组
my_array.fill(5)
print("使用np.fill()方法填充的数组:", my_array)
46. 数组插入使用 np.insert() 或 np.append() 对数组进行插入操作。使用方式：import numpy as np

# 创建数组
my_array = np.array([1, 2, 3, 4, 5])

# 在指定位置插入元素
inserted_array = np.insert(my_array, 2, [6, 7])
print("插入元素后的数组:", inserted_array)

# 在末尾追加元素
appended_array = np.append(my_array, [6, 7])
print("追加元素后的数组:", appended_array)
47. 数组删除使用 np.delete() 对数组进行删除操作。使用方式：import numpy as np

# 创建数组
my_array = np.array([1, 2, 3, 4, 5])

# 删除指定位置的元素
deleted_array = np.delete(my_array, 2)
print("删除元素后的数组:", deleted_array)
48. 数组元素累积求和使用 np.cumsum() 对数组元素进行累积求和。使用方式：import numpy as np

# 创建数组
my_array = np.array([1, 2, 3, 4, 5])

# 对数组元素进行累积求和
cumsum_array = np.cumsum(my_array)
print("数组元素累积求和:", cumsum_array)
49. 数组元素累积求积使用 np.cumprod() 对数组元素进行累积求积。使用方式：import numpy as np

# 创建数组
my_array = np.array([1, 2, 3, 4, 5])

# 对数组元素进行累积求积
cumprod_array = np.cumprod(my_array)
print("数组元素累积求积:", cumprod_array)
50. 数组元素累积比较使用 np.cummax() 或 np.cummin() 对数组元素进行累积比较。使用方式：import numpy as np

# 创建数组
my_array = np.array([3, 1, 4, 1, 5, 9])

# 对数组元素进行累积最大值比较
cummax_array = np.cummax(my_array)
print("数组元素累积最大值:", cummax_array)

# 对数组元素进行累积最小值比较
cummin_array = np.cummin(my_array)
print("数组元素累积最小值:", cummin_array)