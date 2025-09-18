# Python Variable Names: A Comprehensive Guide

## Basic Rules for Variable Names

Python has specific rules for creating valid variable names:

1. **Starting Characters**
   - Must start with a letter or underscore character
   - Cannot start with a number

2. **Allowed Characters**
   - Can only contain alpha-numeric characters and underscores
   - Supports A-z, 0-9, and _

3. **Case Sensitivity**
   - Variables are case-sensitive
   - `age`, `Age`, and `AGE` are considered different variables

4. **Reserved Keywords**
   - Cannot use Python's reserved keywords as variable names

## Legal Variable Name Examples

```python
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
```

## Illegal Variable Name Examples

```python
# These will cause errors
2myvar = "John"  # Cannot start with a number
my-var = "John"  # Cannot use hyphens
my var = "John"  # Cannot use spaces
```

## Naming Conventions

### Camel Case
Each word, except the first, starts with a capital letter:
```python
myVariableName = "John"
```

### Pascal Case
Each word starts with a capital letter:
```python
MyVariableName = "John"
```

### Snake Case
Words are separated by underscore characters:
```python
my_variable_name = "John"
```

## Best Practices

- Choose descriptive names that explain the variable's purpose
- Use lowercase with underscores for most variable names
- Be consistent in your naming style throughout your project

## Pro Tip

Remember that clear, readable variable names make your code more understandable and maintainable.