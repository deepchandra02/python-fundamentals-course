# Python Escape Characters

## Overview
Escape characters in Python allow you to insert special characters into strings that would otherwise be difficult or impossible to include directly.

## Escape Character Syntax
- The escape character is a backslash `\` followed by another character
- Used to insert characters that are normally illegal in a string

## Common Escape Sequences

| Escape Code | Result |
|------------|--------|
| `\'` | Single Quote |
| `\\` | Backslash |
| `\n` | New Line |
| `\r` | Carriage Return |
| `\t` | Tab |
| `\b` | Backspace |
| `\f` | Form Feed |
| `\ooo` | Octal value |
| `\xhh` | Hex value |

## Example: Handling Quotes

### Problem: Quotes Inside Quotes
```python
# This will cause an error
txt = "We are the so-called "Vikings" from the north."
```

### Solution: Use Escape Character
```python
# Correct way to include quotes
txt = "We are the so-called \"Vikings\" from the north."
```

The escape character `\"` allows you to include double quotes within a double-quoted string without causing a syntax error.

## Key Takeaways
- Escape characters provide a way to include special characters in strings
- The backslash `\` is used to "escape" characters that would otherwise be interpreted differently
- Useful for inserting quotes, special formatting, and other non-standard characters