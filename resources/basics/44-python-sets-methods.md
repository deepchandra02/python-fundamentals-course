# Python Set Methods

Python provides a robust set of built-in methods for manipulating sets. Here's a comprehensive overview:

## Key Set Methods

| Method | Description | Shortcut |
|--------|-------------|----------|
| `add()` | Adds an element to the set | - |
| `clear()` | Removes all elements from the set | - |
| `copy()` | Returns a copy of the set | - |
| `difference()` | Returns elements in one set but not another | `-` |
| `intersection()` | Returns common elements between sets | `&` |
| `pop()` | Removes and returns an arbitrary element | - |
| `remove()` | Removes a specific element | - |
| `union()` | Combines sets, returning all unique elements | `|` |

## Important Set Operations

### Adding and Removing Elements
- `add()`: Adds a single element to the set
- `remove()`: Removes a specific element (raises error if not found)
- `discard()`: Removes an element if it exists (no error if not found)

### Set Comparisons
- `issubset()`: Checks if all elements are in another set
- `issuperset()`: Checks if a set contains all elements of another set
- `isdisjoint()`: Checks if sets have no common elements

### Set Modifications
- `difference_update()`: Removes elements found in another set
- `intersection_update()`: Keeps only elements common to sets
- `symmetric_difference()`: Returns elements in either set, but not both

## Example Usage

```python
# Creating sets
fruits1 = {"apple", "banana", "cherry"}
fruits2 = {"banana", "orange", "kiwi"}

# Union
all_fruits = fruits1.union(fruits2)  # or fruits1 | fruits2

# Intersection
common_fruits = fruits1.intersection(fruits2)  # or fruits1 & fruits2

# Difference
unique_fruits1 = fruits1.difference(fruits2)  # or fruits1 - fruits2
```

This overview covers the most commonly used set methods in Python programming.