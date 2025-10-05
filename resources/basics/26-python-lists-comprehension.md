# Python List Comprehension Tutorial

## What is List Comprehension?

List comprehension is a concise way to create new lists in Python based on existing lists, offering a more compact syntax compared to traditional `for` loops.

## Basic Syntax

```python
newlist = [expression for item in iterable if condition == True]
```

## Key Components

- **Expression**: The output or transformation of each item
- **Item**: The current element being processed
- **Iterable**: Any collection like a list, tuple, or range
- **Condition**: Optional filter (like an `if` statement)

## Examples

### Basic List Comprehension

```python
# Create a list of fruits with 'a'
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
# Result: ["banana", "apple", "mango"]
```

### Range Example

```python
# Create a list of numbers less than 5
newlist = [x for x in range(10) if x < 5]
# Result: [0, 1, 2, 3, 4]
```

### Transforming Values

```python
# Convert fruits to uppercase
newlist = [x.upper() for x in fruits]
# Result: ["APPLE", "BANANA", "CHERRY", "KIWI", "MANGO"]
```

### Conditional Expression

```python
# Replace "banana" with "orange"
newlist = [x if x != "banana" else "orange" for x in fruits]
```

## Key Benefits

- More readable and compact than traditional `for` loops
- Allows filtering and transforming lists in a single line
- Creates a new list without modifying the original

## Flexibility

List comprehensions can work with:
- Lists
- Tuples
- Sets
- Range objects
- Any iterable