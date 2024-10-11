# Exercise
# Lambda functions with iterables
# You've used lambda functions to perform actions on a single value; now it's time to test yourself on working with iterables.

# You've been provided with a list called sales_prices containing sales prices for several items. Your goal is to use a lambda function to add tax (20%) to each value in the list.

# Instructions
# 100 XP
# Create add_taxes, which multiplies each value in sales_prices by 20%.
# Print a list using add_taxes to update values in sales_prices.

sales_prices = [29.99, 9.95, 14.50, 39.75, 60.00]

# Create add_taxes to add 20% to each item in sales_prices
# Apply a lambda function inside map()
add_taxes = map(lambda x: x * 1.2, sales_prices)

# Use add_taxes to return a new list with updated values
print(list(add_taxes))