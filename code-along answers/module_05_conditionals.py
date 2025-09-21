# Module 5: Smart Decisions
# 🔨 Live Coding - Calculator v1.0

print("🧮 Smart Calculator v1.0")

# TODO: Get user inputs
num1 = float(input("First number: "))
operation = input("Operation (+, -, *, /, **): ")
num2 = float(input("Second number: "))

# TODO: Use if/elif/else to handle different operations
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "❌ Error: Can't divide by zero!"
elif operation == "**":
    result = num1**num2
else:
    result = "❌ Invalid operation!"

# TODO: Print the result
print(f"🎯 Result: {result}")

# ⚡ Quick Exercise:
# 1. Test all operations including error cases
# 2. Try dividing by zero
# 3. Try entering an invalid operation like "#"
# 4. Add support for modulo operation (%)
