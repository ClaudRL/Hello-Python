# Exercise
# Building a password checker
# You've seen how conditional statements can be used to check for equality. Now you have the skills to build a custom function, you'll combine these two techniques to build a function called password_checker that compares a user's password to a submission, conditionally printing an output depending on the results.

# Instructions
# 100 XP
# Define the password_checker function, which should accept one argument called submission.
# Check if password is equal to submission.
# Add a keyword enabling the conditional printing of "Incorrect password" if password and submission are different.
# Call the function, passing "NOT_VERY_SECURE_2023".

password = "not_very_secure_2023"

# Define the password_checker function
def password_checker(submission):
  
  # Check that the password variable and the submission match
  if password == submission:
    print("Successful login!")
  
  # Otherwise, print "Incorrect password"
  else:
    print("Incorrect password")

# Call the function    
password_checker("not_very_secure_2023")