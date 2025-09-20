# Module 8: Dictionaries & Settings 🗂️
## Key-Value Pairs for Smart Storage
**Duration: 6 minutes | Time: 1:10-1:16**

---

## Why Dictionaries? 🤔

### The Problem with Lists
```python
# User settings stored in list - confusing!
settings = ["John", 2, True, "+"]
# What is each value? Hard to remember!
username = settings[0]     # Position-dependent
decimal_places = settings[1]
show_steps = settings[2]
favorite_op = settings[3]
```

### The Dictionary Solution
```python
# Clear and self-documenting!
settings = {
    "username": "John",
    "decimal_places": 2,
    "show_steps": True,
    "favorite_operation": "+"
}
username = settings["username"]  # Clear meaning!
```

---

## What Are Dictionaries? 📖

### Think of Dictionaries as...
- 📞 **Phone book** - name → phone number
- 🏪 **Store** - item name → price
- 🎵 **Music library** - song title → artist
- ⚙️ **Settings panel** - setting name → value

### Dictionary Characteristics
- **Key-value pairs** - each key maps to a value
- **Unordered** - no specific order (until Python 3.7+)
- **Keys are unique** - no duplicate keys
- **Fast lookups** - finding values is super quick

---

## Creating Dictionaries 🛠️

### Empty Dictionaries
```python
settings = {}
prices = dict()
```

### Dictionaries with Initial Data
```python
user_settings = {
    "username": "Guest",
    "decimal_places": 2,
    "show_steps": True,
    "favorite_operation": "+"
}

operation_names = {
    "+": "Addition",
    "-": "Subtraction",
    "*": "Multiplication",
    "/": "Division"
}
```

---

## Accessing Dictionary Values 🎯

### Getting Values by Key
```python
settings = {"username": "John", "age": 25}

name = settings["username"]      # "John"
age = settings["age"]           # 25
```

### Safe Access with `get()`
```python
# If key doesn't exist, get() returns None (or default)
email = settings.get("email")           # None
email = settings.get("email", "N/A")    # "N/A" (default)

# Direct access crashes if key missing
email = settings["email"]  # KeyError!
```

### Checking if Key Exists
```python
if "username" in settings:
    print(f"Hello, {settings['username']}!")
```

---

## Modifying Dictionaries ✏️

### Adding/Updating Values
```python
settings = {"username": "Guest"}

# Add new key-value pair
settings["theme"] = "dark"

# Update existing value
settings["username"] = "John"

print(settings)  # {"username": "John", "theme": "dark"}
```

### Removing Items
```python
settings = {"username": "John", "theme": "dark", "age": 25}

# Remove specific key
del settings["age"]

# Remove and return value
theme = settings.pop("theme")    # "dark"
```

---

## 🔨 Live Coding: Calculator v2.2

### Adding User Settings!
```python
# User settings stored in dictionary
user_settings = {
    "username": "Guest",
    "decimal_places": 2,
    "show_steps": True,
    "favorite_operation": "+"
}

# Operations lookup dictionary
operations = {
    "+": "Addition",
    "-": "Subtraction",
    "*": "Multiplication",
    "/": "Division"
}

print(f"👋 Welcome back, {user_settings['username']}!")
print(f"🔧 Decimal places: {user_settings['decimal_places']}")

# Access operations by key
selected_op = "+"
print(f"Performing {operations[selected_op]}")
```

---

## Advanced Dictionary Patterns 💡

### Using Dictionaries for Function Lookup
```python
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y

# Store functions in dictionary!
operation_functions = {
    "+": add,
    "-": subtract,
    "*": multiply
}

# Use dictionary to call functions
result = operation_functions["+"](10, 5)  # Calls add(10, 5)
```

### Nested Dictionaries
```python
user_profile = {
    "personal": {
        "name": "John",
        "age": 25
    },
    "preferences": {
        "theme": "dark",
        "notifications": True
    }
}

name = user_profile["personal"]["name"]
```

---

## Looping Through Dictionaries 🔄

### Loop Through Keys
```python
settings = {"username": "John", "theme": "dark"}

for key in settings:
    print(f"Setting: {key}")
```

### Loop Through Values
```python
for value in settings.values():
    print(f"Value: {value}")
```

### Loop Through Key-Value Pairs
```python
for key, value in settings.items():
    print(f"{key}: {value}")

# Output:
# username: John
# theme: dark
```

---

## What We Just Added 🎉

### New Calculator Features
- ✅ **User preferences** stored clearly
- ✅ **Operation name lookup** for better UX
- ✅ **Personalized welcome** messages
- ✅ **Settings management** foundation

### Why This Matters
- **Self-documenting code** - clear what each setting does
- **Easy to extend** - just add new key-value pairs
- **Professional apps** use settings extensively

---

## Quick Exercise (1 minute) ⚡

### Your Turn!
1. **Add more settings** to user_settings
2. **Add more operations** to the operations dictionary
3. **Try accessing a key** that doesn't exist (what happens?)

### Challenge Ideas
```python
# Add these settings
user_settings["language"] = "English"
user_settings["sound_enabled"] = True
user_settings["history_limit"] = 50

# Add these operations
operations["**"] = "Power"
operations["%"] = "Modulo"
operations["//"] = "Integer Division"
```

---

## Dictionary vs List: When to Use Which? 📊

### Use Lists When:
- ✅ **Order matters** (first calculation, second calculation)
- ✅ **Items are similar** (all calculations, all scores)
- ✅ **Need to append** items frequently
- ✅ **Access by position** (get 3rd item)

### Use Dictionaries When:
- ✅ **Need fast lookups** by name/key
- ✅ **Storing settings** and configuration
- ✅ **Mapping relationships** (operation → name)
- ✅ **Self-documenting** data structure needed

### Calculator Uses Both!
- **Lists**: calculation history (order matters)
- **Dictionaries**: user settings, operation lookups

---

## Common Dictionary Patterns 🎯

### Default Values
```python
def get_setting(key, default=None):
    return user_settings.get(key, default)

decimal_places = get_setting("decimal_places", 2)
```

### Counting Items
```python
operation_count = {}
for calc in history:
    if "+" in calc:
        operation_count["+"] = operation_count.get("+", 0) + 1
```

### Configuration Files
```python
config = {
    "app_name": "Python Calculator",
    "version": "2.2",
    "features": {
        "history": True,
        "scientific": False,
        "themes": ["light", "dark"]
    }
}
```

---

## Common Dictionary Mistakes 🚨

### KeyError
```python
settings = {"username": "John"}
theme = settings["theme"]  # KeyError: 'theme'

# Better:
theme = settings.get("theme", "light")  # Safe with default
```

### Using Mutable Objects as Keys
```python
# Don't do this!
bad_dict = {[1, 2]: "value"}  # TypeError: unhashable type: 'list'

# Use immutable types as keys
good_dict = {(1, 2): "value"}  # Tuples work as keys
```

---

## Key Takeaways 📚

### What You Learned
- ✅ **Dictionaries store key-value pairs**
- ✅ **Fast lookups** by key name
- ✅ **Perfect for settings** and configuration
- ✅ **get()** method for safe access
- ✅ **Great for mapping relationships**

### Next Up: Tuples!
- Immutable sequences
- Mathematical constants
- Coordinate pairs
- Data that shouldn't change

**Your calculator is getting personalized! 👤**