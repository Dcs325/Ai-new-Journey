# This script prints a personalized welcome message.

def print_welcome_message(name):
  """
  Prints a welcome message tailored to the provided name.

  Args:
    name: A string representing the name of the person to welcome.
  """
  print(f"Welcome, {name}! this is the beginning of your coding journey.")

# --- How to use the script ---

# 1. Call the function with your desired name:
print_welcome_message("Daniel")

# 2. You can also get input from the user:
# user_name = input("Enter your name: ")
# print_welcome_message(user_name)

# Example with a different name
print_welcome_message("Everyone")