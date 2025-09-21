"""
PYTHON CALCULATOR WORKSHOP

Workshop Plan:
- Start: Hello World (v0.1)
- End: Professional Scientific Calculator (v4.0)
"""

# ==========================================
# MODULE 1: HELLO PYTHON WORLD
# ==========================================

# TODO 1.1: Write your first print statement


# TODO 1.2: Add a welcome message for your calculator


# TODO 1.3: Add a comment explaining what this program does


# ==========================================
# MODULE 2: VARIABLES & NUMBERS (0:08-0:18)
# ==========================================

# TODO 2.1: Create calculator info variables
app_name = ""
version = 0.0
author = ""

# TODO 2.2: Print calculator info using f-strings


# TODO 2.3: Demo variables and math
a, b = 0, 0
demo_result = 0

# TODO 2.4: Print the demo calculation


# ==========================================
# MODULE 3: USER INPUT MAGIC (0:18-0:28)
# ==========================================


def basic_calculator_v03():
    """Calculator v0.3 - Interactive Input"""
    print("🧮 Interactive Calculator v0.3")

    # TODO 3.1: Get user input for numbers
    # num1 = float(input("Enter first number: "))
    # num2 = float(input("Enter second number: "))

    # TODO 3.2: Calculate and show result
    # result = num1 + num2
    # print(f"✨ {num1} + {num2} = {result}")

    pass  # Remove this when you add code


# ==========================================
# MODULE 4: OPERATION STATION (0:28-0:40)
# ==========================================


def multi_operation_calculator_v04():
    """Calculator v0.4 - Multiple Operations"""
    print("🧮 Multi-Operation Calculator v0.4")

    # TODO 4.1: Get two numbers from user
    # num1 = float(input("First number: "))
    # num2 = float(input("Second number: "))

    # TODO 4.2: Show all operations
    # print(f"➕ Addition: {num1} + {num2} = {num1 + num2}")
    # print(f"➖ Subtraction: {num1} - {num2} = {num1 - num2}")
    # print(f"✖️ Multiplication: {num1} * {num2} = {num1 * num2}")
    # print(f"➗ Division: {num1} / {num2} = {num1 / num2}")
    # print(f"🔥 Power: {num1} ** {num2} = {num1 ** num2}")

    # TODO 4.3: Add modulo operation (% operator)

    pass  # Remove this when you add code


# ==========================================
# MODULE 5: SMART DECISIONS (0:40-0:55)
# ==========================================


def smart_calculator_v10():
    """Calculator v1.0 - Operation Selection"""
    print("🧮 Smart Calculator v1.0")

    # TODO 5.1: Get user inputs
    # num1 = float(input("First number: "))
    # operation = input("Operation (+, -, *, /, **): ")
    # num2 = float(input("Second number: "))

    # TODO 5.2: Use if/elif/else for different operations
    # if operation == "+":
    #     result = num1 + num2
    # elif operation == "-":
    #     result = num1 - num2
    # elif operation == "*":
    #     result = num1 * num2
    # elif operation == "/":
    #     if num2 != 0:
    #         result = num1 / num2
    #     else:
    #         result = "❌ Error: Can't divide by zero!"
    # elif operation == "**":
    #     result = num1 ** num2
    # else:
    #     result = "❌ Invalid operation!"

    # TODO 5.3: Print the result
    # print(f"🎯 Result: {result}")

    pass  # Remove this when you add code


# ==========================================
# MODULE 6: LOOP POWER (0:55-1:03)
# ==========================================


def menu_calculator_v20():
    """Calculator v2.0 - Menu System with Loops"""
    print("🧮 Never-Ending Calculator v2.0")

    # TODO 6.1: Create infinite loop
    # while True:
    #     # TODO 6.2: Display menu
    #     print("\n🎯 CALCULATOR MENU")
    #     print("1️⃣ Basic Math")
    #     print("2️⃣ Exit")
    #
    #     choice = input("Choose (1-2): ")
    #
    #     # TODO 6.3: Handle menu choices
    #     if choice == "2":
    #         print("👋 Thanks for calculating!")
    #         break
    #     elif choice == "1":
    #         # TODO 6.4: Get numbers and operation
    #         num1 = float(input("First number: "))
    #         op = input("Operation (+,-,*,/): ")
    #         num2 = float(input("Second number: "))
    #
    #         # TODO 6.5: Calculate based on operation
    #         if op == "+": result = num1 + num2
    #         elif op == "-": result = num1 - num2
    #         elif op == "*": result = num1 * num2
    #         elif op == "/": result = num1 / num2 if num2 != 0 else "Error!"
    #
    #         print(f"✅ Result: {result}")
    #     else:
    #         print("❌ Invalid choice!")

    pass  # Remove this when you add code


