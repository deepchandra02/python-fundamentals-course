# Python Inheritance Tutorial

## Overview
Inheritance in Python allows you to create a new class that inherits methods and properties from an existing class. There are two key terms to understand:

- **Parent Class (Base Class)**: The original class being inherited from
- **Child Class (Derived Class)**: The new class that inherits from the parent class

## Basic Inheritance Example

```python
# Parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Child class
class Student(Person):
    pass  # Inherits everything from Person class
```

## Adding the `__init__()` Function

When you add an `__init__()` function to the child class, it overrides the parent's `__init__()`. To maintain parent class initialization, you have two methods:

### 1. Explicitly Call Parent `__init__()`
```python
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
```

### 2. Use `super()` Function (Recommended)
```python
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
```

## Adding Properties and Methods

```python
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print(f"Welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}")
```

## Key Inheritance Concepts

1. Child classes inherit all methods and properties from the parent class
2. You can override parent methods by redefining them in the child class
3. The `super()` function provides an easy way to call methods from the parent class
4. You can add new properties and methods to child classes

## Best Practices

- Use `super()` for calling parent class methods
- Only override methods when you need different behavior
- Keep inheritance hierarchies simple and logical