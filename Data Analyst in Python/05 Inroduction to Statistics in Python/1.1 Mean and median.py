# Exercise
# Mean and median
# In this chapter, you'll be working with the food_consumption dataset from 2018 Food Carbon Footprint Index by nu3. The food_consumption dataset contains the number of kilograms of food consumed per person per year in each country and food category (consumption), and its carbon footprint (co2_emissions) measured in kilograms of carbon dioxide, or CO2.

# In this exercise, you'll compute measures of center to compare food consumption in the US and Belgium using your pandas and numpy skills.

# pandas is imported as pd for you and food_consumption is pre-loaded.

# Instructions
# 100 XP
# Import numpy with the alias np.
# Subset food_consumption to get the rows where the country is 'USA'.
# Calculate the mean of food consumption in the usa_consumption DataFrame, which is already created for you.
# Calculate the median of food consumption in the usa_consumption DataFrame.

# Import numpy with alias np
import numpy as np

# Subset country for USA: usa_consumption
usa_consumption = food_consumption[food_consumption['country'] == 'USA']
# print(usa_consumption)
# Calculate mean consumption in USA
print(np.mean(usa_consumption['consumption']))

# Calculate median consumption in USA
print(np.median(usa_consumption['consumption']))


# Calculate mode consumption in USA
print("mode = ",usa_consumption['consumption'].mode)