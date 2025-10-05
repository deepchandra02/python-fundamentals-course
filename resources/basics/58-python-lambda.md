# Python Lambda Functions

## Overview
A lambda function is a small, anonymous function in Python that can:
- Take any number of arguments
- Contain only one expression
- Return the result of that expression

## Basic Syntax
```python
lambda arguments : expression
```

## Simple Examples

### Adding 10 to an argument
```python
x = lambda a : a + 10
print(x(5))  # Outputs: 15
```

### Multiplying arguments
```python
x = lambda a, b : a * b
print(x(5, 6))  # Outputs: 30
```

### Summing multiple arguments
```python
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))  # Outputs: 13
```

## Advanced Usage: Function Generator

Lambda functions are powerful when used inside other functions to create specialized functions dynamically:

```python
def myfunc(n):
    return lambda a : a * n

# Create functions that double or triple numbers
mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))  # Outputs: 22
print(mytripler(11))  # Outputs: 33
```

## Key Takeaways
- Use lambda for short, one-time use functions
- Ideal for creating quick, anonymous functions
- Can be passed as arguments to higher-order functions
- Useful for functional programming techniques