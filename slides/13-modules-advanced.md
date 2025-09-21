---
marp: false
---

# Module 13: Modules & Advanced Features 🚀

## Professional Calculator with Scientific Functions

**Duration: 6 minutes | Time: 1:38-1:44**

---

## What Are Modules? 📚

### Think of Modules as...

- 📖 **Library books** - specialized knowledge you can borrow
- 🧰 **Toolbox** - specialized tools for specific jobs
- 🏪 **Store** - go there when you need specific items
- 🔬 **Lab equipment** - advanced tools for complex tasks

### Why Use Modules?

- **Don't reinvent the wheel** - use existing solutions
- **Access advanced features** - beyond basic Python
- **Professional development** - leverage expert code
- **Expand capabilities** - scientific, web, graphics, etc.

---

## The `import` Statement 📥

### Basic Import Syntax

```python
import math

# Use module functions with module.function()
result = math.sqrt(25)      # 5.0
pi_value = math.pi          # 3.141592653589793
```

### Different Import Styles

```python
# Import entire module
import math
radius = math.sqrt(area / math.pi)

# Import specific functions
from math import sqrt, pi
radius = sqrt(area / pi)

# Import with alias
import math as m
radius = m.sqrt(area / m.pi)

# Import all (not recommended)
from math import *
radius = sqrt(area / pi)  # Can cause naming conflicts!
```

---

## The Math Module: Calculator's Best Friend 🧮

### Basic Math Functions

```python
import math

# Roots and powers
math.sqrt(16)         # 4.0 - square root
math.pow(2, 3)        # 8.0 - power (same as 2**3)
math.exp(1)           # 2.718... - e^x

# Logarithms
math.log(10)          # 2.302... - natural log
math.log10(100)       # 2.0 - base-10 log
math.log(8, 2)        # 3.0 - log base 2

# Absolute value and rounding
math.fabs(-5.5)       # 5.5 - absolute value
math.ceil(4.2)        # 5 - round up
math.floor(4.8)       # 4 - round down
```

### Trigonometric Functions

```python
import math

# Convert degrees to radians first!
angle_degrees = 45
angle_radians = math.radians(angle_degrees)

math.sin(angle_radians)     # 0.707... - sine
math.cos(angle_radians)     # 0.707... - cosine
math.tan(angle_radians)     # 1.0 - tangent

# Convert back to degrees
result_radians = math.asin(0.5)  # arcsin
result_degrees = math.degrees(result_radians)  # 30.0
```

### Mathematical Constants

```python
import math

math.pi      # 3.141592653589793
math.e       # 2.718281828459045
math.tau     # 6.283185307179586 (2π)
math.inf     # Infinity
math.nan     # Not a Number
```

---

## 🔨 Live Coding: Calculator v4.0 FINAL

### Scientific Calculator Features!

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

def calculate_bmi():
    print("💪 BMI CALCULATOR")
    weight = safe_float_input("Weight (kg): ")
    height = safe_float_input("Height (m): ")
    bmi = weight / (height ** 2)
    print(f"BMI: {bmi:.1f}")

    if bmi < 18.5: print("Category: Underweight")
    elif bmi < 25: print("Category: Normal weight")
    elif bmi < 30: print("Category: Overweight")
    else: print("Category: Obese")
```

---

## Lambda Functions: Quick Functions 🏃‍♂️

### What Are Lambda Functions?

- **Anonymous functions** - functions without names
- **One-line functions** - for simple operations
- **Perfect for** dictionary values, sorting, filtering

### Lambda Syntax

```python
# Regular function
def square(x):
    return x ** 2

# Lambda function (same thing)
square = lambda x: x ** 2

# Using in dictionaries
operations = {
    "sqrt": lambda x: math.sqrt(x),
    "square": lambda x: x ** 2,
    "cube": lambda x: x ** 3
}

result = operations["sqrt"](25)  # 5.0
```

### Practical Uses

```python
# Sort by second element of tuple
points = [(1, 5), (3, 2), (2, 8)]
sorted_points = sorted(points, key=lambda point: point[1])
# [(3, 2), (1, 5), (2, 8)]

# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6]
```

---

## String Formatting: Professional Output ✨

### F-String Advanced Formatting

```python
import math

number = 1234.56789
large_number = 1234567.89

# Decimal places
print(f"Rounded: {number:.2f}")           # 1234.57

# Thousands separators
print(f"With commas: {large_number:,.2f}") # 1,234,567.89

# Scientific notation
print(f"Scientific: {number:.2e}")         # 1.23e+03

# Percentage
ratio = 0.856
print(f"Percentage: {ratio:.1%}")          # 85.6%

# Padding and alignment
print(f"Padded: '{number:10.2f}'")         # '   1234.57'
print(f"Left: '{number:<10.2f}'")          # '1234.57   '
print(f"Center: '{number:^10.2f}'")        # ' 1234.57  '
```

### Professional Result Formatting

```python
def format_result(num1, op, num2, result):
    """Professional result formatting"""
    if isinstance(result, str):  # Error message
        return f"❌ {result}"

    # Format numbers nicely
    return f"📊 {num1:,.3f} {op} {num2:,.3f} = {result:,.3f}"

