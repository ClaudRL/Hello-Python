# The CLT in action
# The central limit theorem states that a sampling distribution of a sample statistic approaches the normal distribution as you take more samples, no matter the original distribution being sampled from.

# In this exercise, you'll focus on the sample mean and see the central limit theorem in action while examining the num_users column of amir_deals more closely, which contains the number of people who intend to use the product Amir is selling.

# pandas as pd, numpy as np, and matplotlib.pyplot as plt are loaded and amir_deals is available.

# 1. Create a histogram of the num_users column of amir_deals and show the plot.
# Create a histogram of num_users and show
amir_deals['num_users'].hist()
plt.show()
#-------------------------------------------
# Yes, both `amir_deals['num_users'].hist()` and `amir_deals.hist(['num_users'])` will generate a histogram, but there are subtle differences in how each works:

# 1. **`amir_deals['num_users'].hist()`**:
#    - This syntax directly accesses the **Series** (`num_users`) within the DataFrame `amir_deals` and calls the `.hist()` method on that Series.
#    - As a result, it creates a histogram specifically for this single column.
#    - Since it operates on a Series, it provides additional options directly related to single-column data plotting.

# 2. **`amir_deals.hist(['num_users'])`**:
#    - This syntax calls `.hist()` on the entire **DataFrame** (`amir_deals`), but specifies only the `num_users` column to plot by passing it in a list.
#    - Using this method on a DataFrame allows for more flexibility if you later want to plot multiple columns at once (e.g., `amir_deals.hist(['num_users', 'other_column'])`).
#    - This command provides an interface suitable for plotting multiple histograms side-by-side if desired.

# ### When to Use Which
# - Use `amir_deals['num_users'].hist()` if you’re plotting only a single Series and prefer simplicity.
# - Use `amir_deals.hist(['num_users'])` if there’s a possibility you’ll need to plot multiple columns, as it’s more flexible for handling multiple histograms in a single call. 

# In general, for a single histogram, both are effective; the choice depends on whether you want a Series-specific or DataFrame-wide approach.
#-------------------------------------------
# 2. Set the seed to 104.
# Take a sample of size 20 with replacement from the num_users column of amir_deals, and take the mean.

# Set seed to 104
np.random.seed(104)

# Sample 20 num_users with replacement from amir_deals
samp_20 = amir_deals['num_users'].sample(20, replace = True   )

# Take mean of samp_20
print(np.mean(samp_20))

# 3.  Repeat this 100 times using a for loop and store as sample_means. This will take 100 different samples and calculate the mean of each.
