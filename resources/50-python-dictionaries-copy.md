# Python Dictionary Copying

## Overview
When copying dictionaries in Python, simply using `dict2 = dict1` creates a reference, not a true copy. Changes to the original dictionary will affect the referenced dictionary.

## Methods to Copy Dictionaries

### 1. Using `.copy()` Method
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
```

### 2. Using `dict()` Function
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
```

## Key Points
- `.copy()` method creates a shallow copy of the dictionary
- `dict()` function is another way to create a new dictionary with the same key-value pairs
- Both methods prevent modifications to the original dictionary from affecting the new dictionary

## Best Practices
- Always use `.copy()` or `dict()` when you want a separate copy of a dictionary
- Be aware that these methods create shallow copies (nested objects may still reference the original)