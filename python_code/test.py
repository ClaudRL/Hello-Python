import numpy as np

# 设置随机种子为10
np.random.seed(10)

# 生成一组随机数
random_numbers = np.random.randint(0, 100, size=5)
print(random_numbers)

# Set random seed
np.random.seed(24)

# Sample 5 deals without replacement
sample_without_replacement = amir_deals.sample(5, replace = False)
print(sample_without_replacement)

# 2. Take a sample of 5 deals with replacement and save as sample_with_replacement.
# Set random seed
np.random.seed(24)

# Sample 5 deals with replacement
sample_with_replacement = amir_deals.sample(5, replace = True)
print(sample_with_replacement)
