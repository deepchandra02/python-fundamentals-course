# Module 9: Tuples & Constants 🔒
## Immutable Sequences for Fixed Data
**Duration: 5 minutes | Time: 1:16-1:21**

---

## What Are Tuples? 🎯

### Think of Tuples as...
- 📐 **Mathematical coordinates** (x, y) that don't change
- 🌍 **GPS coordinates** (latitude, longitude)
- 📅 **Dates** (year, month, day)
- 🔢 **Mathematical constants** that should never change

### Key Characteristics
- **Immutable** - cannot be changed after creation
- **Ordered** - items have positions (like lists)
- **Allow duplicates** - can have repeated values
- **Indexed** - access items with [0], [1], etc.

---

## Tuples vs Lists: The Difference 📊

### Lists (Mutable)
```python
calculations = ["5+3=8", "10-2=8"]
calculations.append("4*6=24")     # ✅ Can modify
calculations[0] = "6+3=9"         # ✅ Can change items
```

### Tuples (Immutable)
```python
pi_e_sqrt2 = (3.14159, 2.71828, 1.41421)
pi_e_sqrt2.append(1.73205)        # ❌ Error! No append method
pi_e_sqrt2[0] = 3.14              # ❌ Error! Can't change items
```

### When to Use Each
- **Lists**: Shopping lists, calculation history (things that change)
- **Tuples**: Coordinates, constants, configurations (things that don't change)

---

## Creating Tuples 🛠️

### Basic Syntax
```python
# With parentheses (recommended)
point = (10, 20)
colors = ("red", "green", "blue")

# Without parentheses (works but less clear)
point = 10, 20
colors = "red", "green", "blue"

# Empty tuple
empty = ()

# Single item tuple (note the comma!)
single = (42,)  # Without comma, it's just parentheses around 42
```

### Mathematical Constants
```python
MATH_CONSTANTS = (3.14159, 2.71828, 1.41421)  # π, e, √2
CONSTANT_NAMES = ("Pi", "Euler's e", "√2")
```

---

## Accessing Tuple Elements 🔍

### Index Access (Same as Lists)
```python
point = (10, 20)
x = point[0]        # 10
y = point[1]        # 20

constants = (3.14159, 2.71828, 1.41421)
pi = constants[0]   # 3.14159
e = constants[1]    # 2.71828
```

### Negative Indexing
```python
point = (10, 20, 30)
last = point[-1]    # 30
```

### Length and Membership
```python
point = (10, 20, 30)
length = len(point)         # 3
has_ten = 10 in point      # True
```

---

## Tuple Unpacking: The Magic! ✨

### Multiple Assignment
```python
point = (10, 20)
x, y = point        # x = 10, y = 20

# Works with any sequence!
name, age, city = ("John", 25, "NYC")
```

### Function Returns
```python
def get_circle_info(radius):
    area = 3.14159 * radius ** 2
    circumference = 2 * 3.14159 * radius
    return area, circumference  # Returns a tuple!

# Unpack the result
area, circumference = get_circle_info(5)
print(f"Area: {area}, Circumference: {circumference}")
```

### Swapping Variables
```python
a = 10
b = 20
a, b = b, a     # Swap values! a=20, b=10
```

---

## 🔨 Live Coding: Calculator v2.3

### Adding Mathematical Constants!
```python
# Mathematical constants as tuples
MATH_CONSTANTS = (3.14159, 2.71828, 1.41421)  # π, e, √2
CONSTANT_NAMES = ("Pi", "Euler's e", "√2")

# Display constants
print("🔢 MATH CONSTANTS")
for i, (name, value) in enumerate(zip(CONSTANT_NAMES, MATH_CONSTANTS), 1):
    print(f"{i}. {name} = {value}")

# Coordinates as tuples
point1 = (10, 20)
point2 = (30, 40)
print(f"Distance calculation between {point1} and {point2}")
```

### Using `zip()` Function
- **Combines two sequences** element by element
- **Perfect for** pairing names with values
- **Returns pairs** that can be unpacked

---

## What We Just Added 🎉

### New Features
- ✅ **Mathematical constants** stored safely
- ✅ **Professional constant display**
- ✅ **Coordinate system** foundation
- ✅ **Data that can't be accidentally changed**

### Why Use Tuples Here?
- Constants **shouldn't change** during program
- **Prevents bugs** from accidental modification
- **Clear intent** - this data is fixed
- **Memory efficient** - tuples use less memory

---

## Quick Exercise (1 minute) ⚡

### Your Turn!
1. **Add more mathematical constants** (golden ratio, speed of light)
2. **Create coordinate tuples** for geometric shapes
3. **Try changing a tuple** - see what error you get

### Challenge Ideas
```python
# More constants
MORE_CONSTANTS = (1.618, 299792458, 9.81)  # φ, c, g
MORE_NAMES = ("Golden Ratio", "Speed of Light", "Gravity")

# Shape coordinates
triangle = ((0, 0), (10, 0), (5, 8))  # Three points
rectangle = ((0, 0), (10, 0), (10, 5), (0, 5))  # Four corners
```

---

## Useful Tuple Methods 🛠️

### Built-in Methods
```python
numbers = (1, 2, 3, 2, 4, 2)

# Count occurrences
count_2 = numbers.count(2)      # 3

# Find index of first occurrence
index_3 = numbers.index(3)      # 2
```

### Converting Between Types
```python
# List to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)       # (1, 2, 3)

# Tuple to list
my_list = list(my_tuple)        # [1, 2, 3]

# String to tuple
letters = tuple("hello")        # ('h', 'e', 'l', 'l', 'o')
```

---

## Tuples in Calculator Applications 💡

### Configuration That Shouldn't Change
```python
APP_CONFIG = (
    "Python Calculator",    # App name
    "2.3",                 # Version
    "Educational",         # Type
    True                   # Production ready
)
app_name, version, app_type, is_ready = APP_CONFIG
```

### RGB Color Values
```python
COLORS = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255)
}
r, g, b = COLORS["red"]
```

### Date and Time
```python
today = (2024, 9, 20)           # Year, month, day
year, month, day = today
```

---

## When Immutability Helps 🛡️

### Prevents Accidental Changes
```python
# With list - dangerous!
constants = [3.14159, 2.71828]
constants[0] = 3.0  # Oops! Changed pi by mistake

# With tuple - safe!
constants = (3.14159, 2.71828)
constants[0] = 3.0  # Error! Can't change
```

### Thread Safety
- **Multiple parts** of program can safely read tuple
- **No need to worry** about other code changing values
- **Important for** larger applications

### Dictionary Keys
```python
# Tuples can be dictionary keys (lists cannot!)
locations = {
    (0, 0): "Origin",
    (10, 20): "Point A",
    (30, 40): "Point B"
}
```

---

## Common Tuple Patterns 🎯

### Multiple Return Values
```python
def get_name_age():
    return "John", 25  # Returns tuple

name, age = get_name_age()
```

### Iteration with Index and Value
```python
items = ("a", "b", "c")
for i, value in enumerate(items):
    print(f"{i}: {value}")
```

### Safe Function Parameters
```python
def calculate_distance(point1, point2):
    # Function can't accidentally modify the points
    x1, y1 = point1
    x2, y2 = point2
    return ((x2-x1)**2 + (y2-y1)**2)**0.5
```

---

## Key Takeaways 📚

### What You Learned
- ✅ **Tuples are immutable** lists
- ✅ **Perfect for constants** and fixed data
- ✅ **Tuple unpacking** for multiple assignment
- ✅ **zip()** combines sequences
- ✅ **Memory efficient** and thread-safe

### Next Up: Sets!
- Unique collections
- Track which operations user has tried
- Set operations (union, intersection)
- Eliminate duplicates automatically

**Your calculator has solid foundations! 🏗️**