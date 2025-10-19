# Python Fundamentals Workshop: Building a Calculator
*90-Minute Interactive Coding Experience*

## Workshop Overview
High-intensity, hands-on Python workshop where students build a complete calculator while learning core programming concepts. Students work with split-screen setup: lesson materials on left, live coding on right.

## Setup Requirements
- **Left Panel**: Lesson materials and exercises
- **Right Panel**: `calculator.py` file for live coding
- **Duration**: 90 minutes packed with interactive coding

---

## ⚡ Module 1: Hello Python World
**Duration**: 8 minutes | **Time**: 0:00-0:08

### Quick Learning:
- Python basics and print statements
- Comments for code documentation

### 🔨 Live Coding - Calculator v0.1:
```python
# My Python Calculator
print("Hello, World!")
print("🧮 Welcome to My Calculator App!")
# This is my first Python program
```

**⚡ Quick Exercise**: Add your name to the welcome message (2 min)

---

## ⚡ Module 2: Variables & Numbers
**Duration**: 10 minutes | **Time**: 0:08-0:18

### Quick Learning:
- Variables, numbers (int/float), strings
- F-string formatting

### 🔨 Live Coding - Calculator v0.2:
```python
# Calculator with personality
app_name = "Python Calculator"
version = 1.0
author = "Your Name Here"

print(f"🧮 {app_name} v{version}")
print(f"👨‍💻 Created by: {author}")

# Quick math demo
a, b = 10, 5
print(f"Demo: {a} + {b} = {a + b}")
```

**⚡ Quick Exercise**: Personalize your calculator and try different operations (3 min)

---

## ⚡ Module 3: User Input Magic
**Duration**: 10 minutes | **Time**: 0:18-0:28

### Quick Learning:
- `input()` function
- Converting strings to numbers
- Basic error awareness

### 🔨 Live Coding - Calculator v0.3:
```python
print("🧮 Interactive Calculator v0.3")

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Show the magic
result = num1 + num2
print(f"✨ {num1} + {num2} = {result}")
```

**⚡ Quick Exercise**: Test with different numbers and operations (2 min)

---

## ⚡ Module 4: Operation Station
**Duration**: 12 minutes | **Time**: 0:28-0:40

### Quick Learning:
- All arithmetic operators (+, -, *, /, %, **)
- Order of operations

### 🔨 Live Coding - Calculator v0.4:
```python
print("🧮 Multi-Operation Calculator v0.4")

num1 = float(input("First number: "))
num2 = float(input("Second number: "))

print(f"➕ Addition: {num1} + {num2} = {num1 + num2}")
print(f"➖ Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"✖️ Multiplication: {num1} * {num2} = {num1 * num2}")
print(f"➗ Division: {num1} / {num2} = {num1 / num2}")
print(f"🔥 Power: {num1} ** {num2} = {num1 ** num2}")
```

**⚡ Quick Exercise**: Add modulo (%) operation (3 min)

---

## ⚡ Module 5: Smart Decisions
**Duration**: 15 minutes | **Time**: 0:40-0:55

### Quick Learning:
- if/elif/else statements
- Boolean logic
- Error handling basics

### 🔨 Live Coding - Calculator v1.0:
```python
print("🧮 Smart Calculator v1.0")

num1 = float(input("First number: "))
operation = input("Operation (+, -, *, /, **): ")
num2 = float(input("Second number: "))

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
    result = num1 ** num2
else:
    result = "❌ Invalid operation!"

print(f"🎯 Result: {result}")
```

**⚡ Quick Exercise**: Test all operations including error cases (4 min)

---

## ⚡ Module 6: Loop Power
**Duration**: 8 minutes | **Time**: 0:55-1:03

### Quick Learning:
- While loops for repetition
- break and continue
- Menu systems

