# Removing Items from Python Sets

Python provides several methods to remove items from sets:

## 1. remove() Method
- Removes a specific item from the set
- Raises an error if the item does not exist

```python
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
```

## 2. discard() Method
- Removes a specific item from the set
- Does NOT raise an error if the item does not exist

```python
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
```

## 3. pop() Method
- Removes a random item from the set
- Returns the removed item
- Useful when you don't care which specific item is removed

```python
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
```

## 4. clear() Method
- Empties the entire set, leaving an empty set

```python
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
```

## 5. del Keyword
- Completely deletes the set

```python
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)  # This will raise an error
```

**Important Notes:**
- Sets are unordered, so `pop()` removes a random item
- `remove()` will raise an error for non-existent items
- `discard()` will not raise an error for non-existent items