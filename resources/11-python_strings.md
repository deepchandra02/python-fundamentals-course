# Python Strings Tutorial

## Basic String Concepts

### String Definition
Strings in Python are sequences of Unicode characters, defined using either single or double quotes:

```python
# These are equivalent
print("Hello")
print('Hello')
```

### Creating Strings
You can create strings in multiple ways:

1. Single-line strings
```python
a = "Hello, World!"
```

2. Multiline strings (using triple quotes)
```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
```

### String Characteristics

- Strings are arrays of characters
- No separate character data type
- Single characters are strings of length 1
- Can be accessed using square bracket indexing

## String Operations

### Accessing Characters
```python
a = "Hello, World!"
print(a[1])  # Prints 'e' (first character is at index 0)
```

### Looping Through Strings
```python
for x in "banana":
    print(x)  # Prints each character on a new line
```

### String Length
```python
a = "Hello, World!"
print(len(a))  # Prints the number of characters
```

### String Membership
```python
txt = "The best things in life are free!"
print("free" in txt)  # Returns True or False
```

### Conditional String Checking
```python
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
```

## Key Takeaways
- Strings can use single or double quotes
- Multiline strings use triple quotes
- Strings are zero-indexed
- Many built-in methods for string manipulation
- Easy to check string contents using `in` and `not in`