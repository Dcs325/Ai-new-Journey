# First, ask the user for their name.
user_name = input("What is your name friend? ")

# Define the special name we're looking for.
# We'll use 'Gemini' for this example, but you can change it!
special_name = "Great One"

# --- Introducing the if/else logic ---

# Check if the entered name matches our special name (case-sensitive for now).
if user_name == special_name:
    # This block runs ONLY IF the condition (user_name is 'Gemini') is True.
    print(f"Hey, it's the awesome AI Director, {user_name}! Welcome back to the code world! you should never have left")
else:
    # This block runs if the 'if' condition was False (i.e., the name is NOT 'Gemini').
    print(f"Hello, {user_name}! Welcome to the world of Python programming! take your shoes off stay awhile")

print("It was great interacting with you! hury up and come back please :0)")
