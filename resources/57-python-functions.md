# Python Functions Tutorial

## Introduction to Functions

A function in Python is a block of reusable code that:
- Runs only when called
- Can accept parameters
- Can return data as a result

## Creating a Function

Functions are defined using the `def` keyword:

```python
def my_function():
    print("Hello from a function")
```

## Calling a Function

Call a function by using its name followed by parentheses:

```python
my_function()  # Calls the function
```

## Arguments and Parameters

### Basic Arguments
Functions can accept arguments passed inside parentheses:

```python
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
```

### Arbitrary Arguments (`*args`)
When you don't know how many arguments will be passed:

```python
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
```

### Keyword Arguments
Arguments can be passed with key-value syntax:

```python
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1="Emil", child2="Tobias", child3="Linus")
```

## Return Values

Use the `return` statement to send a value back from a function:

```python
def my_function(x):
    return 5 * x

print(my_function(3))  # Outputs 15
```

## Special Argument Types

### Positional-Only Arguments
Use `, /` to specify only positional arguments:

```python
def my_function(x, /):
    print(x)

my_function(3)  # Valid
# my_function(x=3)  # Would raise an error
```

### Keyword-Only Arguments
Use `*, ` to specify only keyword arguments:

```python
def my_function(*, x):
    print(x)

my_function(x=3)  # Valid
# my_function(3)  # Would raise an error
```

## Key Takeaways
- Functions provide code reusability
- Use `def` to define functions
- Functions can accept various argument types
- `return` statement sends values back from functions
- Arguments can be positional or keyword-based