# Example usage
print(format_result(1234.5, "+", 567.8, 1802.3))
# 📊 1,234.500 + 567.800 = 1,802.300
```

---

## What We Just Built 🎉

### Complete Calculator Features

- ✅ **Scientific functions** (√, sin, log, e^x)
- ✅ **BMI calculator** with health categories
- ✅ **Professional formatting** with thousands separators
- ✅ **Lambda functions** for clean operation storage
- ✅ **Math module integration** for advanced calculations

### From Hello World to Professional App

- **Started**: Simple print statement
- **Ended**: Feature-rich scientific calculator
- **Learned**: All fundamental Python concepts
- **Built**: Real, usable application

---

## Quick Exercise (1 minute) ⚡

### Your Turn!

1. **Add cosine and tangent** functions
2. **Add more constants** like math.pi and math.e
3. **Create temperature converter** function

### Challenge: Temperature Converter

```python
def temperature_converter():
    print("🌡️ TEMPERATURE CONVERTER")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Choose (1-2): ")
    temp = safe_float_input("Enter temperature: ")

    if choice == "1":
        result = (temp * 9/5) + 32
        print(f"{temp}°C = {result:.1f}°F")
    elif choice == "2":
        result = (temp - 32) * 5/9
        print(f"{temp}°F = {result:.1f}°C")
```

---

## Other Useful Modules 📦

### Standard Library Modules

```python
# Random numbers
import random
dice_roll = random.randint(1, 6)
random_choice = random.choice(["rock", "paper", "scissors"])

# Date and time
import datetime
now = datetime.datetime.now()
print(f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Operating system interface
import os
current_directory = os.getcwd()
```

### Third-Party Modules (pip install)

```python
# Data analysis
import pandas as pd
import numpy as np

# Web development
import flask
import requests

# Graphics
import matplotlib.pyplot as plt
import tkinter
```

---

## Code Organization Best Practices 🏗️

### Organizing Imports

```python
# Standard library imports first
import math
import datetime
import os

# Third-party imports second
import requests
import numpy as np

# Local imports last
from my_calculator import operations
from my_calculator.utils import format_result
```

### Creating Your Own Modules

```python
# File: calculator_utils.py
def safe_float_input(prompt):
    """Safe input function for floats"""
    # Implementation here
    pass

def format_currency(amount):
    """Format number as currency"""
    return f"${amount:,.2f}"

# File: main_calculator.py
from calculator_utils import safe_float_input, format_currency

# Use imported functions
amount = safe_float_input("Enter amount: ")
print(format_currency(amount))
```

---

## Professional Touches 💎

### Application Header

```python
def display_banner():
    print("=" * 60)
    print("    🧮 PYTHON SCIENTIFIC CALCULATOR v4.0 🧮")
    print("    Built with Python | Learning Workshop 2024")
    print("=" * 60)

def display_credits():
    print("\n" + "="*50)
    print("🎉 Congratulations! You built a complete calculator!")
    print("📚 You learned: Variables, Functions, Loops, Error Handling")
    print("🚀 Next steps: GUI, Web apps, Data science")
    print("="*50)
```

### Help System

```python
def show_help():
    print("""
    🆘 CALCULATOR HELP

    Available Operations:
    + : Addition        - : Subtraction
    * : Multiplication  / : Division
    ** : Power          % : Modulo

    Scientific Functions:
    √ : Square root     sin/cos/tan : Trigonometry
    ln : Natural log    e^x : Exponential

    Special Features:
    📋 History tracking  ⚙️ User settings
    💪 BMI calculator   🌡️ Temperature converter
    """)
```

---

## Key Takeaways 📚

### What You Learned

- ✅ **import statement** brings in external modules
- ✅ **math module** provides scientific functions
- ✅ **lambda functions** for quick anonymous functions
- ✅ **String formatting** for professional output
- ✅ **Code organization** and professional structure

### Your Achievement 🏆

You've built a **complete, professional calculator** with:

- Interactive menu system
- Error handling and validation
- Scientific functions
- Data storage and history
- Professional formatting
- All Python fundamentals!

---

## What's Next? 🚀

### Immediate Extensions

- **GUI version** with tkinter
- **Web calculator** with Flask
- **Mobile app** concepts
- **Database storage** for history

### Python Learning Path

- **Object-Oriented Programming** - classes and objects
- **Web Development** - Flask, Django
- **Data Science** - pandas, numpy, matplotlib
- **Automation** - scripting, APIs
- **Machine Learning** - TensorFlow, scikit-learn

### Congratulations! 🎉

You've mastered Python fundamentals and built something amazing!

**Your journey in programming has just begun! 💪**
