# Module 10: Sets & Unique Operations 🎯
## Collections of Unique Items
**Duration: 5 minutes | Time: 1:21-1:26**

---

## What Are Sets? 🔢

### Think of Sets as...
- 🎯 **Dartboard sections** - each number appears once
- 👥 **Club membership** - each person is either in or out
- 🏷️ **Tags on a post** - no duplicate tags
- 🧮 **Operations you've tried** - each operation counted once

### Key Characteristics
- **Unique items only** - no duplicates allowed
- **Unordered** - no specific sequence
- **Fast membership testing** - "is X in the set?"
- **Mathematical set operations** - union, intersection, difference

---

## Why Sets Matter for Calculators 🤔

### The Problem: Tracking User Behavior
```python
# With list - duplicates possible
operations_tried = []
operations_tried.append("add")
operations_tried.append("subtract")
operations_tried.append("add")      # Duplicate!
print(operations_tried)  # ["add", "subtract", "add"]
# How many unique operations? Hard to tell!
```

### The Solution: Sets
```python
# With set - automatically unique
operations_tried = set()
operations_tried.add("add")
operations_tried.add("subtract")
operations_tried.add("add")         # Duplicate ignored!
print(operations_tried)  # {"add", "subtract"}
# Unique operations = len(operations_tried) = 2
```

---

## Creating Sets 🛠️

### Empty Sets
```python
operations_used = set()         # Empty set
# NOT: operations_used = {}      # This creates empty dictionary!
```

### Sets with Initial Values
```python
# From list
numbers = set([1, 2, 3, 2, 1])     # {1, 2, 3} - duplicates removed
letters = set("hello")              # {'h', 'e', 'l', 'o'} - one 'l'

# Direct creation
colors = {"red", "green", "blue"}
operations = {"add", "subtract", "multiply"}
```

### Automatic Duplicate Removal
```python
# Remove duplicates from list
numbers_with_dupes = [1, 2, 2, 3, 1, 4, 3]
unique_numbers = set(numbers_with_dupes)  # {1, 2, 3, 4}
back_to_list = list(unique_numbers)       # [1, 2, 3, 4]
```

---

## Adding and Removing Items ➕➖

### Adding Items
```python
operations_used = set()
operations_used.add("addition")
operations_used.add("subtraction")
operations_used.add("addition")      # Ignored - already exists

print(operations_used)  # {"addition", "subtraction"}
```

### Removing Items
```python
operations = {"add", "subtract", "multiply"}

operations.remove("add")        # Removes "add"
operations.discard("divide")    # Safe - no error if not found
operations.remove("divide")     # Error! Item not in set

item = operations.pop()         # Removes and returns random item
operations.clear()              # Removes all items
```

---

## Set Operations: Math in Action! 📐

### Available Operations
```python
available_ops = {"add", "subtract", "multiply", "divide", "power"}
tried_ops = {"add", "multiply"}
```

### Union (|) - Combine Sets
```python
all_ops = available_ops | tried_ops
# All operations from both sets
```

### Intersection (&) - Common Items
```python
common = available_ops & tried_ops  # {"add", "multiply"}
# Operations that are both available AND tried
```

### Difference (-) - Items in First but Not Second
```python
not_tried = available_ops - tried_ops  # {"subtract", "divide", "power"}
# Operations available but not yet tried
```

### Symmetric Difference (^) - Items in Either, but Not Both
```python
exclusive = available_ops ^ tried_ops
# Items in one set or the other, but not both
```

---

## 🔨 Live Coding: Calculator v2.4

### Tracking User Exploration!
```python
# Track unique operations used
operations_used = set()
available_operations = {"add", "subtract", "multiply", "divide", "power"}

# When user performs operation:
operation_name = "add"  # example
operations_used.add(operation_name)

print(f"🎯 Operations you've tried: {operations_used}")
print(f"📝 Try these next: {available_operations - operations_used}")

# Check if user is exploring
if len(operations_used) == len(available_operations):
    print("🏆 Calculator Master! You've tried everything!")
```

### Progress Tracking
```python
def show_progress():
    total = len(available_operations)
    tried = len(operations_used)
    percentage = (tried / total) * 100
    print(f"Progress: {tried}/{total} ({percentage:.1f}%)")
```

---

## What We Just Added 🎉

### New Features
- ✅ **Exploration tracking** - see what operations you've used
- ✅ **Progress feedback** - encouragement to try more
- ✅ **Smart suggestions** - shows untried operations
- ✅ **Achievement system** - calculator master badge!