### 🔨 Live Coding - Calculator v2.0:
```python
print("🧮 Never-Ending Calculator v2.0")

while True:
    print("\n🎯 CALCULATOR MENU")
    print("1️⃣ Basic Math")
    print("2️⃣ Exit")

    choice = input("Choose (1-2): ")
    if choice == "2":
        print("👋 Thanks for calculating!")
        break
    elif choice == "1":
        num1 = float(input("First number: "))
        op = input("Operation (+,-,*,/): ")
        num2 = float(input("Second number: "))
        if op == "+": result = num1 + num2
        elif op == "-": result = num1 - num2
        elif op == "*": result = num1 * num2
        elif op == "/": result = num1 / num2 if num2 != 0 else "Error!"
        print(f"✅ Result: {result}")
```

**⚡ Quick Exercise**: Add power operations to menu (2 min)

---

## ⚡ Module 7: Lists & History
**Duration**: 7 minutes | **Time**: 1:03-1:10

### Quick Learning:
- Lists: creating, appending, accessing
- Storing calculation history

### 🔨 Live Coding - Calculator v2.1:
```python
history = []  # List to store calculations

def add_to_history(calc_string):
    history.append(calc_string)

def show_history():
    print("\n📋 CALCULATION HISTORY")
    for i, calc in enumerate(history, 1):
        print(f"{i}. {calc}")

# In your calculation section:
calc_string = f"{num1} {op} {num2} = {result}"
add_to_history(calc_string)

# Add to menu: "3️⃣ Show History"
```

**⚡ Quick Exercise**: Integrate history into calculator (2 min)

---

## ⚡ Module 8: Dictionaries & Settings
**Duration**: 6 minutes | **Time**: 1:10-1:16

### Quick Learning:
- Dictionaries: key-value pairs
- Storing user preferences

### 🔨 Live Coding - Calculator v2.2:
```python
# User settings stored in dictionary
user_settings = {
    "username": "Guest",
    "decimal_places": 2,
    "show_steps": True,
    "favorite_operation": "+"
}

operations = {
    "+": "Addition",
    "-": "Subtraction",
    "*": "Multiplication",
    "/": "Division"
}

print(f"👋 Welcome back, {user_settings['username']}!")
print(f"🔧 Decimal places: {user_settings['decimal_places']}")

# Access operations by key
selected_op = "+"
print(f"Performing {operations[selected_op]}")
```

**⚡ Quick Exercise**: Add more settings to the dictionary (1 min)

---

## ⚡ Module 9: Tuples & Constants
**Duration**: 5 minutes | **Time**: 1:16-1:21

### Quick Learning:
- Tuples: immutable sequences
- Mathematical constants

### 🔨 Live Coding - Calculator v2.3:
```python
# Mathematical constants as tuples
MATH_CONSTANTS = (3.14159, 2.71828, 1.41421)  # π, e, √2
CONSTANT_NAMES = ("Pi", "Euler's e", "√2")

# Display constants
print("🔢 MATH CONSTANTS")
for i, (name, value) in enumerate(zip(CONSTANT_NAMES, MATH_CONSTANTS)):
    print(f"{i+1}. {name} = {value}")

# Coordinates as tuples
point1 = (10, 20)
point2 = (30, 40)
print(f"Distance calculation between {point1} and {point2}")
```

**⚡ Quick Exercise**: Add more mathematical constants (1 min)

---

## ⚡ Module 10: Sets & Unique Operations
**Duration**: 5 minutes | **Time**: 1:21-1:26

### Quick Learning:
- Sets: unique collections
- Set operations

### 🔨 Live Coding - Calculator v2.4:
```python
# Track unique operations used
operations_used = set()
available_operations = {"add", "subtract", "multiply", "divide", "power"}

# When user performs operation:
operation_name = "add"  # example
operations_used.add(operation_name)

print(f"🎯 Operations you've tried: {operations_used}")
print(f"📝 Try these next: {available_operations - operations_used}")

# Check if user is exploring
if len(operations_used) == len(available_operations):
    print("🏆 Calculator Master! You've tried everything!")
```

**⚡ Quick Exercise**: Track unique numbers used in calculations (1 min)

---

## ⚡ Module 11: Functions & Organization
**Duration**: 6 minutes | **Time**: 1:26-1:32

### Quick Learning:
- Functions: organization and reusability
- Return values and parameters

