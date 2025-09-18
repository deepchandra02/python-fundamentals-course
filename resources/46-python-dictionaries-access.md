# Python Dictionary Access Tutorial

## Accessing Dictionary Items

In Python, you can access dictionary items using two primary methods:

### 1. Square Bracket Notation
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]  # Directly access value by key
```

### 2. get() Method
```python
x = thisdict.get("model")  # Alternative way to access value
```

## Getting Dictionary Keys and Values

### Keys Method
```python
x = thisdict.keys()  # Returns a view of all dictionary keys
```

### Values Method
```python
x = thisdict.values()  # Returns a view of all dictionary values
```

### Items Method
```python
x = thisdict.items()  # Returns a list of key-value tuple pairs
```

## Checking Key Existence

### Using 'in' Keyword
```python
if "model" in thisdict:
    print("Key exists in dictionary")
```

## Key Characteristics

- Keys and values lists are "views" of the dictionary
- Changes to the original dictionary are reflected in these views
- You can dynamically add or modify dictionary items

### Example of Dynamic Updates
```python
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.keys()
car["color"] = "white"  # Adding a new key updates the keys view
```

## Best Practices
- Use `.get()` method to safely retrieve values
- Check key existence before accessing
- Use `.keys()`, `.values()`, and `.items()` for iteration and inspection