# Exercise
# Adding arbitrary arguments
# In the video, you saw that Python allows custom functions to accept any number of positional arguments through the use of "Arbitrary arguments". This flexibility enables functions to be used in a variety of ways while still producing the expected results!

# Using this power, you'll build a function that concatenates (joins together) strings, regardless of how many blocks of text are provided!

# Instructions
# 100 XP
# Define a function called concat() that accepts arbitrary arguments called args.
# Create a variable called result and assign an empty string to it.
# Use a for loop to iterate over each arg in args.
# Call the function to test that it works correctly.

# Define a function called concat
def concat(*args):

  # Create an empty string
  result = ""
  
  # Iterate over the Python args tuple
  for arg in args:
    result += " " + arg
  return result

# Call the function
print(concat("Python", "is", "great!"))

# *args（位置参数）：适用于烹饪步骤等不确定数量的内容。每道菜可能包含不同数量的烹饪步骤，使用 *args 可以灵活传递这些步骤。

# 示例：
def add_recipe(name, *steps):
    print(f"Recipe: {name}")
    print("Cooking steps:")
    for step in steps:
        print(f"- {step}")

add_recipe("Pasta", "Boil water", "Add pasta", "Cook for 10 minutes", "Drain and serve")