# Exercise
# Quartiles, quantiles, and quintiles
# Quantiles are a great way of summarizing numerical data since they can be used to measure center and spread, as well as to get a sense of where a data point stands in relation to the rest of the data set. For example, you might want to give a discount to the 10% most active users on a website.

# In this exercise, you'll calculate quartiles, quintiles, and deciles, which split up a dataset into 4, 5, and 10 pieces, respectively.

# Both pandas as pd and numpy as np are loaded and food_consumption is available.

# 1. Calculate the quartiles of the co2_emission column of food_consumption.

# Calculate the quartiles of co2_emission
print(np.quantile(food_consumption['co2_emission'],[0, 0.25, 0.5, 0.75, 1]))

# 2. Calculate the six quantiles that split up the data into 5 pieces (quintiles) of the co2_emission column of food_consumption.

# Calculate the quintiles of co2_emission
print(np.quantile(food_consumption['co2_emission'],[0, 0.2, 0.4, 0.6, 0.8, 1]))

# 3. Calculate the eleven quantiles of co2_emission that split up the data into ten pieces (deciles).
# Calculate the deciles of co2_emission
print(np.quantile(food_consumption['co2_emission'],np.linspace(0,1,11)))
