# Exercise
# Finding outliers using IQR
# Outliers can have big effects on statistics like mean, as well as statistics that rely on the mean, such as variance and standard deviation. Interquartile range, or IQR, is another way of measuring spread that's less influenced by outliers. IQR is also often used to find outliers. If a value is less than 
#  or greater than 
# , it's considered an outlier. In fact, this is how the lengths of the whiskers in a matplotlib box plot are calculated.

# Diagram of a box plot showing median, quartiles, and outliers

# In this exercise, you'll calculate IQR and use it to find some outliers. pandas as pd and numpy as np are loaded and food_consumption is available.

# 1. Calculate the total co2_emission per country by grouping by country and taking the sum of co2_emission. Store the resulting DataFrame as emissions_by_country.

