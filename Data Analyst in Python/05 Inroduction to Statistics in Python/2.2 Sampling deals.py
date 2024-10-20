# Exercise
# Sampling deals
# In the previous exercise, you counted the deals Amir worked on. Now it's time to randomly pick five deals so that you can reach out to each customer and ask if they were satisfied with the service they received. You'll try doing this both with and without replacement.

# Additionally, you want to make sure this is done randomly and that it can be reproduced in case you get asked how you chose the deals, so you'll need to set the random seed before sampling from the deals.

# Both pandas as pd and numpy as np are loaded and amir_deals is available.

# 1. Set the random seed to 24.
# Take a sample of 5 deals without replacement and store them as sample_without_replacement.
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

