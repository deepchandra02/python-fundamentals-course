# Module 12: Error Handling & Polish
# 🔨 Live Coding - Calculator v4.0

# TODO: Create safe input function with error handling
def safe_float_input(prompt):
    while True:
        try:
            # TODO: Get input and convert to float

        except ValueError:
            print("❌ Please enter a valid number!")

# TODO: Create safe operation input function
def safe_operation_input():
    valid_ops = {"+", "-", "*", "/", "**", "%"}
    while True:
        op = input("Operation (+,-,*,/,**,%): ")
        # TODO: Check if operation is valid
        if op in valid_ops:

        print(f"❌ Invalid! Use: {', '.join(valid_ops)}")

# TODO: Example of handling different errors
def safe_divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "❌ Cannot divide by zero!"
    except TypeError:
        return "❌ Invalid number types!"

# Safe calculator usage example:
try:
    print("🧮 Safe Calculator")
    # TODO: Use safe input functions
    num1 =
    op =
    num2 =

    # Perform calculation
    result = safe_divide(num1, num2) if op == "/" else "Other operations..."
    print(f"Result: {result}")

except KeyboardInterrupt:
    print("\n👋 Calculator closed safely!")

# ⚡ Quick Exercise:
# 1. Test the safe input with invalid entries
# 2. Try pressing Ctrl+C during input
# 3. Add validation for negative numbers in square root