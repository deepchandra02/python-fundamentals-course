# Module 8: Dictionaries & Settings
# Duration: 6 minutes | Time: 1:10-1:16

# 🔨 Live Coding - Calculator v2.2

# TODO: Create user settings dictionary
user_settings = {
    "username": ,
    "decimal_places": ,
    "show_steps": ,
    "favorite_operation":
}

# TODO: Create operations dictionary for lookups
operations = {
    "+": ,
    "-": ,
    "*": ,
    "/":
}

# TODO: Print personalized welcome message using dictionary values
print(f"👋 Welcome back, !")
print(f"🔧 Decimal places: !")

# TODO: Access operations by key
selected_op = "+"
print(f"Performing {operations[selected_op]}")

# Example: Using dictionary to store operation functions (advanced)
def add(x, y): return x + y
def subtract(x, y): return x - y

operation_functions = {
    "+": add,
    "-": subtract
}

# TODO: Use the dictionary to call functions
result = operation_functions["+"](10, 5)
print(f"Function result: {result}")

# ⚡ Quick Exercise (1 min):
# 1. Add more settings to user_settings
# 2. Add multiplication and division to operations
# 3. Try accessing a key that doesn't exist (what happens?)