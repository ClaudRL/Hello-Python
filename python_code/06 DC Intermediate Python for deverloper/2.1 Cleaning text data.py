# Exercise
# Cleaning text data
# In the video, you saw how to build a custom function that performs a calculation and rounds the results. However, custom functions can be used for any task we expect to repeat! One common example is cleaning text data so that it conforms to specific requirements.

# In this exercise, you'll create a function that takes string data and:

# Replaces spaces with underscores
# Converts to lowercase
# Returns the formatted string
# Instructions
# 100 XP
# Define a function called clean_string, which takes an argument called text.
# Inside the function, create a variable called no_spaces, which contains the text with spaces replaced by underscores.
# Inside the function, create a variable called clean_text, which converts characters in no_spaces to lowercase.
# Finish the function by producing clean_text as an output.

# Create the clean_string function
def clean_string(text):
  
  # Replace spaces with underscores
  no_spaces = text.replace(" ", "_")
  
  # Convert to lowercase
  clean_text = no_spaces.lower()
  
  # Return the final text as an output
  return clean_text

converted_text = clean_string("I LoVe dATaCamP!")
print(converted_text)