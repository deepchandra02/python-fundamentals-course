---
marp: true
---

# Module 11: Functions & Organization 🏗️

## Building Reusable Code Blocks

**Duration: 6 minutes | Time: 1:26-1:32**

---

## Why Functions? 🤔

### The Problem: Repetitive Code

```python
# Calculator without functions - messy!
num1 = float(input("First number: "))
num2 = float(input("Second number: "))

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
# Repeating similar patterns everywhere...
```

### The Solution: Functions

```python
# Clean, organized, reusable!
def add(x, y):
    return x + y

def get_two_numbers():
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    return num1, num2

# Use anywhere in your program
result = add(10, 5)
num1, num2 = get_two_numbers()
```

---

## What Are Functions? 📦

### Think of Functions as...

- 🏭 **Factories** - input materials, output products
- 📱 **Apps** - tap button, get result
- 🎛️ **Black boxes** - input goes in, output comes out
- 🧮 **Calculator buttons** - press +, get addition

### Function Benefits

- **Reusability** - write once, use many times
- **Organization** - group related code together
- **Testing** - easier to test small pieces
- **Debugging** - isolate problems quickly
- **Collaboration** - team members work on different functions

---

## Creating Functions 🛠️

### Basic Function Syntax

```python
def function_name(parameters):
    """Optional docstring describing function"""
    # Function body
    return result  # Optional return statement
```

### Simple Examples

```python
def greet():
    """Print a greeting message"""
    print("Hello, Calculator User!")

def add(x, y):
    """Add two numbers and return the result"""
    return x + y

def get_user_name():
    """Get user's name from input"""
    name = input("What's your name? ")
    return name
```

---

## Parameters and Arguments 📥

### Parameters vs Arguments

```python
def add(x, y):    # x and y are PARAMETERS
    return x + y

result = add(5, 3)  # 5 and 3 are ARGUMENTS
```

### Different Parameter Types

```python
# Required parameters
def multiply(x, y):
    return x * y

# Default parameters
def power(base, exponent=2):
    return base ** exponent

power(5)      # Uses default: 5²
power(5, 3)   # Override default: 5³

# Multiple parameters
def calculate(num1, operation, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
```

---

## Return Values 📤

### Functions That Return Values

```python
def add(x, y):
    return x + y

def is_even(number):
    return number % 2 == 0

def get_operation_name(symbol):
    operations = {"+": "Addition", "-": "Subtraction"}
    return operations.get(symbol, "Unknown")

# Using return values
result = add(10, 5)           # result = 15
even = is_even(8)             # even = True
name = get_operation_name("+") # name = "Addition"
```

### Functions That Don't Return (Return None)

```python
def print_welcome():
    print("Welcome to Calculator!")
    # No return statement = returns None

def show_history(calculations):
    for i, calc in enumerate(calculations, 1):
        print(f"{i}. {calc}")
    # No return statement = returns None
```

---

## 🔨 Live Coding: Calculator v3.0

### Organizing with Functions!

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    return "Error: Division by zero!"

def get_operation_function(op):
    """Return the appropriate function for the operation"""
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    return operations.get(op, None)

# Usage
num1, num2 = 10, 5
operation = "+"
func = get_operation_function(operation)
if func:
    result = func(num1, num2)
    print(f"{num1} {operation} {num2} = {result}")
```

---

## Advanced Function Patterns 💡

### Storing Functions in Dictionaries

```python
# Functions as values!
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Call function through dictionary
op = "+"
result = operations[op](10, 5)  # Calls add(10, 5)
```

### Functions Calling Other Functions

```python
def safe_divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return divide(x, y)

def calculate_with_validation(num1, op, num2):
    func = get_operation_function(op)
    if func:
        return func(num1, num2)
    return "Invalid operation"
```

---

## What We Just Built 🎉

### New Architecture

- ✅ **Modular design** - each operation is separate function
- ✅ **Reusable components** - functions used anywhere
- ✅ **Clean organization** - related code grouped together
- ✅ **Easy to extend** - add new operations easily
- ✅ **Professional structure** - like real applications

### Code Quality Improvements

- **Readable** - clear function names explain purpose
- **Testable** - can test each function individually
- **Maintainable** - bugs isolated to specific functions
- **Scalable** - easy to add features

---

## Quick Exercise (1 minute) ⚡

### Your Turn!

1. **Create power() function** for exponentiation
2. **Add modulo() function** for remainder
3. **Update operations dictionary** with new functions

### Challenge: Advanced Functions

```python
def power(base, exponent):
    return base ** exponent

def modulo(dividend, divisor):
    if divisor != 0:
        return dividend % divisor
    return "Cannot modulo by zero"

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)  # Recursive function!
```

---

## Function Documentation 📚

### Docstrings: Professional Documentation

```python
def calculate_area(radius):
    """
    Calculate the area of a circle.

    Parameters:
    radius (float): The radius of the circle

    Returns:
    float: The area of the circle
    """
    return 3.14159 * radius ** 2

# Access documentation
print(calculate_area.__doc__)
help(calculate_area)
```

### Good Function Names

```python
# Good ✅
def calculate_circle_area(radius):
def get_user_input():
def validate_operation(op):

# Bad ❌
def calc(r):
def get():
def check(x):
```

---

## Scope: Variable Visibility 🔍

### Local vs Global Scope

```python
# Global variable
app_name = "Calculator"

def greet_user(name):
    # Local variables
    message = f"Welcome to {app_name}, {name}!"
    return message

print(greet_user("John"))  # Works - can access global
print(message)             # Error - message is local to function
```

### Function Parameters Are Local

```python
def add(x, y):
    # x and y only exist inside this function
    result = x + y
    return result

# print(x)  # Error - x doesn't exist outside function
```

---

## Common Function Patterns 🎯

### Input Validation Functions

```python
def safe_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

def get_valid_operation():
    valid_ops = ["+", "-", "*", "/"]
    while True:
        op = input("Operation (+,-,*,/): ")
        if op in valid_ops:
            return op
        print("Invalid operation!")
```

### Utility Functions

```python
def format_result(value, decimal_places=2):
    return f"{value:.{decimal_places}f}"

def is_valid_number(text):
    try:
        float(text)
        return True
    except ValueError:
        return False
```

---

## Function Best Practices 💎

### Single Responsibility Principle

```python
# Good ✅ - each function does one thing
def get_numbers():
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    return num1, num2

def add(x, y):
    return x + y

def display_result(result):
    print(f"Result: {result}")

# Bad ❌ - function does too many things
def calculate_and_display():
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    result = num1 + num2
    print(f"Result: {result}")
    # Save to history
    # Update statistics
    # etc...
```

### Keep Functions Small

- **Rule of thumb**: If you can't see entire function on screen, it's too big
- **Break down** large functions into smaller ones
- **Each function** should have clear, single purpose

---

## Key Takeaways 📚

### What You Learned

- ✅ **Functions organize code** into reusable blocks
- ✅ **Parameters and return values** for input/output
- ✅ **Scope** determines variable visibility
- ✅ **Dictionaries can store functions** for dynamic calling
- ✅ **Professional code structure** with modular design

### Next Up: Error Handling!

- Handle user mistakes gracefully
- Try/except blocks for robust code
- Input validation and error messages
- Make calculator bulletproof

**Your calculator is becoming professional! 💼**
