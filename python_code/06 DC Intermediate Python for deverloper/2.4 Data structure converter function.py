# Exercise
# Data structure converter function
# Now you've learned about the types of arguments in functions, you'll put this into practice by building a custom function that converts data into different structures.

# Instructions
# 100 XP
# Define convert_data_structure with two arguments: data and data_type, where the latter has a default value of "list".
# Add a condition to check if data_type is "tuple".
# Else if data_type is "set", convert data into a set, saving it as a variable of the same name.
# Call the function on the data structure provided, using an appropriate keyword argument value-pair to convert it to a set.

# Create the convert_data_structure function
def convert_data_structure(data, data_type = "list"):
  
  # If data_type is "tuple"
  if data_type == "tuple":
    data = tuple(data)
  
  # Else if data_type is set, convert to a set
  elif data_type == "set":
    data = set(data)
  else:
    data = list(data)
  return data

# Call the function to convert to a set
convert_data_structure({"a", 1, "b", 2, "c", 3}, data_type="set")