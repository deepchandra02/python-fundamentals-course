# Python Global Variables

## Overview

Global variables in Python are variables created outside of functions that can be accessed both inside and outside function scopes.

## Key Concepts

### Global Variable Basics

- Variables created outside functions are global variables
- Global variables can be used by everyone, both inside and outside functions

### Example of a Global Variable

```python
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()  # Prints: Python is awesome
```

### Local vs Global Variables

When you create a variable with the same name inside a function, it becomes a local variable:

```python
x = "awesome"

def myfunc():
    x = "fantastic"  # This is a local variable
    print("Python is " + x)  # Prints: Python is fantastic

myfunc()
print("Python is " + x)  # Prints: Python is awesome
```

## The `global` Keyword

The `global` keyword allows you to:
- Create a global variable inside a function
- Modify a global variable from within a function

### Creating a Global Variable

```python
def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)  # Prints: Python is fantastic
```

### Modifying a Global Variable

```python
x = "awesome"

def myfunc():
    global x
    x = "fantastic"  # Changes the global variable

myfunc()
print("Python is " + x)  # Prints: Python is fantastic
```

## Best Practices

- Use global variables sparingly
- Prefer passing variables as function parameters
- Be cautious of potential naming conflicts
- Consider using classes or modules for better variable management

## Learning Highlights

- Global variables are accessible everywhere in your code
- Local variables are confined to their function
- The `global` keyword provides explicit control over variable scope