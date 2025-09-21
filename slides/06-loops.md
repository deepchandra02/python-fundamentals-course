---
marp: false
---

# Module 6: Loop Power 🔄

## Repeating Actions with While Loops

**Duration: 8 minutes | Time: 0:55-1:03**

---

## Why Loops Matter 🎯

### Without Loops (Repetitive Code)

```python
print("Welcome to Calculator!")
# User calculates once and program ends
num1 = float(input("First number: "))
operation = input("Operation: ")
num2 = float(input("Second number: "))
# Calculate and show result
print("Thanks for using calculator!")
```

### With Loops (Smart Repetition)

```python
print("Welcome to Calculator!")
while user_wants_to_continue:
    # User can calculate many times
    # Program keeps running until they want to stop
print("Thanks for using calculator!")
```

---

## The `while` Loop 🔄

### Basic Syntax

```python
while condition:
    # Code to repeat
    # This runs over and over
    # Until condition becomes False
```

### Simple Example

```python
count = 1
while count <= 3:
    print(f"Count: {count}")
    count = count + 1  # Important: update the condition!

print("Done counting!")
```

### Output:

```
Count: 1
Count: 2
Count: 3
Done counting!
```

---

## Infinite Loops (The Good Kind) ♾️

### When You Want to Loop Forever

```python
while True:
    # This runs forever
    # Until something breaks out
    user_input = input("Continue? (q to quit): ")
    if user_input == "q":
        break  # Exit the loop
```

### The `break` Statement

- **Immediately exits** the loop
- **Jumps to** code after the loop
- **Common pattern** for menu systems

---

## Menu Systems with Loops 📋

### Classic Menu Pattern

```python
while True:
    print("\n--- MENU ---")
    print("1. Option A")
    print("2. Option B")
    print("3. Exit")

    choice = input("Choose (1-3): ")

    if choice == "3":
        print("Goodbye!")
        break
    elif choice == "1":
        print("You chose Option A")
    elif choice == "2":
        print("You chose Option B")
    else:
        print("Invalid choice!")
```

---

## Loop Control: `break` and `continue` 🎮

### `break` - Exit Loop Completely

```python
while True:
    number = int(input("Enter number (0 to quit): "))
    if number == 0:
        break  # Exit the loop entirely
    print(f"You entered: {number}")
```

### `continue` - Skip to Next Iteration

```python
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skip the rest of this iteration
    print(f"Count: {count}")
# Prints: 1, 2, 4, 5 (skips 3)
```

---

## 🔨 Live Coding: Calculator v2.0

### Never-Ending Calculator!

```python
print("🧮 Never-Ending Calculator v2.0")

while True:
    print("\n🎯 CALCULATOR MENU")
    print("1️⃣ Basic Math")
    print("2️⃣ Exit")

    choice = input("Choose (1-2): ")

    if choice == "2":
        print("👋 Thanks for calculating!")
        break
    elif choice == "1":
        num1 = float(input("First number: "))
        op = input("Operation (+,-,*,/): ")
        num2 = float(input("Second number: "))

        if op == "+": result = num1 + num2
        elif op == "-": result = num1 - num2
        elif op == "*": result = num1 * num2
        elif op == "/": result = num1 / num2 if num2 != 0 else "Error!"

        print(f"✅ Result: {result}")
    else:
        print("❌ Invalid choice!")
```

---

## What We Just Built 🎉

### New Powers

- ✅ **Infinite loop** keeps calculator running
- ✅ **Menu system** for user choices
- ✅ **Multiple calculations** without restarting program
- ✅ **Graceful exit** when user chooses
- ✅ **Professional user experience**

### User Experience Improved

- Calculator doesn't exit after one calculation
- Users can perform many operations
- Clean menu interface
- Proper goodbye message

---

## Quick Exercise (2 minutes) ⚡

### Your Turn!

1. **Add "3️⃣ Power Operations"** to the menu
2. **Test the exit functionality** - make sure it works
3. **Try invalid menu choices** - see error handling
4. **Add more operations** to the basic math section

### Challenge: Power Operations Menu

```python
elif choice == "3":
    print("🔥 POWER OPERATIONS")
    base = float(input("Base: "))
    exp = float(input("Exponent: "))
    result = base ** exp
    print(f"🔥 {base} ** {exp} = {result}")
```

---

## Loop Patterns You'll Use 💡

### Input Validation Loop

```python
while True:
    age = input("Enter your age: ")
    if age.isdigit():
        age = int(age)
        break
    print("Please enter a valid number!")
```

### Countdown Loop

```python
countdown = 5
while countdown > 0:
    print(f"Starting in {countdown}...")
    countdown -= 1
print("Go!")
```

### Accumulator Loop

```python
total = 0
count = 0
while count < 5:
    number = float(input("Enter number: "))
    total += number
    count += 1
average = total / count
```

---

## Common Loop Mistakes 🚨

### Infinite Loop (The Bad Kind)

```python
# This never stops!
count = 1
while count <= 10:
    print(count)
    # Forgot to update count!
```

### Off-by-One Errors

```python
# Want to print 1-10
count = 1
while count < 10:  # Only goes to 9!
    print(count)
    count += 1
```

### Indentation Problems

```python
# Wrong indentation
while True:
print("This won't work")
```

---

## While vs For Loops 🤔

### Use `while` When:

- ✅ You don't know how many iterations
- ✅ Condition might never be true
- ✅ Menu systems and user interfaces
- ✅ "Keep going until user says stop"

### Use `for` When:

- ✅ You know the number of iterations
- ✅ Looping through collections (lists, strings)
- ✅ "Do this exactly N times"

### For Our Calculator

- `while` is perfect for menu systems!

---

## Key Takeaways 📚

### What You Learned

- ✅ **while loops** repeat code based on conditions
- ✅ **Infinite loops** with `while True`
- ✅ **break** exits loops immediately
- ✅ **continue** skips to next iteration
- ✅ **Menu systems** using loop patterns

### Next Up: Lists & History!

- Store multiple values
- Remember calculation history
- Track user's calculations
- Add memory to your calculator

**Your calculator never stops! 🔄**
