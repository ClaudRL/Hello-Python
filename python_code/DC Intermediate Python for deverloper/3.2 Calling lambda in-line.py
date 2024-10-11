# Exercise
# Calling lambda in-line
# Remember, one of the key benefits of lambda is the ability to use functions in-line.

# In this exercise, you'll modify the approach of the previous exercise to add tax to the sales_price variable in-line without storing a lambda function as a variable first.

# Instructions
# 100 XP
# # In a single line of code, make a lambda function that multiplies sale_price by 1.2 and returns the results.

sale_price = 29.99

# Call a lambda function adding 20% to sale_price
print((lambda x : x * 1.2)(sale_price))