# Exercise
# Exercise
# Adding a keyword argument
# Previously, you developed a custom function to clean text, as shown here:

# # Create the clean_string function
# def clean_string(text):

#       # Replace spaces with underscores
#       no_spaces = text.replace(" ", "_")

#       # Convert to lowercase
#       clean_text = no_spaces.lower()

#       # Display the final text as an output
#       return clean_text
# Now, you will modify it to take different default keyword arguments!
 
# Define clean_text, which has two arguments: text, and lower, with the latter having a default value of True.
# Define clean_text
def clean_text(text, lower = True):
  if lower == False:
    clean_text = text.replace(" ", "_")
    return clean_text
  else:
    clean_text = text.replace(" ", "_")
    clean_text = clean_text.lower()
    return clean_text

# Re-define clean_text with arguments of text followed by remove, with the latter having a default value of None.

# Define clean_text
def clean_text(text, remove = None):
  if remove != None:
    clean_text = text.replace(remove, "")
    clean_text = clean_text.lower()
    return clean_text
  else:
    clean_text = text.lower()
    return clean_text



