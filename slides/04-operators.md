# Module 4: Operation Station 🚀
## All Mathematical Operations
**Duration: 12 minutes | Time: 0:28-0:40**

---

## Python Math Operators 🧮

### Basic Arithmetic
```python
a = 10
b = 3

# Addition
result = a + b      # 13

# Subtraction
result = a - b      # 7

# Multiplication
result = a * b      # 30

# Division
result = a / b      # 3.3333333333333335
```

---

## More Powerful Operators 💪

### Division Variations
```python
a = 10
b = 3

# Regular division (float result)
result = a / b      # 3.3333333333333335

# Integer division (whole number result)
result = a // b     # 3

# Modulo (remainder)
result = a % b      # 1 (because 10 ÷ 3 = 3 remainder 1)
```

### Power Operation
```python
# Exponentiation (power)
base = 2
exponent = 3
result = base ** exponent   # 8 (2³ = 2×2×2)

# More examples
result = 5 ** 2             # 25 (5²)
result = 10 ** 3            # 1000 (10³)
```

---

## Modulo: The Remainder Operator 🔄

### What is Modulo?
- **Finds remainder** after division
- **Symbol**: `%`
- **Useful for**: checking even/odd, time calculations, cycling

### Examples
```python
10 % 3    # 1 (10 ÷ 3 = 3 remainder 1)
15 % 4    # 3 (15 ÷ 4 = 3 remainder 3)
20 % 5    # 0 (20 ÷ 5 = 4 remainder 0)
```

### Real Uses
```python
# Check if number is even
number = 8
if number % 2 == 0:
    print("Even!")

# Clock arithmetic
hour = 25 % 12    # 1 (25 o'clock = 1 o'clock)
```

---

## Order of Operations 📐

### Python Follows PEMDAS
1. **P**arentheses `()`
2. **E**xponents `**`
3. **M**ultiplication `*` and **D**ivision `/`
4. **A**ddition `+` and **S**ubtraction `-`

### Examples
```python
result = 2 + 3 * 4        # 14 (not 20!)
result = (2 + 3) * 4      # 20
result = 2 ** 3 * 4       # 32 (8 * 4)
result = 2 ** (3 * 4)     # 4096 (2¹²)
```

---

## Operator Symbols Quick Reference 📋

| Operator | Symbol | Example | Result |
|----------|--------|---------|--------|
| Addition | `+` | `5 + 3` | `8` |
| Subtraction | `-` | `5 - 3` | `2` |
| Multiplication | `*` | `5 * 3` | `15` |
| Division | `/` | `5 / 3` | `1.666...` |
| Integer Division | `//` | `5 // 3` | `1` |
| Modulo | `%` | `5 % 3` | `2` |
| Power | `**` | `5 ** 3` | `125` |

---

## Working with Different Number Types 🔢

### Mixing Integers and Floats
```python
result = 5 + 3.0        # 8.0 (becomes float)
result = 10 / 2         # 5.0 (division always returns float)
result = 10 // 3        # 3 (integer division returns int)
result = 10.0 // 3      # 3.0 (floor division with float)
```

### When Results Become Floats
- **Regular division** `/` always returns float
- **Mixed operations** (int + float) return float
- **Integer division** `//` returns int (unless mixed with float)

---

## 🔨 Live Coding: Calculator v0.4

### Showing All Operations!
```python
print("🧮 Multi-Operation Calculator v0.4")

num1 = float(input("First number: "))
num2 = float(input("Second number: "))

print(f"➕ Addition: {num1} + {num2} = {num1 + num2}")
print(f"➖ Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"✖️ Multiplication: {num1} * {num2} = {num1 * num2}")
print(f"➗ Division: {num1} / {num2} = {num1 / num2}")
print(f"🔥 Power: {num1} ** {num2} = {num1 ** num2}")
```

### What We Added
- ✅ **All basic operators** in one program
- ✅ **Beautiful emoji formatting**
- ✅ **Multiple results** displayed at once
- ✅ **Professional calculator feel**

---

## Quick Exercise (3 minutes) ⚡

### Your Turn!
1. **Add modulo operation** to your calculator
2. **Try integer division** (`//`)
3. **Test with different numbers** - see how operators behave
4. **Add more emoji styling**

### Challenge: Add These Operations
```python
# Modulo (remainder)
print(f"📐 Modulo: {num1} % {num2} = {num1 % num2}")

# Integer division
print(f"📊 Integer Division: {num1} // {num2} = {num1 // num2}")

# Square of each number
print(f"🔷 {num1} squared = {num1 ** 2}")
print(f"🔶 {num2} squared = {num2 ** 2}")
```

---

## Special Cases to Know ⚠️

### Division by Zero
```python
result = 5 / 0    # ZeroDivisionError - crashes program!
```

### Very Large Numbers
```python
result = 2 ** 100    # Python handles big numbers easily!
# 1267650600228229401496703205376
```

### Negative Numbers
```python
result = -5 ** 2     # -25 (careful with negatives!)
result = (-5) ** 2   # 25 (use parentheses for clarity)
```

---

## Practical Calculator Tips 💡

### Formatting Large Numbers
```python
result = 1234567.89
print(f"Result: {result:,.2f}")  # Result: 1,234,567.89
```

### Rounding Results
```python
result = 10 / 3
print(f"Rounded: {result:.2f}")  # Rounded: 3.33
```

### Scientific Notation
```python
big_number = 1.5e6    # 1,500,000
small_number = 1.5e-6 # 0.0000015
```

---

## Key Takeaways 📚

### What You Learned
- ✅ **Seven math operators**: +, -, *, /, //, %, **
- ✅ **Order of operations** (PEMDAS)
- ✅ **Modulo for remainders**
- ✅ **Power operator** for exponents
- ✅ **Professional formatting** with emojis

### Next Up: Smart Decisions!
- Let users choose which operation to perform
- Add conditional logic (if/else)
- Handle division by zero
- Make calculator truly interactive

**Your calculator is becoming powerful! ⚡**