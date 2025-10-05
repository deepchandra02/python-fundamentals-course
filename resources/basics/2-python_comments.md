# Python Comments Tutorial

## Overview
Comments in Python are used to:
- Explain code
- Make code more readable
- Prevent code execution during testing

## Creating Comments

### Single-Line Comments
Comments start with a `#` symbol and are ignored by Python:

```python
# This is a comment
print("Hello, World!")

print("Hello, World!")  # Comment at end of line
```

### Preventing Code Execution
Comments can temporarily disable code:

```python
# print("Hello, World!")
print("Cheers, Mate!")
```

## Multiline Comments

### Method 1: Multiple `#` Lines
```python
# This is a comment
# written in
# more than just one line
print("Hello, World!")
```

### Method 2: Multiline String
```python
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")
```

## Key Points
- Comments start with `#`
- Multiline comments can use multiple `#` or triple quotes
- Comments are ignored by Python interpreter
- Use comments to explain complex code or temporarily disable code

## Best Practices
- Write clear, concise comments
- Explain "why" something is done, not just "what" is happening
- Don't overuse comments - good code should be self-explanatory