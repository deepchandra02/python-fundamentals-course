# Python While Loops

Python provides two primitive loop commands: `while` and `for` loops. This tutorial focuses on the `while` loop, which executes a set of statements as long as a condition is true.

## Basic While Loop

A basic while loop prints numbers while a condition is met:

```python
i = 1
while i < 6:
    print(i)
    i += 1
```

**Key Points:**
- Always increment the index variable to prevent infinite loops
- The loop continues until the condition becomes false

## Break Statement

The `break` statement allows you to exit the loop prematurely:

```python
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
```

## Continue Statement

The `continue` statement skips the current iteration and moves to the next:

```python
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
```

## Else Statement

The `else` statement runs a block of code once the condition becomes false:

```python
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
```

## Best Practices
- Always have a way to exit the loop
- Increment loop variables
- Use `break` and `continue` carefully
- Consider using `for` loops when the number of iterations is known