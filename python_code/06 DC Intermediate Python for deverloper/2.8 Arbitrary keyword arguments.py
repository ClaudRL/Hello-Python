# Exercise
# Arbitrary keyword arguments
# Arbitrary positional arguments are one way to add flexibility when creating custom functions, but you can also use arbitrary keyword arguments.

# Your goal is to take the concat function that you created in the last exercise and modify it to accept arbitrary keyword arguments. Good luck!

# Instructions
# 100 XP
# Define concat() as a function that accepts arbitrary keyword arguments called kwargs.
# Inside the function, create an empty string.
# Inside the function, loop over the keyword argument values, using kwarg as the iterator.
# Call concat() with keyword arguments of start equal to "Python", middle equal to "is", and end equal to "great!".

# Define a function called concat
def concat(**kwarg):
  
  # Create an empty string
  result = ""
  
  # Iterate over the Python kwargs
  for kwarg in kwarg.values():
    result += " " + kwarg
  return result 

# Call the function
print(concat(start="Python", middle="is", end="great!"))


# **kwargs（关键字参数）：适用于可选的食材、配料、或烹饪温度、时间等可能不统一的参数。

# 示例：
def add_recipe(name, **details):
    print(f"Recipe: {name}")
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")

add_recipe("Pasta", ingredients="Pasta, Water, Salt", cooking_time="10 minutes", temperature="Medium")
