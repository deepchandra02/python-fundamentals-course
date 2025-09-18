# Python String Modification Methods

Python provides several built-in methods to modify strings:

## 1. Upper Case
Convert a string to uppercase using `.upper()`:
```python
a = "Hello, World!"
print(a.upper())  # Outputs: HELLO, WORLD!
```

## 2. Lower Case
Convert a string to lowercase using `.lower()`:
```python
a = "Hello, World!"
print(a.lower())  # Outputs: hello, world!
```

## 3. Remove Whitespace
Remove spaces from the beginning and end of a string using `.strip()`:
```python
a = " Hello, World! "
print(a.strip())  # Outputs: "Hello, World!"
```

## 4. Replace String
Replace parts of a string using `.replace()`:
```python
a = "Hello, World!"
print(a.replace("H", "J"))  # Outputs: "Jello, World!"
```

## 5. Split String
Split a string into a list using `.split()`:
```python
a = "Hello, World!"
print(a.split(","))  # Outputs: ['Hello', ' World!']
```

## Key Points
- These methods create a new string; they do not modify the original string
- String methods are powerful tools for string manipulation
- More string methods can be found in the Python String Methods Reference