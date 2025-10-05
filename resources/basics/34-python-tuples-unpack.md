# Python Tuple Unpacking

## Basic Tuple Unpacking

Tuple unpacking allows you to extract values from a tuple and assign them to individual variables. Here's how it works:

```python
# Packing a tuple
fruits = ("apple", "banana", "cherry")

# Unpacking a tuple
(green, yellow, red) = fruits

print(green)    # Outputs: apple
print(yellow)   # Outputs: banana
print(red)      # Outputs: cherry
```

**Important Note:** The number of variables must match the number of values in the tuple.

## Using Asterisk `*` for Remaining Values

When you have more values than variables, you can use an asterisk to collect remaining values:

### Collecting Remaining Values as a List

```python
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)    # Outputs: apple
print(yellow)   # Outputs: banana
print(red)      # Outputs: ['cherry', 'strawberry', 'raspberry']
```

### Distributing Values Across Variables

```python
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)    # Outputs: apple
print(tropic)   # Outputs: ['mango', 'papaya', 'pineapple']
print(red)      # Outputs: cherry
```

The asterisk allows flexible unpacking by collecting multiple values into a list when the exact number of variables doesn't match the tuple's length.