# ==========================================
# MODULE 7: LISTS & HISTORY (1:03-1:10)
# ==========================================

# TODO 7.1: Create global history list
# history = []


# TODO 7.2: Function to add to history
def add_to_history(calc_string):
    """Add calculation to history"""
    # history.append(calc_string)
    pass


# TODO 7.3: Function to show history
def show_history():
    """Display calculation history"""
    # print("\n📋 CALCULATION HISTORY")
    # if history:
    #     for i, calc in enumerate(history, 1):
    #         print(f"{i}. {calc}")
    # else:
    #     print("No calculations yet!")
    pass


# ==========================================
# MODULE 8: DICTIONARIES & SETTINGS (1:10-1:16)
# ==========================================

# TODO 8.1: Create user settings dictionary
# user_settings = {
#     "username": "Guest",
#     "decimal_places": 2,
#     "show_steps": True,
#     "favorite_operation": "+"
# }

# TODO 8.2: Create operations lookup dictionary
# operations = {
#     "+": "Addition",
#     "-": "Subtraction",
#     "*": "Multiplication",
#     "/": "Division"
# }


def display_user_info():
    """Show personalized user information"""
    # print(f"👋 Welcome back, {user_settings['username']}!")
    # print(f"🔧 Decimal places: {user_settings['decimal_places']}")
    pass


# ==========================================
# MODULE 9: TUPLES & CONSTANTS (1:16-1:21)
# ==========================================

# TODO 9.1: Mathematical constants as tuples
# MATH_CONSTANTS = (3.14159, 2.71828, 1.41421)  # π, e, √2
# CONSTANT_NAMES = ("Pi", "Euler's e", "√2")


def display_constants():
    """Show mathematical constants"""
    # print("🔢 MATH CONSTANTS")
    # for i, (name, value) in enumerate(zip(CONSTANT_NAMES, MATH_CONSTANTS), 1):
    #     print(f"{i}. {name} = {value}")
    pass


# TODO 9.2: Coordinate examples
def distance_example():
    """Example using coordinate tuples"""
    # point1 = (10, 20)
    # point2 = (30, 40)
    # print(f"Distance calculation between {point1} and {point2}")
    pass


# ==========================================
# MODULE 10: SETS & UNIQUE OPERATIONS (1:21-1:26)
# ==========================================

# TODO 10.1: Track unique operations
# operations_used = set()
# available_operations = {"add", "subtract", "multiply", "divide", "power"}


def track_operation(operation_name):
    """Track which operations user has tried"""
    # operations_used.add(operation_name)
    # print(f"🎯 Operations you've tried: {operations_used}")
    # print(f"📝 Try these next: {available_operations - operations_used}")
    #
    # if len(operations_used) == len(available_operations):
    #     print("🏆 Calculator Master! You've tried everything!")
    pass


# ==========================================
# MODULE 11: FUNCTIONS & ORGANIZATION (1:26-1:32)
# ==========================================


# TODO 11.1: Basic math functions
def add(x, y):
    """Add two numbers"""
    # return x + y
    pass


def subtract(x, y):
    """Subtract two numbers"""
    # return x - y
    pass


def multiply(x, y):
    """Multiply two numbers"""
    # return x * y
    pass


def divide(x, y):
    """Divide two numbers with zero check"""
    # if y != 0:
    #     return x / y
    # return "Error: Division by zero!"
    pass


# TODO 11.2: Function to get operation function
def get_operation_function(op):
    """Return the appropriate function for the operation"""
    # operations = {
    #     "+": add,
    #     "-": subtract,
    #     "*": multiply,
    #     "/": divide
    # }
    # return operations.get(op, None)
    pass


# TODO 11.3: Input helper function
def get_two_numbers():
    """Get two numbers from user"""
    # num1 = float(input("First number: "))
    # num2 = float(input("Second number: "))
    # return num1, num2
    pass


# ==========================================
# MODULE 12: ERROR HANDLING & POLISH (1:32-1:38)
# ==========================================


# TODO 12.1: Safe input functions
def safe_float_input(prompt):
    """Get float input with error handling"""
    # while True:
    #     try:
    #         return float(input(prompt))
    #     except ValueError:
    #         print("❌ Please enter a valid number!")
    pass


def safe_operation_input():
    """Get valid operation with error handling"""
    # valid_ops = {"+", "-", "*", "/", "**", "%"}
    # while True:
    #     op = input("Operation (+,-,*,/,**,%): ")
    #     if op in valid_ops:
    #         return op
    #     print(f"❌ Invalid! Use: {', '.join(valid_ops)}")
    pass


