# Python List Access Tutorial

## Accessing List Items

In Python, list items are indexed, allowing you to access them by their index number.

### Basic Indexing

```python
thislist = ["apple", "banana", "cherry"]
print(thislist[1])  # Prints "banana"
```

Key points:
- Indexing starts at 0
- The first item is at index 0
- The second item is at index 1

### Negative Indexing

Negative indexing allows you to access items from the end of the list:

```python
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])  # Prints "cherry" (last item)
```

- `-1` refers to the last item
- `-2` refers to the second-last item

### Accessing a Range of Items

You can select a range of items using slice notation:

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])  # Prints ["cherry", "orange", "kiwi"]
```

Slice notation rules:
- `[start:end]` - includes start index, excludes end index
- Leaving start blank starts from the beginning
- Leaving end blank goes to the end of the list

### Negative Index Range

You can also use negative indexes in ranges:

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])  # Prints ["orange", "kiwi", "melon"]
```

### Checking Item Existence

Use the `in` keyword to check if an item is in the list:

```python
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
```

## Key Takeaways
- Python list indexing starts at 0
- Negative indexes count from the end of the list
- Slice notation allows flexible item selection
- The `in` keyword helps check for item presence