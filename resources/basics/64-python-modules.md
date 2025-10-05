# Python Modules Tutorial

## What is a Module?

A module in Python is essentially a code library - a file containing a set of functions and variables that you want to include in your application.

## Creating a Module

To create a module, simply save your code in a file with a `.py` extension. Here's a basic example:

```python
# mymodule.py
def greeting(name):
    print("Hello, " + name)

person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}
```

## Using a Module

### Importing a Whole Module

```python
import mymodule

# Call a function from the module
mymodule.greeting("Jonathan")

# Access a variable from the module
age = mymodule.person1["age"]
print(age)
```

### Creating an Alias

You can rename a module when importing:

```python
import mymodule as mx

a = mx.person1["age"]
print(a)
```

### Importing Specific Parts

```python
from mymodule import person1

print(person1["age"])
```

## Built-in Modules

Python comes with several built-in modules you can use:

```python
import platform

# Get system information
x = platform.system()
print(x)
```

## Exploring Module Contents

Use the `dir()` function to list all names in a module:

```python
import platform

x = dir(platform)
print(x)
```

## Key Takeaways

- Modules help organize and reuse code
- You can create your own modules or use built-in Python modules
- Import entire modules or specific parts
- Use `dir()` to explore module contents
- Modules can contain functions, variables, and more