# Python - Remove List Items

Python provides several methods to remove items from lists:

## Remove Specified Item
Use the `remove()` method to delete a specific item:

```python
# Remove first occurrence of an item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)  # Output: ["apple", "cherry"]
```

## Remove by Index
Use `pop()` to remove an item at a specific index:

```python
# Remove item at index 1
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)  # Removes "banana"
print(thislist)  # Output: ["apple", "cherry"]

# Remove last item if no index specified
thislist = ["apple", "banana", "cherry"]
thislist.pop()  # Removes "cherry"
```

## Delete Using del Keyword
The `del` keyword can remove specific items or entire lists:

```python
# Remove first item
thislist = ["apple", "banana", "cherry"]
del thislist[0]  # Removes "apple"

# Delete entire list
del thislist
```

## Clear the List
Use `clear()` to empty the list while keeping the list object:

```python
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)  # Output: []
```

Key points:
- `remove()` removes the first occurrence of a specified item
- `pop()` removes by index (last item by default)
- `del` can remove specific items or entire lists
- `clear()` empties the list contents