# Python Conditions and If Statements

Python supports standard logical comparison operators:

## Comparison Operators
- Equals: `a == b`
- Not Equals: `a != b`
- Less than: `a < b`
- Less than or equal to: `a <= b`
- Greater than: `a > b`
- Greater than or equal to: `a >= b`

## Basic If Statement
```python
a = 33
b = 200
if b > a:
    print("b is greater than a")
```

## Indentation
Python uses indentation to define code blocks, unlike other languages that use curly brackets.

## Elif and Else Statements
```python
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
```

## Short Hand Conditionals
### One-line If
```python
if a > b: print("a is greater than b")
```

### Ternary Operator
```python
print("A") if a > b else print("B")
```

## Logical Operators
### And
```python
if a > b and c > a:
    print("Both conditions are True")
```

### Or
```python
if a > b or a > c:
    print("At least one condition is True")
```

### Not
```python
if not a > b:
    print("a is NOT greater than b")
```

## Nested If Statements
```python
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
```

## Pass Statement
Used when you want an empty if statement:
```python
if b > a:
    pass
```

Key takeaways:
- Python uses indentation to define code blocks
- Supports multiple conditional structures
- Logical operators allow complex condition checking
- Ternary operators provide concise conditional expressions