# Python Variables: Assigning Multiple Values

## Multiple Values to Multiple Variables

In Python, you can assign multiple values to multiple variables in a single line:

```python
x, y, z = "Orange", "Banana", "Cherry"
```

**Key Point**: The number of variables must match the number of values, or an error will occur.

## One Value to Multiple Variables

You can also assign the same value to multiple variables simultaneously:

```python
x = y = z = "Orange"
```

## Unpacking Collections

Python allows you to extract values from collections like lists and tuples:

```python
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
```

### Important Considerations

- Ensure the number of variables matches the number of values
- This technique works with lists, tuples, and other iterable collections
- Unpacking is a powerful way to assign multiple variables quickly

## Best Practices

- Use meaningful variable names
- Keep the number of variables and values consistent
- Utilize unpacking for clean, concise code

## Example Scenarios

```python
# Multiple different values
colors = "red", "green", "blue"

# Same value assignment
default_status = status = active = False

# List unpacking
coordinates = [10, 20, 30]
x, y, z = coordinates
```

This approach provides a flexible and readable way to assign multiple variables in Python.