# ==========================================
# MODULE 13: MODULES & ADVANCED FEATURES (1:38-1:44)
# ==========================================

# TODO 13.1: Import math module
# import math


def scientific_operations():
    """Advanced scientific calculator functions"""
    # print("🔬 SCIENTIFIC CALCULATOR")
    # operations = {
    #     "1": ("Square Root", lambda x: math.sqrt(x)),
    #     "2": ("Sine (degrees)", lambda x: math.sin(math.radians(x))),
    #     "3": ("Natural Log", lambda x: math.log(x)),
    #     "4": ("Power of e", lambda x: math.exp(x))
    # }
    #
    # for key, (name, _) in operations.items():
    #     print(f"{key}. {name}")
    #
    # choice = input("Choose (1-4): ")
    # if choice in operations:
    #     num = safe_float_input("Enter number: ")
    #     name, func = operations[choice]
    #     result = func(num)
    #     print(f"✨ {name}({num}) = {result:.4f}")
    pass


def calculate_bmi():
    """BMI Calculator"""
    # print("💪 BMI CALCULATOR")
    # weight = safe_float_input("Weight (kg): ")
    # height = safe_float_input("Height (m): ")
    # bmi = weight / (height ** 2)
    # print(f"BMI: {bmi:.1f}")
    #
    # if bmi < 18.5: print("Category: Underweight")
    # elif bmi < 25: print("Category: Normal weight")
    # elif bmi < 30: print("Category: Overweight")
    # else: print("Category: Obese")
    pass


def format_result(num1, op, num2, result):
    """Professional result formatting"""
    # return f"📊 {num1:,.2f} {op} {num2:,.2f} = {result:,.2f}"
    pass


# ==========================================
# MAIN CALCULATOR - FINAL VERSION
# ==========================================


def main_calculator():
    """
    🧮 ULTIMATE PYTHON CALCULATOR v4.0 🧮

    Complete calculator with all features:
    - Basic arithmetic operations
    - Menu system with loops
    - Calculation history
    - User settings
    - Error handling
    - Scientific functions
    - BMI calculator
    """

    print("=" * 50)
    print("    🧮 PYTHON CALCULATOR v4.0 🧮")
    print("=" * 50)

    # TODO: Integrate all features into main menu
    # while True:
    #     print("\n🎯 MAIN MENU")
    #     print("1️⃣ Basic Calculator")
    #     print("2️⃣ Scientific Calculator")
    #     print("3️⃣ BMI Calculator")
    #     print("4️⃣ Show History")
    #     print("5️⃣ Settings")
    #     print("6️⃣ Exit")
    #
    #     choice = input("Choose (1-6): ")
    #
    #     if choice == "6":
    #         print("👋 Thanks for using Python Calculator!")
    #         break
    #     elif choice == "1":
    #         # Basic calculator logic
    #         pass
    #     elif choice == "2":
    #         scientific_operations()
    #     elif choice == "3":
    #         calculate_bmi()
    #     elif choice == "4":
    #         show_history()
    #     elif choice == "5":
    #         display_user_info()
    #     else:
    #         print("❌ Invalid choice!")

    pass


# ==========================================
# WORKSHOP TESTING FUNCTIONS
# ==========================================


def test_module(module_number):
    """Test individual modules during workshop"""
    if module_number == 1:
        print("Testing Module 1: Hello World")
        # Call basic print statements

    elif module_number == 3:
        print("Testing Module 3: User Input")
        basic_calculator_v03()

    elif module_number == 4:
        print("Testing Module 4: Operations")
        multi_operation_calculator_v04()

    elif module_number == 5:
        print("Testing Module 5: Conditionals")
        smart_calculator_v10()

    elif module_number == 6:
        print("Testing Module 6: Loops")
        menu_calculator_v20()

    else:
        print("Module not implemented yet!")


# ==========================================
# MAIN EXECUTION
# ==========================================

if __name__ == "__main__":
    """
    🎯 WORKSHOP EXECUTION

    During the workshop, your instructor will guide you to:
    1. Uncomment sections as you learn each concept
    2. Fill in TODO items step by step
    3. Test each module individually
    4. Build toward the final calculator

    Uncomment the line below when ready to run your calculator!
    """

    # For testing individual modules during workshop:
    # test_module(1)  # Change number to test different modules

    # For final calculator (uncomment when complete):
    # main_calculator()

    print("🎉 Welcome to the Python Fundamentals Workshop!")
    print("👨‍💻 Follow along to build an amazing calculator!")
