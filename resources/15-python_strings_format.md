# Python String Formatting

Python offers multiple ways to format strings, with F-Strings being the most modern and preferred method.

## F-Strings (Formatted String Literals)

Introduced in Python 3.6, F-Strings provide a concise way to embed expressions inside string literals.

### Basic Syntax
```python
age = 36
txt = f"My name is John, I am {age}"
print(txt)
```

### Features

1. **Placeholders**
   - Use curly brackets `{}` to insert variables
   ```python
   price = 59
   txt = f"The price is {price} dollars"
   ```

2. **Modifiers**
   - Format values with modifiers after a colon
   ```python
   price = 59
   txt = f"The price is {price:.2f} dollars"  # Displays 2 decimal places
   ```

3. **Inline Expressions**
   - Can include Python code directly in placeholders
   ```python
   txt = f"The price is {20 * 59} dollars"
   ```

## Key Points
- Prefix the string with `f` to create an F-String
- Placeholders can contain:
  - Variables
  - Expressions
  - Function calls
  - Mathematical operations
- Modifiers allow precise formatting of values

## Alternatives
While F-Strings are recommended, older methods like `.format()` still exist for compatibility with earlier Python versions.