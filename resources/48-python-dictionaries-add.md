# Python Dictionary: Adding Items

## Adding Items to a Dictionary

In Python, you can add items to a dictionary in two primary ways:

### 1. Direct Assignment

You can add a new item to a dictionary by using a new index key and assigning a value:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
```

### 2. Using the `update()` Method

The `update()` method allows you to add an item or multiple items to a dictionary:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
```

Key characteristics of adding dictionary items:
- Direct assignment creates a new key-value pair if the key doesn't exist
- The `update()` method can add single or multiple items
- The argument for `update()` must be another dictionary or an iterable with key-value pairs

## Best Practices
- Use direct assignment for single item additions
- Use `update()` when adding multiple items or when working with another dictionary
- Always ensure the key is unique to avoid overwriting existing values