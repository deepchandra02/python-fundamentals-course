# Module 5: Smart Decisions 🧠
## If/Elif/Else Logic
**Duration: 15 minutes | Time: 0:40-0:55**

---

## Why Programs Need to Make Decisions 🤔

### Real-World Decision Making
- 🌧️ "If it's raining, take umbrella"
- 🏧 "If PIN is correct, show balance"
- 🧮 "If user chooses '+', do addition"

### In Programming
- **Conditional statements** let programs choose what to do
- **Different actions** based on different conditions
- **Smart programs** respond appropriately to user input

---

## Boolean Values: True or False ✅❌

### The Foundation of Decisions
```python
is_raining = True
is_sunny = False
temperature = 25

# Boolean expressions
is_hot = temperature > 30        # False
is_warm = temperature >= 20      # True
is_perfect = temperature == 25   # True
```

### Comparison Operators
| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>=` | Greater or equal | `5 >= 5` | `True` |
| `<=` | Less or equal | `3 <= 5` | `True` |

---

## The `if` Statement 🚦

### Basic Syntax
```python
if condition:
    # Code to run if condition is True
    print("Condition was true!")
```

### Real Example
```python
age = 18

if age >= 18:
    print("You can vote!")
    print("You're an adult!")
```

### Important: Indentation Matters!
```python
# Correct ✅
if age >= 18:
    print("This is inside the if")
    print("This is also inside")

# Wrong ❌ - IndentationError
if age >= 18:
print("This won't work")
```

---

## `if/else`: Two Choices 🔀

### When You Need an Alternative
```python
temperature = 15

if temperature > 20:
    print("It's warm! 🌞")
else:
    print("It's cool! 🧥")
```

### Calculator Example
```python
operation = input("Enter operation (+, -): ")

if operation == "+":
    result = num1 + num2
else:
    result = num1 - num2

print(f"Result: {result}")
```

---

## `if/elif/else`: Multiple Choices 🎯

### When You Have Many Options
```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade: {grade}")
```

### How `elif` Works
1. **Checks conditions** in order from top to bottom
2. **Runs first match** and skips the rest
3. **else** runs if no conditions were true

---

## String Comparisons 📝

### Comparing Text Input
```python
operation = input("Enter operation: ")

if operation == "+":
    print("Addition selected")
elif operation == "-":
    print("Subtraction selected")
elif operation == "*":
    print("Multiplication selected")
else:
    print("Unknown operation")
```

### Case Sensitivity Matters!
```python
answer = input("Continue? (yes/no): ")

# This might miss "Yes", "YES", "Y"
if answer == "yes":
    print("Continuing...")

# Better approach (we'll learn more techniques later)
if answer.lower() == "yes":
    print("Continuing...")
```

---

## Logical Operators: Combining Conditions 🔗

### `and` - Both Must Be True
```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive!")
```

### `or` - At least One Must Be True
```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's weekend!")
```

### `not` - Opposite of Condition
```python
is_raining = False

if not is_raining:
    print("Great day for a walk!")
```

---

## 🔨 Live Coding: Calculator v1.0

### Smart Operation Selection!
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

---

## What We Just Built 🎉

### New Features
- ✅ **User chooses operation** instead of showing all
- ✅ **Handles different operations** appropriately
- ✅ **Error checking** for division by zero
- ✅ **Invalid input handling**
- ✅ **Professional error messages**

### Nested Conditions
- Used `if` inside another `if` for division check
- Shows how conditions can be combined for complex logic

---

## Quick Exercise (4 minutes) ⚡

### Your Turn!
1. **Test all operations** including error cases
2. **Try dividing by zero** - see the error handling
3. **Enter invalid operation** like "#" - see what happens
4. **Add support for modulo** operation (%)

### Challenge: Add More Operations
```python
elif operation == "%":
    if num2 != 0:
        result = num1 % num2
    else:
        result = "❌ Error: Can't modulo by zero!"
elif operation == "//":
    if num2 != 0:
        result = num1 // num2
    else:
        result = "❌ Error: Can't divide by zero!"
```

---

## Common Conditional Patterns 💡

### Error Checking
```python
if num2 == 0:
    print("Error: Division by zero!")
else:
    result = num1 / num2
```

### Input Validation
```python
if operation in ["+", "-", "*", "/", "**", "%"]:
    # Valid operation - proceed
    pass
else:
    print("Invalid operation!")
```

### Range Checking
```python
if 0 <= score <= 100:
    print("Valid score")
else:
    print("Score must be between 0 and 100")
```

---

## Common Mistakes to Avoid 🚨

### Assignment vs Comparison
```python
# Wrong ❌ - Assignment
if operation = "+":

# Correct ✅ - Comparison
if operation == "+":
```

### Indentation Issues
```python
# Wrong ❌
if condition:
print("This won't work")

# Correct ✅
if condition:
    print("This works!")
```

### Missing Colon
```python
# Wrong ❌
if condition
    print("Missing colon")

# Correct ✅
if condition:
    print("Colon included!")
```

---

## Key Takeaways 📚

### What You Learned
- ✅ **if/elif/else** for decision making
- ✅ **Comparison operators** (==, !=, >, <, >=, <=)
- ✅ **Logical operators** (and, or, not)
- ✅ **Error handling** with nested conditions
- ✅ **Input validation** for user choices

### Next Up: Loops!
- Make programs repeat actions
- Create menu systems
- Let users calculate multiple times
- Build a never-ending calculator

**Your calculator is getting smart! 🤖**