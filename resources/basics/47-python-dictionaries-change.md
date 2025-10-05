# Python Dictionary Item Modification

## Changing Dictionary Values

In Python, you can change the value of a dictionary item by referring to its key name:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018  # Changes the value of "year"
```

## Updating Dictionaries

The `update()` method provides another way to modify dictionary values:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})  # Updates the "year" value
```

### Key Points:
- Use square bracket notation `dict["key"] = new_value` to change a specific item
- The `update()` method can modify one or multiple dictionary items
- The `update()` method takes a dictionary or an iterable of key-value pairs as an argument

## Best Practices
- Always ensure the key exists before trying to modify its value
- Use `update()` when you want to change multiple values at once
- Be careful not to introduce typos in key names when changing values