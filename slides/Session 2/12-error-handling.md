---
marp: false
---

# Module 12: Error Handling & Polish 🛡️

## Making Your Calculator Bulletproof

**Duration: 6 minutes | Time: 1:32-1:38**

---

## Why Error Handling Matters 💥

### What Happens Without Error Handling

```python
# User enters "hello" instead of number
num1 = float(input("Enter number: "))  # CRASH! 💥
# ValueError: could not convert string to float: hello
# Program stops, user confused
```

### What Happens With Error Handling

```python
# Graceful handling of user mistakes
while True:
    try:
        num1 = float(input("Enter number: "))
        break  # Success! Exit loop
    except ValueError:
        print("❌ Please enter a valid number!")
        # Program continues, user gets helpful message
```

### Professional vs Amateur Apps

- **Amateur**: Crashes on unexpected input
- **Professional**: Handles errors gracefully with helpful messages

---

## Types of Errors 🚨

### Syntax Errors (Code Problems)

```python
# These prevent code from running at all
if x = 5:           # SyntaxError: should be ==
    print("hello"   # SyntaxError: missing closing )
```

### Runtime Errors (User Problems)

```python
# These happen during program execution
int("hello")        # ValueError
10 / 0             # ZeroDivisionError
my_list[99]        # IndexError
my_dict["missing"] # KeyError
```

### Logical Errors (Logic Problems)

```python
# Code runs but produces wrong results
def calculate_area(radius):
    return 3.14 * radius  # Should be radius ** 2!
```

---

## Try/Except: Catching Errors 🎣

### Basic Try/Except

```python
try:
    # Code that might fail
    number = float(input("Enter number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("❌ Please enter a valid number!")
except ZeroDivisionError:
    print("❌ Cannot divide by zero!")
```

### Catch Multiple Errors

```python
try:
    # Risky code here
    result = risky_operation()
except (ValueError, TypeError, ZeroDivisionError):
    print("❌ Something went wrong with the numbers!")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
```

---

## The try/except/else/finally Pattern 🔄

### Complete Error Handling

```python
try:
    # Code that might fail
    num = float(input("Enter number: "))
    result = 10 / num
except ValueError:
    print("❌ Invalid number format!")
except ZeroDivisionError:
    print("❌ Cannot divide by zero!")
else:
    # Runs only if no exceptions occurred
    print(f"✅ Success! Result: {result}")
finally:
    # Always runs, regardless of errors
    print("Operation completed.")
```

---

## 🔨 Live Coding: Calculator v4.0

### Bulletproof Input Functions!

```python
def safe_float_input(prompt):
    """Get float input with error handling"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number!")

def safe_operation_input():
    """Get valid operation with error handling"""
    valid_ops = {"+", "-", "*", "/", "**", "%"}
    while True:
        op = input("Operation (+,-,*,/,**,%): ")
        if op in valid_ops:
            return op
        print(f"❌ Invalid! Use: {', '.join(valid_ops)}")

def safe_divide(x, y):
    """Safe division with zero checking"""
    try:
        return x / y
    except ZeroDivisionError:
        return "❌ Cannot divide by zero!"
```

---

## Advanced Error Handling Patterns 💡

### Input Validation Loop

```python
def get_positive_number(prompt):
    """Get a positive number from user"""
    while True:
        try:
            num = float(input(prompt))
            if num <= 0:
                print("❌ Please enter a positive number!")
                continue
            return num
        except ValueError:
            print("❌ Please enter a valid number!")

def get_integer_in_range(prompt, min_val, max_val):
    """Get integer within specified range"""
    while True:
        try:
            num = int(input(prompt))
            if min_val <= num <= max_val:
                return num
            print(f"❌ Please enter a number between {min_val} and {max_val}!")
        except ValueError:
            print("❌ Please enter a valid integer!")
```

---

## What We Just Added 🎉

### Bulletproof Features

- ✅ **Safe input functions** that never crash
- ✅ **Helpful error messages** instead of crashes
- ✅ **Input validation** for all user entries
- ✅ **Graceful error recovery** - program continues running
- ✅ **Professional user experience**

### User Experience Improvements

- **No more crashes** from invalid input
- **Clear feedback** on what went wrong
- **Second chances** to enter correct data
- **Confidence** in using the calculator

---

## Quick Exercise (1 minute) ⚡

### Your Turn!

1. **Test safe input** with invalid entries (letters, symbols)
2. **Try pressing Ctrl+C** during input - what happens?
3. **Add validation** for negative numbers in square root

### Challenge: Handle Keyboard Interrupt

