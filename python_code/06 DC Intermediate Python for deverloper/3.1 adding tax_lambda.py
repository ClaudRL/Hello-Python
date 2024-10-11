# Exercise
# Adding tax
# Time to test out your lambda function skills!

# In this exercise, you'll use a lambda function to add a tax of 20% to the cost of the sale_price variable.

# Instructions
# 100 XP
# Define the add_tax lambda function to multiply the argument provided to it, x, by 1.2.
# Call add_tax() on the sale_price variable.

sale_price = 29.99

# Define a lambda function called add_tax
add_tax = lambda x: x * 1.2

# Call the lambda function
print(add_tax(sale_price))