# Module 11: Functions & Organization
# Duration: 6 minutes | Time: 1:26-1:32

# 🔨 Live Coding - Calculator v3.0

# TODO: Create basic math functions
def add(x, y):


def subtract(x, y):


def multiply(x, y):


def divide(x, y):
    # TODO: Handle division by zero
    if y != 0:

    return "Error: Division by zero!"

# TODO: Create function to get operation function
def get_operation_function(op):
    """Return the appropriate function for the operation"""
    operations = {
        "+": ,
        "-": ,
        "*": ,
        "/":
    }
    return operations.get(op, None)

# TODO: Create function to get two numbers from user
def get_two_numbers():


# Example usage:
# TODO: Use the functions
num1, num2 = get_two_numbers()
operation = "+"
func = get_operation_function(operation)
if func:
    result = func(num1, num2)
    print(f"{num1} {operation} {num2} = {result}")

# ⚡ Quick Exercise (1 min):
# 1. Create power() and modulo() functions
# 2. Add them to the operations dictionary
# 3. Test your new functions