### Why This Matters
- **Gamification** makes learning fun
- **Automatic deduplication** - no need to check for duplicates
- **Fast set operations** for comparisons
- **Professional app behavior**

---

## Quick Exercise (1 minute) ⚡

### Your Turn!
1. **Track unique numbers** used in calculations
2. **What happens** if you add the same operation twice?
3. **Try different set operations** with your own data

### Challenge Ideas
```python
# Track unique numbers used
numbers_used = set()

# In calculation loop:
numbers_used.add(num1)
numbers_used.add(num2)

print(f"🔢 Unique numbers used: {numbers_used}")

# Track difficulty levels
easy_ops = {"add", "subtract"}
hard_ops = {"power", "modulo"}
user_tried_hard = bool(operations_used & hard_ops)
```

---

## Set Membership Testing 🔍

### Fast "In" Checks
```python
operations_used = {"add", "subtract", "multiply"}

# Very fast membership testing
if "add" in operations_used:
    print("You've used addition!")

if "divide" not in operations_used:
    print("Try division next!")
```

### Why Sets Are Fast
- **Hash-based storage** - like dictionary keys
- **O(1) average lookup time** - instant checking
- **Much faster than lists** for membership testing

### Comparison: List vs Set
```python
# Slow - searches through entire list
big_list = list(range(10000))
if 9999 in big_list:  # Checks every item until found
    print("Found!")

# Fast - hash lookup
big_set = set(range(10000))
if 9999 in big_set:   # Instant check
    print("Found!")
```

---

## Practical Set Patterns 💡

### Removing Duplicates
```python
def remove_duplicates(items):
    return list(set(items))

calculations = ["5+3", "10-2", "5+3", "4*6", "10-2"]
unique_calcs = remove_duplicates(calculations)  # ["5+3", "10-2", "4*6"]
```

### Finding Common Elements
```python
user1_ops = {"add", "subtract", "multiply"}
user2_ops = {"subtract", "divide", "power"}
common_ops = user1_ops & user2_ops  # {"subtract"}
```

### Feature Flags
```python
enabled_features = {"history", "scientific", "themes"}

if "scientific" in enabled_features:
    # Show scientific calculator options
    pass

if "history" in enabled_features:
    # Enable calculation history
    pass
```

---

## Sets vs Other Data Types 📊

### Sets vs Lists
| Sets | Lists |
|------|-------|
| ✅ Unique items only | ❌ Can have duplicates |
| ✅ Fast membership testing | ❌ Slow membership testing |
| ❌ No indexing [0] | ✅ Indexed access |
| ❌ Unordered | ✅ Ordered |

### Sets vs Dictionaries
| Sets | Dictionaries |
|------|-------------|
| ✅ Just values | ✅ Key-value pairs |
| ✅ Mathematical operations | ❌ No set operations |
| ✅ Unique items | ✅ Unique keys only |

### When to Use Sets
- ✅ **Need unique items** only
- ✅ **Fast membership testing** required
- ✅ **Set operations** needed (union, intersection)
- ✅ **Order doesn't matter**

---

## Common Set Gotchas 🚨

### Sets Are Unordered
```python
my_set = {3, 1, 2}
print(my_set)  # Might print {1, 2, 3} or {2, 1, 3} - order varies!
```

### Only Immutable Items
```python
# This works
good_set = {1, "hello", (1, 2)}

# This doesn't work
bad_set = {1, [1, 2]}  # TypeError: unhashable type: 'list'
```

### Empty Set Syntax
```python
empty_set = set()      # ✅ Correct
empty_set = {}         # ❌ This is an empty dictionary!
```

---

## Advanced Set Operations 🎓

### Subset and Superset Testing
```python
basic_ops = {"add", "subtract"}
all_ops = {"add", "subtract", "multiply", "divide"}

is_subset = basic_ops <= all_ops        # True - basic_ops is subset
is_superset = all_ops >= basic_ops      # True - all_ops is superset
```

### Set Comprehensions
```python
# Create set of even numbers
evens = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}

# Operations from history that contain "+"
plus_operations = {op for op in operations_used if "+" in op}
```

---

## Key Takeaways 📚

### What You Learned
- ✅ **Sets store unique items** only
- ✅ **Fast membership testing** with `in`
- ✅ **Set operations** (union, intersection, difference)
- ✅ **Perfect for tracking** what user has tried
- ✅ **Automatic duplicate removal**

### Next Up: Functions!
- Organize code into reusable blocks
- Parameters and return values
- Clean, professional code structure
- Make calculator modular and maintainable

**Your calculator tracks user exploration! 🎮**