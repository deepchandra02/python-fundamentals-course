# Python Match Statement Tutorial

## Overview
The `match` statement in Python is a powerful control flow mechanism used to perform different actions based on different conditions, offering a more concise alternative to multiple `if..else` statements.

## Basic Syntax
```python
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
```

## Key Features

### Basic Matching
- Evaluates an expression once
- Compares the expression value with each case
- Executes the code block of the first matching case

### Example: Weekday Matching
```python
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 4:
    print("Thursday")
```

### Default Case
Use the underscore `_` as a catch-all default case:
```python
match day:
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _:
    print("Weekday")
```

### Combining Values
Use the pipe `|` to match multiple values in one case:
```python
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Weekday")
  case 6 | 7:
    print("Weekend")
```

### Conditional Guards
Add `if` statements for additional conditions:
```python
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
```

## Key Takeaways
- More readable than multiple `if..else` statements
- Supports multiple value matching
- Allows conditional guards
- Provides a default case mechanism