### 🔨 Live Coding - Calculator v3.0:
```python
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error: Division by zero!"

def get_operation_function(op):
    """Return the appropriate function for the operation"""
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
    return operations.get(op, None)

# Usage
num1, num2 = 10, 5
operation = "+"
func = get_operation_function(operation)
if func:
    result = func(num1, num2)
    print(f"{num1} {operation} {num2} = {result}")
```

**⚡ Quick Exercise**: Add power and modulo functions (1 min)

---

## ⚡ Module 12: Error Handling & Polish
**Duration**: 6 minutes | **Time**: 1:32-1:38

### Quick Learning:
- Try/except blocks
- Input validation
- Professional error messages

### 🔨 Live Coding - Calculator v4.0:
```python
def safe_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number!")

def safe_operation_input():
    valid_ops = {"+", "-", "*", "/", "**", "%"}
    while True:
        op = input("Operation (+,-,*,/,**,%): ")
        if op in valid_ops:
            return op
        print(f"❌ Invalid! Use: {', '.join(valid_ops)}")

# Safe calculator usage
try:
    num1 = safe_float_input("First number: ")
    op = safe_operation_input()
    num2 = safe_float_input("Second number: ")
    # Perform calculation with error handling
except KeyboardInterrupt:
    print("\n👋 Calculator closed safely!")
```

**⚡ Quick Exercise**: Add validation for division by zero (1 min)

---

## ⚡ Module 13: Modules & Advanced Features
**Duration**: 6 minutes | **Time**: 1:38-1:44

### Quick Learning:
- Import statement and math module
- String formatting
- Advanced features

### 🔨 Live Coding - Calculator v4.0 FINAL:
```python
import math

def scientific_operations():
    print("🔬 SCIENTIFIC CALCULATOR")
    operations = {
        "1": ("Square Root", lambda x: math.sqrt(x)),
        "2": ("Sine (degrees)", lambda x: math.sin(math.radians(x))),
        "3": ("Natural Log", lambda x: math.log(x)),
        "4": ("Power of e", lambda x: math.exp(x))
    }

    for key, (name, _) in operations.items():
        print(f"{key}. {name}")

    choice = input("Choose (1-4): ")
    if choice in operations:
        num = safe_float_input("Enter number: ")
        name, func = operations[choice]
        result = func(num)
        print(f"✨ {name}({num}) = {result:.4f}")

def format_result(num1, op, num2, result):
    """Professional result formatting"""
    return f"📊 {num1:,.2f} {op} {num2:,.2f} = {result:,.2f}"

# Add scientific mode to main menu
```

**⚡ Quick Exercise**: Add more scientific functions (1 min)

---

## 🎯 Workshop Wrap-up
**Duration**: 10 minutes | **Time**: 1:40-1:50

### Student Showcase:
- Quick demos of personalized calculators
- Share favorite features
- Q&A and next steps

### What Students Built:
✅ Interactive calculator with menu system
✅ Error handling and input validation
✅ Calculation history tracking
✅ Scientific operations
✅ Professional code organization
✅ Real programming skills!

---

## 📚 Skills Mastered in 90 Minutes:
- **Variables & Data Types**: Numbers, strings, booleans
- **User Input/Output**: Interactive programs and formatting
- **Operators**: All mathematical operations (+, -, *, /, %, **)
- **Conditionals**: If/elif/else statements and boolean logic
- **Loops**: While loops, break/continue, menu systems
- **Lists**: Creating, appending, accessing, iteration
- **Dictionaries**: Key-value pairs, user settings, lookups
- **Tuples**: Immutable sequences, constants, coordinates
- **Sets**: Unique collections, set operations, tracking
- **Functions**: Definition, parameters, return values, organization
- **Error Handling**: Try/except blocks, input validation
- **Modules**: Import statements, math module, advanced functions
- **String Operations**: F-strings, formatting, professional output

## 🚀 Post-Workshop Extensions:
- Add GUI with tkinter
- Create web version with Flask
- Build mobile app concepts
- Explore data science applications

**Result**: Students leave with a working calculator app and solid Python foundation! 🎉