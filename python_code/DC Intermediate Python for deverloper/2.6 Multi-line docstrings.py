# Exercise
# Multi-line docstrings
# Sometimes single-line docstrings are sufficient, but if your function is more complex or has several arguments, then it is generally a better choice to include a multi-line docstring.

# You'll practice this by creating a multi-line docstring for the convert_data_structure function you made earlier.

# Add a summary to the docstring: Convert a data structure to a list, tuple, or set..
# Add Args:, first with data (list, tuple, or set): A data structure to be converted., and second with data_type (str): String representing the type of structure to convert data to.
# Detail the Returns: section: data (list, tuple, or set): Converted data structure.


# Create the convert_data_type function
def convert_data_structure(data, data_type="list"):
  # Add a multi-line docstring
  """
  Convert a data structure to a list, tuple, or set.
  
  Args:
  	data (list, tuple, or set): A data structure to be converted.
    data_type (str): String representing the type of structure to convert data to.
    
  Returns:
  	data (list, tuple, or set): Converted data structure.
  """
  if data_type == "tuple":
    data = tuple(data)
  elif data_type == "set":
    data = set(data)
  else:
    data = list(data)
  return data

print(help(convert_data_structure))