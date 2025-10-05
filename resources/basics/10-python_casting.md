# Python Casting: Type Conversion Guide

## Overview
Python casting allows you to specify and convert variable types using constructor functions. This process transforms data between different types like integers, floats, and strings.

## Casting Methods

### Integer Casting (`int()`)
Converts values to whole numbers:
```python
x = int(1)    # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3
```

### Float Casting (`float()`)
Converts values to decimal numbers:
```python
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
```

### String Casting (`str()`)
Converts various data types to strings:
```python
x = str("s1")  # x will be 's1'
y = str(2)     # y will be '2'
z = str(3.0)   # z will be '3.0'
```

## Key Takeaways
- Casting helps explicitly define variable types
- Constructor functions (`int()`, `float()`, `str()`) are used for conversion
- Conversion can happen between numbers and strings
- Decimal values are truncated when converting to integers