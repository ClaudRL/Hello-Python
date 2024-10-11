# Exercise
# Calculating on a pivot table
# Pivot tables are filled with summary statistics, but they are only a first step to finding something insightful. Often you'll need to perform further calculations on them. A common thing to do is to find the rows or columns where the highest or lowest value occurs.

# Recall from Chapter 1 that you can easily subset a Series or DataFrame to find rows of interest using a logical condition inside of square brackets. For example: series[series > value].

# pandas is loaded as pd and the DataFrame temp_by_country_city_vs_year is available. The .head() for this DataFrame is shown below, with only a few of the year columns displayed:

# country	city	2000	2001	2002	…	2013
# Afghanistan	Kabul	15.823	15.848	15.715	…	16.206
# Angola	Luanda	24.410	24.427	24.791	…	24.554
# Australia	Melbourne	14.320	14.180	14.076	…	14.742
# Sydney	17.567	17.854	17.734	…	18.090
# Bangladesh	Dhaka	25.905	25.931	26.095	…	26.587
# Instructions
# 100 XP
# Calculate the mean temperature for each year, assigning to mean_temp_by_year.
# Filter mean_temp_by_year for the year that had the highest mean temperature.
# Calculate the mean temperature for each city (across columns), assigning to mean_temp_by_city.
# Filter mean_temp_by_city for the city that had the lowest mean temperature.

# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean(axis = "index")

# Filter for the year that had the highest mean temp
# print(mean_temp_by_year[mean_temp_by_year.idxmax()])
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis = "columns")

# Filter for the city that had the lowest mean temp
# print(mean_temp_by_city[mean_temp_by_city.idxmin()])
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])