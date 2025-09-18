# Python Dictionaries Tutorial

## Introduction to Dictionaries

A dictionary in Python is a collection that stores data in key:value pairs with the following key characteristics:

### Key Features
- Ordered (since Python 3.7)
- Changeable
- Do not allow duplicate keys
- Written with curly brackets `{}`

### Basic Dictionary Example

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
```

## Dictionary Fundamentals

### Creating a Dictionary
You can create a dictionary in two primary ways:
1. Using curly braces `{}`
2. Using the `dict()` constructor

```python
# Using curly braces
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Using dict() constructor
thisdict = dict(name="John", age=36, country="Norway")
```

### Dictionary Characteristics

#### Data Types
Dictionary values can be of any data type:
- Strings
- Integers
- Booleans
- Lists

```python
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
```

#### Length
Use `len()` to determine the number of items:

```python
print(len(thisdict))
```

#### Checking Type
Use `type()` to confirm it's a dictionary:

```python
print(type(thisdict))  # <class 'dict'>
```

## Important Considerations

### Duplicates
- Duplicate keys are not allowed
- A duplicate key will overwrite the previous value

### Ordering
- In Python 3.7+, dictionaries maintain insertion order
- In Python 3.6 and earlier, dictionaries were unordered

## Python Collections Comparison

Python has four main collection types:
1. **List**: Ordered, changeable, allows duplicates
2. **Tuple**: Ordered, unchangeable, allows duplicates
3. **Set**: Unordered, unchangeable*, no duplicates
4. **Dictionary**: Ordered**, changeable, no duplicates

*Set items are unchangeable, but you can add/remove items
**Ordered as of Python 3.7+