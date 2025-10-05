# Python Sets Tutorial

## Introduction to Sets

A set in Python is a collection with the following key characteristics:
- Unordered
- Unchangeable*
- Unindexed
- No duplicate values allowed

*Note: Set items are technically unchangeable, but you can remove and add new items.

## Creating a Set

Sets are created using curly brackets:

```python
thisset = {"apple", "banana", "cherry"}
print(thisset)
```

## Key Characteristics

### Unordered
- Set items do not have a defined order
- Items can appear in different orders each time
- Cannot be referenced by index or key

### Unchangeable
- Cannot modify existing set items
- Can remove and add new items

### No Duplicates
Duplicate values are automatically ignored:

```python
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)  # Will only show unique values
```

### Special Duplicate Handling
- `True` and `1` are considered the same value
- `False` and `0` are considered the same value

## Set Properties

### Length
Use `len()` to get the number of items:

```python
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
```

### Data Types
Sets can contain mixed data types:

```python
set1 = {"abc", 34, True, 40, "male"}
```

### Constructor Method
You can also create sets using the `set()` constructor:

```python
thisset = set(("apple", "banana", "cherry"))
```

## Comparison with Other Collections

Python has four main collection types:
1. List: Ordered, changeable, allows duplicates
2. Tuple: Ordered, unchangeable, allows duplicates
3. Set: Unordered, unchangeable*, no duplicates
4. Dictionary: Ordered**, changeable, no duplicates

*Set items are unchangeable, but you can remove/add items
**Dictionaries are ordered in Python 3.7+

## Best Practices

When choosing a collection type, consider:
- Meaning preservation
- Efficiency
- Security requirements