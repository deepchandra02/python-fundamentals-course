# Python Set Joining Methods

Python provides several methods to join sets, each with unique behaviors:

## Union
Combines all unique items from multiple sets.

### Using `union()` method
```python
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)  # Creates new set with all unique items
```

### Using `|` operator
```python
set3 = set1 | set2  # Alternative union method
```

## Update
Inserts items from one set into another, modifying the original set.

```python
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)  # Modifies set1 directly
```

## Intersection
Keeps only items present in both sets.

```python
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)  # Contains only common items
```

## Difference
Returns items from the first set not present in other sets.

```python
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)  # Items in set1 not in set2
```

## Symmetric Difference
Keeps items that are in either set, but not in both.

```python
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
```

### Key Points
- Methods like `union()` can join sets with other data types
- Operators like `|` only work with sets
- Some methods create new sets, others modify existing sets