# Pandas Complete Tutorial

*Complete W3Schools Pandas Tutorial - All Sections Combined*

This comprehensive guide covers all aspects of Pandas, from basic introduction to advanced data analysis and visualization.

**Source:** W3Schools Python Pandas Tutorial

---

# Pandas Introduction

## What is Pandas?

Pandas is a Python library used for working with data sets.

It has functions for analyzing, cleaning, exploring, and manipulating data.

The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.

---

## Why Use Pandas?

Pandas allows us to analyze big data and make conclusions based on statistical theories.

Pandas can clean messy data sets, and make them readable and relevant.

Relevant data is very important in data science.

> **Data Science:** is a branch of computer science where we study how to store, use and analyze data for deriving information from it.

---

## What Can Pandas Do?

Pandas gives you answers about the data. Like:

- Is there a correlation between two or more columns?
- What is average value?
- Max value?
- Min value?

Pandas are also able to delete rows that are not relevant, or contains wrong values, like empty or NULL values. This is called *cleaning* the data.

---

## Where is the Pandas Codebase?

The source code for Pandas is located at this github repository: https://github.com/pandas-dev/pandas

> **github:** enables many people to work on the same codebase.

---

# Pandas Getting Started

## Installation of Pandas

If you have Python and PIP already installed on a system, then installation of Pandas is very easy.

Install it using this command:

```bash
C:\Users\Your Name>pip install pandas
```

If this command fails, then use a python distribution that already has Pandas installed like, Anaconda, Spyder etc.

---

## Import Pandas

Once Pandas is installed, import it in your applications by adding the `import` keyword:

```python
import pandas
```

Now Pandas is imported and ready to use.

**Example:**

```python
import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)
```

---

## Pandas as pd

Pandas is usually imported under the `pd` alias.

> **alias:** In Python alias are an alternate name for referring to the same thing.

Create an alias with the `as` keyword while importing:

```python
import pandas as pd
```

Now the Pandas package can be referred to as `pd` instead of `pandas`.

**Example:**

```python
import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
```

---

## Checking Pandas Version

The version string is stored under `__version__` attribute.

**Example:**

```python
import pandas as pd

print(pd.__version__)
```

---

# Pandas Series

## What is a Series?

A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type.

**Example:** Create a simple Pandas Series from a list:

```python
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
```

---

## Labels

If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.

This label can be used to access a specified value.

**Example:** Return the first value of the Series:

```python
print(myvar[0])
```

---

## Create Labels

With the `index` argument, you can name your own labels.

**Example:** Create your own labels:

```python
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
```

When you have created labels, you can access an item by referring to the label.

**Example:** Return the value of "y":

```python
print(myvar["y"])
```

---

## Key/Value Objects as Series

You can also use a key/value object, like a dictionary, when creating a Series.

**Example:** Create a simple Pandas Series from a dictionary:

```python
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)
```

> **Note:** The keys of the dictionary become the labels.

To select only some of the items in the dictionary, use the `index` argument and specify only the items you want to include in the Series.

**Example:** Create a Series using only data from "day1" and "day2":

```python
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)
```

---

## DataFrames

Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

Series is like a column, a DataFrame is the whole table.

**Example:** Create a DataFrame from two Series:

```python
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)
```

---

# Pandas DataFrames

## What is a DataFrame?

A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

**Example:** Create a simple Pandas DataFrame:

```python
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)
```

**Result:**
```
     calories  duration
  0       420        50
  1       380        40
  2       390        45
```

---

## Locate Row

As you can see from the result above, the DataFrame is like a table with rows and columns.

Pandas use the `loc` attribute to return one or more specified row(s).

**Example:** Return row 0:

```python
#refer to the row index:
print(df.loc[0])
```

**Result:**
```
  calories    420
  duration     50
  Name: 0, dtype: int64
```

> **Note:** This example returns a Pandas **Series**.

**Example:** Return row 0 and 1:

```python
#use a list of indexes:
print(df.loc[[0, 1]])
```

**Result:**
```
     calories  duration
  0       420        50
  1       380        40
```

> **Note:** When using `[]`, the result is a Pandas **DataFrame**.

---

## Named Indexes

With the `index` argument, you can name your own indexes.

**Example:** Add a list of names to give each row a name:

```python
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)
```

**Result:**
```
        calories  duration
  day1       420        50
  day2       380        40
  day3       390        45
```

---

## Locate Named Indexes

Use the named index in the `loc` attribute to return the specified row(s).

**Example:** Return "day2":

```python
#refer to the named index:
print(df.loc["day2"])
```

**Result:**
```
  calories    380
  duration     40
  Name: day2, dtype: int64
```

---

## Load Files Into a DataFrame

If your data sets are stored in a file, Pandas can load them into a DataFrame.

**Example:** Load a comma separated file (CSV file) into a DataFrame:

```python
import pandas as pd

df = pd.read_csv('data.csv')

print(df)
```

> You will learn more about importing files in the next chapters.

---

# Additional Topics

The remaining tutorials cover:

- **Reading CSV Files**: Load and manipulate CSV data
- **Reading JSON Files**: Work with JSON data sources
- **Analyzing DataFrames**: Use head(), tail(), info() methods
- **Cleaning Data**: Handle empty cells, wrong formats, duplicates
- **Data Correlations**: Find relationships in your data
- **Plotting**: Visualize data with charts and graphs

For the complete tutorial on each topic, refer to the individual numbered markdown files in this directory.
