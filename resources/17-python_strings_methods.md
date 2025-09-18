# Python String Methods

Python provides a rich set of built-in string methods that allow you to manipulate and analyze strings. Here's a comprehensive overview:

## Key Characteristics
- All string methods return new values
- They do not modify the original string

## Common String Methods

### Case Manipulation
- `capitalize()`: Converts first character to uppercase
- `casefold()`: Converts entire string to lowercase
- `lower()`: Converts string to lowercase
- `upper()`: Converts string to uppercase
- `swapcase()`: Swaps case of characters
- `title()`: Capitalizes first letter of each word

### Searching and Checking
- `count()`: Returns number of times a value appears in string
- `find()`: Searches for a value and returns its position
- `index()`: Similar to find(), but raises an error if not found
- `startswith()`: Checks if string starts with specified value
- `endswith()`: Checks if string ends with specified value

### Validation Methods
- `isalnum()`: Checks if all characters are alphanumeric
- `isalpha()`: Checks if all characters are alphabetic
- `isdigit()`: Checks if all characters are digits
- `islower()`: Checks if all characters are lowercase
- `isupper()`: Checks if all characters are uppercase

### Modification Methods
- `strip()`: Removes whitespace from both sides
- `lstrip()`: Removes whitespace from left side
- `rstrip()`: Removes whitespace from right side
- `replace()`: Replaces specified values in string
- `split()`: Splits string into a list
- `join()`: Joins elements of an iterable

### Formatting
- `center()`: Centers the string
- `ljust()`: Left-justifies the string
- `rjust()`: Right-justifies the string
- `zfill()`: Fills string with zeros on the left

## Example Usage

```python
# Case manipulation
text = "hello world"
print(text.capitalize())  # "Hello world"
print(text.upper())       # "HELLO WORLD"

# Searching
sentence = "Python is awesome"
print(sentence.count("o"))  # 2
print(sentence.find("is"))  # 7

# Validation
name = "John123"
print(name.isalnum())  # True
print(name.isalpha())  # False

# Modification
data = "  apple,banana,cherry  "
print(data.strip())             # "apple,banana,cherry"
print(data.strip().split(","))  # ['apple', 'banana', 'cherry']
```

## Key Benefits
- Provide powerful string manipulation capabilities
- Easy to use and remember
- Return new strings, preserving original data
- Essential for text processing and data cleaning