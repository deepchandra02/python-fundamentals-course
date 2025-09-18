# Python - Adding List Items

Python provides several methods to add items to lists:

## 1. Append Items
Use the `append()` method to add an item to the end of a list:

```python
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)  # Outputs: ["apple", "banana", "cherry", "orange"]
```

## 2. Insert Items
Use the `insert()` method to add an item at a specific index:

```python
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)  # Outputs: ["apple", "orange", "banana", "cherry"]
```

## 3. Extend List
Use the `extend()` method to add elements from another list or iterable:

```python
# Adding from another list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)  # Outputs: ["apple", "banana", "cherry", "mango", "pineapple", "papaya"]

# Adding from a tuple
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)  # Outputs: ["apple", "banana", "cherry", "kiwi", "orange"]
```

Key points:
- `append()` adds a single item to the end of the list
- `insert()` adds an item at a specific index
- `extend()` can add elements from lists, tuples, sets, and other iterables
- Elements are added to the end of the list when using `extend()`