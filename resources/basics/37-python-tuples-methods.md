# Python Tuple Methods

Python provides two built-in methods for tuples:

## 1. count() Method
- **Purpose**: Returns the number of times a specified value occurs in a tuple
- **Syntax**: `tuple.count(value)`

## 2. index() Method
- **Purpose**: Searches the tuple for a specified value and returns its position
- **Syntax**: `tuple.index(value)`

### Example Usage

```python
# Example of count() method
fruits = ('apple', 'banana', 'cherry', 'apple')
apple_count = fruits.count('apple')  # Returns 2

# Example of index() method
fruits = ('apple', 'banana', 'cherry')
banana_position = fruits.index('banana')  # Returns 1
```

### Key Characteristics
- Tuples are immutable, so these methods do not modify the original tuple
- `count()` helps you determine frequency of an element
- `index()` helps you find the first occurrence of an element

### Important Notes
- If the value is not found, `index()` will raise a `ValueError`
- These methods work similarly to list methods but cannot modify the tuple