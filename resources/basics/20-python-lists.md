# Python Lists Tutorial

## Introduction to Lists

Lists in Python are a versatile data structure used to store multiple items in a single variable. They have several key characteristics:

### Key Characteristics
- Ordered collection of items
- Changeable (can modify after creation)
- Allow duplicate values
- Indexed (first item at index 0)

### Creating a List
```python
# Basic list creation
thislist = ["apple", "banana", "cherry"]
```

### List Properties

#### Ordered
- Items have a defined order
- New items are added at the end
- Order remains consistent (with some method exceptions)

#### Changeable
- Can add, remove, and modify items after creation

#### Duplicate Values Allowed
```python
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
```

### List Length
```python
thislist = ["apple", "banana", "cherry"]
print(len(thislist))  # Prints number of items
```

### Data Types in Lists
Lists can contain mixed data types:
```python
# Different data type examples
list1 = ["apple", "banana", "cherry"]  # Strings
list2 = [1, 5, 7, 9, 3]  # Integers
list3 = [True, False, False]  # Booleans
mixed_list = ["abc", 34, True, 40, "male"]  # Mixed types
```

### List Constructor
```python
# Using list() constructor
thislist = list(("apple", "banana", "cherry"))
```

## Python Collections Overview
Python has four main collection types:
1. **List**: Ordered, changeable, allows duplicates
2. **Tuple**: Ordered, unchangeable, allows duplicates
3. **Set**: Unordered, unchangeable, no duplicates
4. **Dictionary**: Ordered, changeable, no duplicates

### Checking List Type
```python
mylist = ["apple", "banana", "cherry"]
print(type(mylist))  # Prints <class 'list'>
```

## Practical Considerations
- Choose list when you need an ordered, mutable collection
- Consider performance and use case when selecting collection type
- Lists are ideal for storing related items that may change over time