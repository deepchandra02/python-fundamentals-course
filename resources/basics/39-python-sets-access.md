# Python Sets: Accessing Items

## Key Characteristics of Set Access

Sets in Python have unique access properties:
- You cannot access items by index or key
- Sets are unordered collections
- You can iterate through sets or check item membership

## Accessing Set Items

### Looping Through a Set

```python
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)
```

This example demonstrates how to loop through all items in a set.

### Checking Item Membership

#### Checking if an Item is Present

```python
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)  # Returns True
```

#### Checking if an Item is NOT Present

```python
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)  # Returns False
```

## Important Notes

- Sets are mutable, but their items cannot be changed after creation
- You can add new items to a set, but cannot modify existing items
- Set membership checks are very efficient

## Best Practices

- Use `in` and `not in` for quick membership tests
- Use `for` loops to iterate through set contents
- Remember that sets are unordered, so iteration order is not guaranteed