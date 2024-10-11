# Exercise
# Avoiding errors
# In the video, you saw a couple of approaches for error handling that can be applied to custom functions.

# In this exercise, you'll test out one of the approaches that avoids raising an error, printing a helpful message if an error occurs, but not terminating the script.

# Instructions
# 100 XP
# Use a keyword allowing you to attempt to run code that cleans text.
# Swap a space for a single underscore in the text argument.
# Use another keyword that prints a helpful message if an error occurs when calling the snake_case() function.

def snake_case(text):
  # Attempt to clean the text
  try:
    # Swap spaces for underscores
    clean_text = ____.____("____", "____")
    clean_text = clean_text.lower()
  # Run this code if an error occurs
  except:
    print("The snake_case() function expects a string as an argument, please check the data type provided.")
    
snake_case("User Name 187")

#修复后
def snake_case(text):
  # Attempt to clean the text
  try:
    # Swap spaces for underscores
    clean_text = text.replace(" ", "_")
    clean_text = clean_text.lower()
    print(clean_text)
  # Run this code if an error occurs
  except:
    print("The snake_case() function expects a string as an argument, please check the data type provided.")
    
snake_case("User Name 187")