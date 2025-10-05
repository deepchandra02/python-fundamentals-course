# Python Numbers

## Overview

Python has three primary numeric types:
- `int` (integer)
- `float` (floating point number)
- `complex` (complex number)

## Integer (int)

Integers are whole numbers without decimals, with unlimited length.

```python
x = 1
y = 35656222554887711
z = -3255522
```

## Float

Floats are numbers with decimal points or scientific notation.

```python
# Decimal floats
x = 1.10
y = 1.0
z = -35.59

# Scientific notation
x = 35e3    # 35,000
y = 12E4    # 120,000
z = -87.7e100
```

## Complex Numbers

Complex numbers include a real and imaginary component, denoted with 'j'.

```python
x = 3+5j
y = 5j
z = -5j
```

## Type Conversion

You can convert between numeric types using built-in functions:

```python
x = 1    # int
y = 2.8  # float
z = 1j   # complex

a = float(x)    # int to float
b = int(y)      # float to int
c = complex(x)  # int to complex
```

**Note:** Complex numbers cannot be converted to other numeric types.

## Random Numbers

Use the `random` module to generate random numbers:

```python
import random

print(random.randrange(1, 10))  # Random number between 1-9
```

## Key Takeaways

- Python supports multiple numeric types
- Type conversion is possible between most numeric types
- The `type()` function can verify a variable's type
- The `random` module provides random number generation capabilities