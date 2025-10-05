# Python Sets: Adding Items

## Adding a Single Item
To add a single item to a set, use the `add()` method:

```python
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
```

## Adding Multiple Items from Another Set
Use the `update()` method to add items from another set:

```python
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
```

## Adding Items from Any Iterable
The `update()` method can add items from various iterable objects like lists, tuples, or dictionaries:

```python
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
```

## Key Characteristics
- Sets are unordered collections of unique elements
- You cannot change existing items in a set
- You can only add new items using `add()` or `update()`

## Methods for Adding Items
1. `add()`: Adds a single item
2. `update()`: Adds multiple items from any iterable

Remember that sets automatically eliminate duplicate values, so adding an existing item will have no effect.