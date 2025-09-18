# Python Tuples Tutorial

## What are Tuples?

Tuples are a built-in Python data type used to store multiple items in a single variable. Key characteristics include:

- Ordered collection of items
- Unchangeable (immutable)
- Allow duplicate values
- Created using round brackets `()`

### Basic Tuple Creation

```python
# Creating a tuple
mytuple = ("apple", "banana", "cherry")
```

## Key Properties

### 1. Ordered
- Items have a defined order that won't change
- First item has index `[0]`, second item has index `[1]`, etc.

### 2. Unchangeable
- Cannot modify, add, or remove items after creation

### 3. Allows Duplicates
```python
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
```

### 4. Length
```python
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))  # Prints number of items
```

## Creating Tuples

### Single Item Tuple
```python
# Must include a comma
thistuple = ("apple",)  # This is a tuple
thistuple = ("apple")   # This is NOT a tuple
```

### Different Data Types
```python
# Tuples can contain mixed data types
tuple1 = ("abc", 34, True, 40, "male")
```

### Using tuple() Constructor
```python
thistuple = tuple(("apple", "banana", "cherry"))
```

## Comparison with Other Collections

Python has four main collection types:
- **List**: Ordered and changeable, allows duplicates
- **Tuple**: Ordered and unchangeable, allows duplicates
- **Set**: Unordered, unchangeable*, no duplicates
- **Dictionary**: Ordered** and changeable, no duplicates

*Set items are unchangeable, but you can add/remove items
**Ordered as of Python 3.7

## Best Practices

- Use tuples when you want an immutable sequence of items
- Tuples are more memory efficient than lists
- Useful for storing related, unchanging data