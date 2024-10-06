# Exercise
# Sorting rows
# Finding interesting bits of data in a DataFrame is often easier if you change the order of the rows. You can sort the rows by passing a column name to .sort_values().

# In cases where rows have the same value (this is common if you sort on a categorical variable), you may wish to break the ties by sorting on another column. You can sort on multiple columns in this way by passing a list of column names.

# Sort on …	Syntax
# one column	df.sort_values("breed")
# multiple columns	df.sort_values(["breed", "weight_kg"])
# By combining .sort_values() with .head(), you can answer questions in the form, "What are the top cases where…?".

# homelessness is available and pandas is loaded as pd.


# 1. Sort homelessness by the number of homeless individuals in the individuals column, from smallest to largest, and save this as homelessness_ind.
# Print the head of the sorted DataFrame.

# Sort homelessness by descending family members
# Sort homelessness by individuals
homelessness_ind = homelessness.sort_values("individuals")

# Print the top few rows
print(homelessness_ind.head())