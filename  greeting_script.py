# First, ask the user for their name using the input() function.
# The text inside input() is the prompt shown to the user.
user_name = input("What is your name? ")

# Now, 'user_name' is a variable that holds whatever the user typed.
# You can now use this variable in your greeting.

# Finally, print a greeting that uses the 'user_name' variable.
# We're using an f-string (formatted string literal) here, which is a clean way to
# embed variables directly into strings in Python.
print(f"Hello, {user_name}! Welcome to the world of Python programming!")

# You could also do it with string concatenation (older method):
# print("Hello, " + user_name + "! Welcome to the world of Python programming!")