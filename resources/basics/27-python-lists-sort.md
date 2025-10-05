# Python List Sorting

## Basic Sorting

Python lists can be sorted using the `.sort()` method, which sorts the list in-place:

### Alphabetical Sorting
```python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
```

### Numerical Sorting
```python
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
```

## Descending Sort

To sort in descending order, use the `reverse` parameter:

```python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)
```

## Custom Sorting

You can create a custom sorting function using the `key` parameter:

```python
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)
```

## Case-Insensitive Sorting

To sort strings without considering case:

```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)
```

## Reversing a List

To simply reverse the order of a list:

```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
```

## Key Takeaways
- `.sort()` modifies the original list
- Use `reverse=True` for descending order
- `key` parameter allows custom sorting logic
- `str.lower` helps with case-insensitive sorting
- `.reverse()` flips the current order of list items