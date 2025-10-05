# Python - Join Lists

## Ways to Join Lists in Python

### 1. Using the `+` Operator
The simplest way to join lists is by using the `+` operator:

```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
```

### 2. Appending Items Manually
You can append items from one list to another using a `for` loop:

```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)
```

### 3. Using the `extend()` Method
The `extend()` method adds all elements from one list to the end of another:

```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
```

## Key Takeaways
- The `+` operator creates a new list
- `append()` adds individual items one at a time
- `extend()` adds all items from one list to another efficiently

Each method achieves list concatenation, but they have slightly different use cases and performance characteristics.