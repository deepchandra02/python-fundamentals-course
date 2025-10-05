# Python - Copying Lists

In Python, simply assigning a list to a new variable (`list2 = list1`) does not create a copy. Instead, it creates a reference to the original list, meaning changes to the original list will affect the new list.

## Methods to Copy a List

### 1. Using `copy()` Method
```python
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
```

### 2. Using `list()` Function
```python
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
```

### 3. Using Slice Operator
```python
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
```

## Key Points
- All three methods create a new list with the same elements
- The new list is independent of the original list
- Modifications to the new list will not affect the original list

Each method provides a way to create a true copy of a list, allowing you to work with the new list without impacting the original list's contents.