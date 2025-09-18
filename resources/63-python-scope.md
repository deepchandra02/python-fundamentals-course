# Python Scope

Python scope determines the accessibility and lifetime of variables within different parts of a program. Here's a comprehensive overview:

## Local Scope

A variable created inside a function is only available within that function.

```python
def myfunc():
    x = 300  # Local variable
    print(x)  # This works

myfunc()
```

### Nested Function Scope

Inner functions can access variables from the outer function:

```python
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)  # Can access outer function's variable
    myinnerfunc()
```

## Global Scope

Variables created in the main body of the code are global and accessible everywhere:

```python
x = 300  # Global variable

def myfunc():
    print(x)  # Can access global variable

myfunc()
print(x)  # Also works outside the function
```

### Variable Naming Conflicts

When using the same variable name inside and outside a function, Python treats them as separate variables:

```python
x = 300  # Global x

def myfunc():
    x = 200  # Local x
    print(x)  # Prints 200

myfunc()
print(x)  # Prints 300
```

## Global Keyword

Use `global` to modify a global variable inside a function:

```python
x = 300

def myfunc():
    global x
    x = 200  # Modifies the global x

myfunc()
print(x)  # Prints 200
```

## Nonlocal Keyword

The `nonlocal` keyword is used in nested functions to work with variables in the outer (enclosing) function:

```python
def myfunc1():
    x = "Jane"
    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x

print(myfunc1())  # Prints "hello"
```

Key Takeaways:
- Local scope is limited to the function where a variable is created
- Global scope allows variables to be accessed throughout the entire program
- The `global` keyword allows modification of global variables inside functions
- The `nonlocal` keyword works with variables in nested function scopes