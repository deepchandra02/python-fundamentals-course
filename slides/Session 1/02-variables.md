---
marp: true
---

# Module 2: Variables & Numbers 📊

## Storing and Using Data

**Duration: 10 minutes | Time: 0:08-0:18**

---

## What Are Variables? 📦

### Think of Variables as Labeled Boxes

- **Store information** for later use
- **Give names** to your data
- **Change values** as needed

### Why Use Variables?

- **Avoid repetition** - write once, use many times
- **Make code readable** - `age` is clearer than `25`
- **Easy to update** - change value in one place

---

## Creating Variables 🎯

### Simple Assignment

```python
app_name = "Python Calculator"
version = 1.0
author = "Your Name"
```

### Rules for Variable Names

- ✅ Start with **letter** or **underscore**: `name`, `_value`
- ✅ Use **letters, numbers, underscores**: `app_name`, `version2`
- ❌ **No spaces**: `app name` → `app_name`
- ❌ **No special characters**: `app-name` → `app_name`
- ❌ **Case-sensitive**: `Name` ≠ `name`

---

## Python Data Types 🔢

### Numbers

```python
age = 25                # Integer (whole number)
price = 19.99          # Float (decimal number)
temperature = -5       # Negative numbers work too
```

### Strings (Text)

```python
name = "Python"        # Double quotes
message = 'Hello!'     # Single quotes work too
emoji = "🧮"           # Emojis are strings too!
```

### Checking Types

```python
x = 5
print(type(x))         # <class 'int'>
```

---

## F-Strings: Beautiful Output 🌟

### Old Way (Don't Do This)

```python
name = "Sarah"
age = 25
print("Hello, my name is " + name + " and I am " + str(age))
```

### New Way (F-Strings) ✨

```python
name = "Sarah"
age = 25
print(f"Hello, my name is {name} and I am {age}")
```

### More F-String Examples

```python
app_name = "Calculator"
version = 1.0
print(f"Welcome to {app_name} v{version}! 🎉")
```

---

## Basic Math with Variables 🧮

### Arithmetic Operations

```python
a = 10
b = 5

addition = a + b        # 15
subtraction = a - b     # 5
multiplication = a * b  # 50
division = a / b        # 2.0
```

### Variable Updates

```python
score = 100
score = score + 10      # Now score is 110
score += 5              # Shortcut: now score is 115
```

---

## 🔨 Live Coding: Calculator v0.2

### Adding Personality to Our Calculator

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

### What We Added

- ✅ **Variables** for app information
- ✅ **F-strings** for beautiful output
- ✅ **Math operations** with variables
- ✅ **Multiple assignment** with `a, b = 10, 5`

---

## Quick Exercise (3 minutes) ⚡

### Your Turn!

1. **Personalize** your calculator with your name
2. **Try different operations**: subtraction, multiplication, division
3. **Experiment** with different number types (integers vs floats)
4. **Add more demo calculations**

### Challenge Ideas

```python
# Try these ideas:
favorite_number = 7
lucky_number = 13
result = favorite_number * lucky_number

pi = 3.14159
radius = 5
area = pi * radius * radius
print(f"Circle area: {area}")
```

---

## Type Conversion (Casting) 🔄

### When You Need to Convert Types

```python
# String to number
number_text = "42"
number = int(number_text)    # Convert to integer
decimal = float(number_text) # Convert to float

# Number to string
age = 25
age_text = str(age)          # Convert to string
```

### Common Conversions

- `int()` - Convert to whole number
- `float()` - Convert to decimal number
- `str()` - Convert to text

---

## Key Takeaways 📚

### What You Learned

- ✅ **Variables** store and organize data
- ✅ **Data types**: int, float, str
- ✅ **F-strings** for formatted output
- ✅ **Basic math** operations with variables
- ✅ **Type conversion** when needed

### Next Up: User Input!

- Get information from the user
- Make your calculator interactive
- Convert user input to numbers for math

**You're building the foundation! 🏗️**
