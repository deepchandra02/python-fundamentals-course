# Python For Loops Tutorial

## Introduction

A `for` loop in Python is used for iterating over sequences like lists, tuples, dictionaries, sets, or strings. Unlike loops in some other programming languages, Python's `for` loop works more like an iterator method.

## Basic For Loop Syntax

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
```

This will print each fruit in the list.

## Looping Through Strings

You can also loop through characters in a string:

```python
for x in "banana":
    print(x)
```

## Control Flow Statements

### Break Statement
Stops the loop before completing all iterations:

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
```

### Continue Statement
Skips the current iteration and continues with the next:

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
```

## Range() Function

Used to loop a specific number of times:

```python
# Print 0-5
for x in range(6):
    print(x)

# Custom start and increment
for x in range(2, 30, 3):
    print(x)
```

## Else in For Loops

The `else` block executes when the loop completes normally:

```python
for x in range(6):
    print(x)
else:
    print("Finally finished!")
```

**Note:** The `else` block won't run if the loop is stopped by a `break` statement.

## Nested Loops

Loops can be nested inside each other:

```python
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
```

## Pass Statement

Use `pass` as a placeholder when you need an empty loop:

```python
for x in [0, 1, 2]:
    pass
```

## Key Takeaways
- For loops iterate over sequences
- Use `break` and `continue` to control flow
- `range()` creates number sequences
- Nested loops allow complex iterations
- `else` clause runs after normal loop completion