# Python Polymorphism

Polymorphism in Python means "many forms" and refers to methods, functions, or operators with the same name that can be executed on different objects or classes.

## Function Polymorphism

The `len()` function demonstrates polymorphism by working differently with various data types:

### String Polymorphism
```python
x = "Hello World!"
print(len(x))  # Returns number of characters
```

### Tuple Polymorphism
```python
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))  # Returns number of items in tuple
```

### Dictionary Polymorphism
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))  # Returns number of key/value pairs
```

## Class Polymorphism

Classes can have the same method name with different implementations:

```python
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

# Polymorphic behavior
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
  x.move()
```

## Inheritance Class Polymorphism

Polymorphism can also work with inherited classes:

```python
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  def move(self):
    print("Drive!")

class Boat(Vehicle):
  def move(self):
    print("Sail!")
```

## Key Takeaways
- Polymorphism allows the same interface to work with different types
- Built-in functions like `len()` demonstrate polymorphism
- Classes can implement the same method names with different behaviors
- Inheritance supports polymorphic behavior
- Enables writing flexible, reusable code