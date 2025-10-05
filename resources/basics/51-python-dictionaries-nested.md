# Python Nested Dictionaries

## What are Nested Dictionaries?

A nested dictionary is a dictionary that contains one or more dictionaries as its values. This allows you to create complex, hierarchical data structures in Python.

## Creating Nested Dictionaries

### Method 1: Direct Creation
```python
myfamily = {
  "child1": {
    "name": "Emil",
    "year": 2004
  },
  "child2": {
    "name": "Tobias",
    "year": 2007
  },
  "child3": {
    "name": "Linus",
    "year": 2011
  }
}
```

### Method 2: Combining Separate Dictionaries
```python
child1 = {
  "name": "Emil",
  "year": 2004
}
child2 = {
  "name": "Tobias",
  "year": 2007
}
child3 = {
  "name": "Linus",
  "year": 2011
}

myfamily = {
  "child1": child1,
  "child2": child2,
  "child3": child3
}
```

## Accessing Nested Dictionary Items

To access items in a nested dictionary, use multiple square bracket notations:

```python
# Print the name of child 2
print(myfamily["child2"]["name"])
```

## Looping Through Nested Dictionaries

You can iterate through nested dictionaries using the `items()` method:

```python
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
```

This approach allows you to access both the keys of the outer dictionary and the keys and values of the inner dictionaries.

## Key Takeaways
- Nested dictionaries can represent complex, hierarchical data
- Access nested items using multiple square bracket notations
- Use `items()` method to loop through nested dictionaries
- Useful for organizing related information in a structured way