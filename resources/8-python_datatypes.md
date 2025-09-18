# Python Data Types

## Overview

In Python, data types are fundamental to understanding how variables store and manipulate different kinds of information. Python has several built-in data types categorized as follows:

## Built-in Data Types

### Text Type
- `str` (String)

### Numeric Types
- `int` (Integer)
- `float` (Floating-point number)
- `complex` (Complex number)

### Sequence Types
- `list`
- `tuple`
- `range`

### Mapping Type
- `dict` (Dictionary)

### Set Types
- `set`
- `frozenset`

### Boolean Type
- `bool`

### Binary Types
- `bytes`
- `bytearray`
- `memoryview`

### None Type
- `NoneType`

## Determining Data Type

You can find the data type of any object using the `type()` function:

```python
x = 5
print(type(x))  # Outputs the type of x
```

## Setting Data Types

### Automatic Type Assignment
Python automatically assigns data types when you assign a value:

```python
x = "Hello World"  # str
x = 20  # int
x = 20.5  # float
x = ["apple", "banana", "cherry"]  # list
```

### Explicit Type Conversion
You can also explicitly specify data types using constructor functions:

```python
x = str("Hello World")
x = int(20)
x = list(("apple", "banana", "cherry"))
```

## Key Takeaways
- Data types define the kind of data a variable can store
- Python automatically assigns types
- You can convert between types using constructor functions
- Understanding data types is crucial for effective Python programming