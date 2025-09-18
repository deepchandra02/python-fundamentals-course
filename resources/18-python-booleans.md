# Python Booleans Tutorial

## Overview
Booleans in Python represent two values: `True` or `False`. They are fundamental for evaluating conditions and controlling program flow.

## Basic Boolean Concepts

### Boolean Values
Booleans are the result of comparing values or evaluating expressions:

```python
print(10 > 9)   # Returns True
print(10 == 9)  # Returns False
print(10 < 9)   # Returns False
```

### Evaluating Values
The `bool()` function can evaluate any value:

```python
print(bool("Hello"))  # Returns True
print(bool(15))       # Returns True
```

## Truthy and Falsy Values

### Most Values are True
Almost any value is considered `True` if it has content:
- Non-empty strings
- Non-zero numbers
- Non-empty lists, tuples, sets, and dictionaries

### Falsy Values
Values that evaluate to `False`:
- Empty strings `""`
- `0`
- `None`
- Empty collections `()`, `[]`, `{}`
- `False`

## Boolean Functions and Comparisons

### Creating Boolean Functions
You can create functions that return boolean values:

```python
def myFunction():
    return True

print(myFunction())  # Prints True

if myFunction():
    print("YES!")
else:
    print("NO!")
```

### Built-in Boolean Checks
Python has built-in functions like `isinstance()` that return boolean values:

```python
x = 200
print(isinstance(x, int))  # Returns True
```

## Key Takeaways
- Booleans are fundamental for conditional logic
- Most values are considered `True`
- Only specific empty or zero values are `False`
- You can create and use boolean functions
- Comparison operators return boolean values