```python
def safe_calculator():
    try:
        while True:
            num1 = safe_float_input("First number: ")
            op = safe_operation_input()
            num2 = safe_float_input("Second number: ")
            # Calculate and display result
    except KeyboardInterrupt:
        print("\n👋 Calculator closed safely!")
```

---

## Specific Calculator Error Cases 🧮

### Division by Zero

```python
def safe_divide(x, y):
    if y == 0:
        return "❌ Error: Cannot divide by zero!"
    return x / y

def safe_modulo(x, y):
    if y == 0:
        return "❌ Error: Cannot modulo by zero!"
    return x % y
```

### Invalid Operations

```python
def validate_operation(op):
    valid_operations = {"+", "-", "*", "/", "**", "%", "//"}
    if op not in valid_operations:
        raise ValueError(f"Invalid operation: {op}")
    return True
```

### Range Validation

```python
def safe_power(base, exponent):
    try:
        if abs(base) > 1000 and exponent > 10:
            return "❌ Result would be too large!"
        return base ** exponent
    except OverflowError:
        return "❌ Result is too large to calculate!"
```

---

## User-Friendly Error Messages 💬

### Bad Error Messages ❌

```python
# Technical jargon users don't understand
except ValueError:
    print("ValueError: invalid literal for int() with base 10")

except ZeroDivisionError:
    print("ZeroDivisionError: float division by zero")
```

### Good Error Messages ✅

```python
# Clear, helpful, actionable messages
except ValueError:
    print("❌ That doesn't look like a number. Please try again!")

except ZeroDivisionError:
    print("❌ Oops! Can't divide by zero. Please enter a different number!")
```

### Message Guidelines

- **Use emojis** for visual appeal
- **Be specific** about what went wrong
- **Be helpful** - suggest what to do next
- **Be polite** - don't blame the user

---

## Logging Errors for Debugging 📊

### Simple Error Logging

```python
import datetime

def log_error(error_message):
    timestamp = datetime.datetime.now()
    with open("calculator_errors.log", "a") as log_file:
        log_file.write(f"{timestamp}: {error_message}\n")

try:
    result = risky_calculation()
except Exception as e:
    log_error(f"Calculation failed: {e}")
    print("❌ Something went wrong. Please try again!")
```

### Debug Mode

```python
DEBUG_MODE = True  # Set to False for production

def debug_print(message):
    if DEBUG_MODE:
        print(f"🐛 DEBUG: {message}")

try:
    result = complex_calculation()
    debug_print(f"Calculation successful: {result}")
except Exception as e:
    debug_print(f"Error details: {e}")
    print("❌ Calculation failed!")
```

---

## Error Handling Best Practices 🏆

### Be Specific with Exceptions

```python
# Good ✅ - specific error handling
try:
    num = float(user_input)
except ValueError:
    print("❌ Please enter a valid number!")

# Bad ❌ - catches everything
try:
    num = float(user_input)
except:
    print("❌ Something went wrong!")
```

### Don't Ignore Errors

```python
# Bad ❌ - silent failure
try:
    result = risky_operation()
except:
    pass  # User has no idea something went wrong!

# Good ✅ - acknowledge and handle
try:
    result = risky_operation()
except Exception as e:
    print(f"❌ Operation failed: {e}")
    result = default_value
```

### Fail Fast When Appropriate

```python
def divide(x, y):
    # Check preconditions early
    if not isinstance(x, (int, float)):
        raise TypeError("x must be a number")
    if not isinstance(y, (int, float)):
        raise TypeError("y must be a number")
    if y == 0:
        raise ValueError("Cannot divide by zero")

    return x / y
```

---

## Testing Error Handling 🧪

### Manual Testing Scenarios

1. **Enter letters** instead of numbers
2. **Enter symbols** like @#$%
3. **Press Enter** without typing anything
4. **Enter extremely large** numbers
5. **Try division by zero**
6. **Press Ctrl+C** during input

### Automated Testing (Advanced)

```python
def test_safe_input():
    # This would be in a separate test file
    import io
    import sys

    # Test with invalid input
    sys.stdin = io.StringIO("hello\n5\n")
    result = safe_float_input("Enter number: ")
    assert result == 5.0
```

---

## Key Takeaways 📚

### What You Learned

- ✅ **try/except blocks** catch and handle errors
- ✅ **Input validation** prevents crashes
- ✅ **User-friendly messages** improve experience
- ✅ **Graceful error recovery** keeps program running
- ✅ **Professional error handling** separates good from great apps

### Next Up: Modules & Advanced Features!

- Import external libraries
- Use math module for advanced calculations
- Create scientific calculator features
- Add professional polish and formatting

**Your calculator is now bulletproof! 🛡️**
