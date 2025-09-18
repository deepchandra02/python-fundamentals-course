# Python Classes and Objects

Python is an object-oriented programming language where almost everything is an object with properties and methods. Here's a comprehensive guide to understanding Python classes:

## Creating a Class

A class is like a blueprint for creating objects. Here's a basic class definition:

```python
class MyClass:
    x = 5
```

## Creating Objects

You can create objects from a class:

```python
p1 = MyClass()
print(p1.x)  # Outputs: 5
```

## The `__init__()` Method

The `__init__()` method is a special method that initializes object properties when the object is created:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)  # Outputs: John
print(p1.age)   # Outputs: 36
```

## The `__str__()` Method

This method defines how the object should be represented as a string:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"
```

## Creating Methods

You can define methods inside a class:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()  # Calls the method
```

## The `self` Parameter

`self` is a reference to the current instance of the class:
- It must be the first parameter of any method
- It allows access to the object's attributes
- Can be named differently, but `self` is the convention

## Modifying and Deleting Properties

```python
# Modify a property
p1.age = 40

# Delete a property
del p1.age

# Delete the entire object
del p1
```

## Key Takeaways
- Classes are templates for creating objects
- `__init__()` initializes object properties
- `self` refers to the current instance
- Objects can have properties and methods
- Properties and objects can be modified or deleted