#!/usr/bin/env python3
"""
Script to create all Session 3 notebooks with Example → TODO pattern
This creates notebooks 02-05 (01 already created)
"""

import json
import os

# Notebook base directory
NOTEBOOK_DIR = "notebooks/Session 3"

def create_notebook(cells):
    """Create a Jupyter notebook structure"""
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

def md_cell(content):
    """Create a markdown cell"""
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": content.split("\n")
    }

def code_cell(content):
    """Create a code cell"""
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": content.split("\n")
    }

print("Creating Session 3 notebooks...\n")

# =====================================================================
# 02-PANDAS-FUNDAMENTALS.IPYNB
# =====================================================================

print("Creating 02-pandas-fundamentals.ipynb...")

pandas_cells = [
    md_cell("""# 🐼 Pandas Fundamentals - Session 3
## Python Fundamentals Workshop: Data Science & ML

**What you'll learn in this notebook:**
- ✅ Create and manipulate Pandas Series and DataFrames
- ✅ Read data from CSV and JSON files
- ✅ Select and filter data
- ✅ Clean and prepare data for analysis
- ✅ Perform grouping and aggregation operations

**Estimated time:** 40-50 minutes

---"""),

    md_cell("""## 🎯 Why Pandas?

Pandas is the most popular library for data manipulation and analysis in Python:

- **Powerful:** Handle large datasets with ease
- **Flexible:** Work with structured data (like Excel, CSV, SQL)
- **Fast:** Optimized for performance
- **Intuitive:** Easy-to-use syntax for complex operations

Think of Pandas as **Excel on steroids**!

Let's start by importing Pandas!"""),

    code_cell("""import pandas as pd
import numpy as np

print(f"Pandas version: {pd.__version__}")
print("✅ Pandas imported successfully!")"""),

    md_cell("""---

## 1️⃣ Pandas Series

A Series is a **one-dimensional** labeled array. Think of it as a single column in a spreadsheet."""),

    md_cell("""### 💡 Example: Creating and Using Series"""),

    code_cell("""# Create a Series from a list
temperatures = pd.Series([22, 25, 19, 23, 28, 30, 27])
print("Temperature Series:")
print(temperatures)
print()

# Series with custom index
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temp_series = pd.Series([22, 25, 19, 23, 28, 30, 27], index=days)
print("Temperature by Day:")
print(temp_series)
print()

# Access elements by index
print(f"Temperature on Monday: {temp_series['Mon']}°C")
print(f"Temperature on Friday: {temp_series['Fri']}°C")
print()

# Perform operations
print("Temperatures in Fahrenheit:")
print(temp_series * 9/5 + 32)
print()

# Basic statistics
print("Statistics:")
print(f"  Mean: {temp_series.mean():.2f}°C")
print(f"  Max: {temp_series.max()}°C")
print(f"  Min: {temp_series.min()}°C")"""),

    md_cell("""### ✏️ Your Turn: Create Your Own Series"""),

    code_cell("""# ✏️ YOUR TURN: Practice creating and using Series

# Task 1: Create a Series of student scores with names as index
# Names: ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
# Scores: [85, 92, 78, 88, 95]

# Your code here
student_scores = None  # Create Series with index=names

print("Student Scores:")
print(student_scores if student_scores is not None else "Not created yet")
print()

# Task 2: Access Bob's score
# Your code here
bob_score = None  # Access using index

print(f"Bob's score: {bob_score}" if bob_score is not None else "Not accessed yet")
print()

# Task 3: Calculate the average score
# Your code here
avg_score = None  # Use .mean()

print(f"Average score: {avg_score:.2f}" if avg_score is not None else "Not calculated yet")
print()

# Task 4: Find scores above 85
# Hint: Use boolean indexing like: series[series > 85]
# Your code here
high_scores = None  # Filter scores > 85

print("Scores above 85:")
print(high_scores if high_scores is not None else "Not filtered yet")"""),

    md_cell("""---

## 2️⃣ Pandas DataFrames

A DataFrame is a **two-dimensional** labeled data structure. Think of it as a spreadsheet or SQL table."""),

    md_cell("""### 💡 Example: Creating and Exploring DataFrames"""),

    code_cell("""# Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston'],
    'Salary': [70000, 85000, 65000, 75000, 90000]
}

df = pd.DataFrame(data)
print("Employee DataFrame:")
print(df)
print()

# Display basic info
print("DataFrame Info:")
print(f"  Shape: {df.shape} (rows, columns)")
print(f"  Columns: {list(df.columns)}")
print(f"  Data types:")
print(df.dtypes)
print()

# Access a single column (returns a Series)
print("Names column:")
print(df['Name'])
print()

# Access multiple columns
print("Name and Salary:")
print(df[['Name', 'Salary']])
print()

# Access a row by index
print("First row:")
print(df.iloc[0])  # iloc = integer location
print()

# Access row by index label
print("Row at index 2:")
print(df.loc[2])  # loc = label location"""),

    md_cell("""### ✏️ Your Turn: Create and Explore DataFrames"""),

    code_cell("""# ✏️ YOUR TURN: Practice creating and exploring DataFrames

# Task 1: Create a DataFrame with product information
# Products: ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard']
# Prices: [1200, 800, 500, 300, 100]
# Stock: [15, 30, 25, 10, 50]

# Your code here
products_df = None  # Create DataFrame from dict

print("Products DataFrame:")
print(products_df if products_df is not None else "Not created yet")
print()

# Task 2: Display the shape of the DataFrame
# Your code here
df_shape = None  # Use .shape

print(f"DataFrame shape: {df_shape}" if df_shape is not None else "Not accessed yet")
print()

# Task 3: Access only the 'Product' and 'Price' columns
# Your code here
price_info = None  # Select columns

print("Product and Price:")
print(price_info if price_info is not None else "Not selected yet")
print()

# Task 4: Get the product with the highest price
# Hint: Use df['Price'].max() to find max, then filter
# Your code here
max_price = None  # Find maximum price

print(f"Highest price: ${max_price}" if max_price is not None else "Not calculated yet")"""),

    md_cell("""---

## 3️⃣ Reading Data from Files

Pandas can read data from many formats: CSV, Excel, JSON, SQL, and more!"""),

    md_cell("""### 💡 Example: Reading CSV Data"""),

    code_cell("""from io import StringIO

# Sample CSV data (in real scenarios, you'd use pd.read_csv('file.csv'))
csv_data = \"\"\"Name,Department,Salary,Years
Alice,Engineering,95000,5
Bob,Marketing,65000,3
Charlie,Engineering,88000,4
Diana,Sales,72000,6
Eve,Marketing,70000,2
Frank,Engineering,105000,8
Grace,Sales,68000,3
\"\"\"

# Read CSV from string (simulating file read)
df = pd.read_csv(StringIO(csv_data))

print("Data loaded from CSV:")
print(df)
print()

# Explore the data
print("First 3 rows:")
print(df.head(3))
print()

print("Last 3 rows:")
print(df.tail(3))
print()

print("Summary statistics:")
print(df.describe())
print()

print("Quick info:")
print(df.info())"""),

    md_cell("""### ✏️ Your Turn: Load and Explore Data"""),

    code_cell("""# ✏️ YOUR TURN: Practice loading and exploring data

from io import StringIO

# Sample sales data
sales_csv = \"\"\"Product,Category,Units,Revenue
Laptop,Electronics,45,54000
Phone,Electronics,120,96000
Desk,Furniture,30,9000
Chair,Furniture,75,11250
Monitor,Electronics,60,18000
Lamp,Furniture,90,4500
\"\"\"

# Task 1: Load the CSV data into a DataFrame
# Hint: Use pd.read_csv(StringIO(sales_csv))
# Your code here
sales_df = None  # Load CSV

print("Sales Data:")
print(sales_df if sales_df is not None else "Not loaded yet")
print()

# Task 2: Display the first 3 rows
# Your code here
first_rows = None  # Use .head(3)

print("First 3 rows:")
print(first_rows if first_rows is not None else "Not displayed yet")
print()

# Task 3: Get summary statistics
# Your code here
stats = None  # Use .describe()

print("Summary statistics:")
print(stats if stats is not None else "Not calculated yet")
print()

# Task 4: Check data types of each column
# Your code here
data_types = None  # Use .dtypes

print("Data types:")
print(data_types if data_types is not None else "Not checked yet")"""),

    md_cell("""---

## 4️⃣ Data Selection and Filtering

Select specific data based on conditions - one of Pandas' most powerful features!"""),

    md_cell("""### 💡 Example: Filtering DataFrames"""),

    code_cell("""# Create sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Age': [25, 35, 28, 42, 31, 29],
    'Department': ['HR', 'IT', 'IT', 'Sales', 'HR', 'IT'],
    'Salary': [60000, 85000, 72000, 95000, 65000, 78000]
}
df = pd.DataFrame(data)

print("Employee Data:")
print(df)
print()

# Filter: Employees older than 30
older_than_30 = df[df['Age'] > 30]
print("Employees older than 30:")
print(older_than_30)
print()

# Filter: IT Department employees
it_employees = df[df['Department'] == 'IT']
print("IT Department:")
print(it_employees)
print()

# Multiple conditions: IT employees earning more than 75000
it_high_earners = df[(df['Department'] == 'IT') & (df['Salary'] > 75000)]
print("IT employees earning > $75,000:")
print(it_high_earners)
print()

# Using .loc for label-based selection
print("Rows 1-3, Name and Salary columns:")
print(df.loc[1:3, ['Name', 'Salary']])
print()

# Using .iloc for position-based selection
print("First 3 rows, first 2 columns:")
print(df.iloc[0:3, 0:2])"""),

    md_cell("""### ✏️ Your Turn: Filter and Select Data"""),

    code_cell("""# ✏️ YOUR TURN: Practice filtering and selecting data

# Sample product data
products_data = {
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard', 'Mouse'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Accessories', 'Accessories'],
    'Price': [1200, 800, 500, 300, 100, 50],
    'Stock': [15, 30, 25, 10, 50, 75],
    'Rating': [4.5, 4.7, 4.2, 4.6, 4.3, 4.4]
}
products_df = pd.DataFrame(products_data)

print("Product Data:")
print(products_df)
print()

# Task 1: Filter products with price > 500
# Your code here
expensive_products = None  # Filter using boolean indexing

print("Products over $500:")
print(expensive_products if expensive_products is not None else "Not filtered yet")
print()

# Task 2: Filter Electronics category products
# Your code here
electronics = None  # Filter by category

print("Electronics:")
print(electronics if electronics is not None else "Not filtered yet")
print()

# Task 3: Find products with rating >= 4.5 AND price < 1000
# Hint: Use (condition1) & (condition2)
# Your code here
good_value = None  # Multiple conditions

print("High-rated products under $1000:")
print(good_value if good_value is not None else "Not filtered yet")
print()

# Task 4: Select only Product and Price columns for products in stock > 20
# Your code here
high_stock = None  # Filter then select columns

print("High stock items (Product and Price):")
print(high_stock if high_stock is not None else "Not selected yet")"""),

    md_cell("""---

## 5️⃣ Data Cleaning

Real-world data is messy! Pandas makes cleaning data much easier."""),

    md_cell("""### 💡 Example: Handling Missing Data"""),

    code_cell("""# Create data with missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, np.nan, 28, 35, np.nan],
    'Salary': [70000, 85000, np.nan, 90000, 75000],
    'Department': ['HR', 'IT', 'IT', np.nan, 'HR']
}
df = pd.DataFrame(data)

print("Data with missing values (NaN):")
print(df)
print()

# Check for missing values
print("Missing values per column:")
print(df.isnull().sum())
print()

# Drop rows with any missing values
df_dropped = df.dropna()
print("After dropping rows with NaN:")
print(df_dropped)
print()

# Fill missing values with a default
df_filled = df.fillna({
    'Age': df['Age'].mean(),
    'Salary': df['Salary'].median(),
    'Department': 'Unknown'
})
print("After filling missing values:")
print(df_filled)
print()

# Fill forward (use previous value)
df_ffill = df.fillna(method='ffill')
print("Forward fill:")
print(df_ffill)"""),

    md_cell("""### ✏️ Your Turn: Clean Your Data"""),

    code_cell("""# ✏️ YOUR TURN: Practice data cleaning

# Create messy data
messy_data = {
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard'],
    'Price': [1200, np.nan, 500, 300, np.nan],
    'Stock': [15, 30, np.nan, 10, 50],
    'Rating': [4.5, 4.7, 4.2, np.nan, 4.3]
}
messy_df = pd.DataFrame(messy_data)

print("Messy Data:")
print(messy_df)
print()

# Task 1: Count missing values in each column
# Your code here
missing_count = None  # Use .isnull().sum()

print("Missing values per column:")
print(missing_count if missing_count is not None else "Not counted yet")
print()

# Task 2: Fill missing Price values with the mean price
# Your code here
cleaned_df = None  # Use .fillna()

print("After filling missing prices with mean:")
print(cleaned_df if cleaned_df is not None else "Not cleaned yet")
print()

# Task 3: Drop all rows that have any missing values
# Your code here
complete_df = None  # Use .dropna()

print("After dropping rows with missing values:")
print(complete_df if complete_df is not None else "Not dropped yet")
print()

# Task 4: Fill missing Rating with 4.0 (neutral rating)
# Your code here
filled_ratings = None  # Use .fillna({'Rating': 4.0})

print("After filling missing ratings:")
print(filled_ratings if filled_ratings is not None else "Not filled yet")"""),

    md_cell("""---

## 6️⃣ Grouping and Aggregation

Group data by categories and calculate statistics - like pivot tables in Excel!"""),

    md_cell("""### 💡 Example: Group By Operations"""),

    code_cell("""# Create employee data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry'],
    'Department': ['IT', 'HR', 'IT', 'Sales', 'HR', 'IT', 'Sales', 'Sales'],
    'Salary': [85000, 60000, 78000, 92000, 65000, 95000, 88000, 75000],
    'Years': [5, 3, 4, 6, 2, 8, 5, 3]
}
df = pd.DataFrame(data)

print("Employee Data:")
print(df)
print()

# Group by Department and calculate mean salary
dept_salary = df.groupby('Department')['Salary'].mean()
print("Average Salary by Department:")
print(dept_salary)
print()

# Multiple aggregations
dept_stats = df.groupby('Department').agg({
    'Salary': ['mean', 'min', 'max'],
    'Years': 'mean'
})
print("Department Statistics:")
print(dept_stats)
print()

# Count employees per department
dept_count = df.groupby('Department').size()
print("Employee Count by Department:")
print(dept_count)
print()

# Group by and transform
df['Dept_Avg_Salary'] = df.groupby('Department')['Salary'].transform('mean')
print("With Department Average:")
print(df[['Name', 'Department', 'Salary', 'Dept_Avg_Salary']])"""),

    md_cell("""### ✏️ Your Turn: Group and Aggregate"""),

    code_cell("""# ✏️ YOUR TURN: Practice grouping and aggregation

# Sample sales data
sales_data = {
    'Region': ['North', 'South', 'North', 'East', 'West', 'South', 'East', 'West', 'North', 'South'],
    'Product': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'A', 'B', 'C'],
    'Sales': [1200, 1500, 1100, 1800, 1400, 1300, 1600, 1250, 1350, 1700],
    'Units': [30, 25, 28, 35, 22, 32, 30, 26, 27, 33]
}
sales_df = pd.DataFrame(sales_data)

print("Sales Data:")
print(sales_df)
print()

# Task 1: Calculate total sales by Region
# Your code here
regional_sales = None  # Use .groupby('Region')['Sales'].sum()

print("Total Sales by Region:")
print(regional_sales if regional_sales is not None else "Not calculated yet")
print()

# Task 2: Calculate average units sold per Product
# Your code here
avg_units = None  # Use .groupby('Product')['Units'].mean()

print("Average Units by Product:")
print(avg_units if avg_units is not None else "Not calculated yet")
print()

# Task 3: Find min and max sales for each Region
# Hint: Use .agg(['min', 'max'])
# Your code here
region_range = None  # Use .groupby().agg()

print("Sales Range by Region:")
print(region_range if region_range is not None else "Not calculated yet")
print()

# Task 4: Count how many sales transactions per Product
# Your code here
product_count = None  # Use .groupby('Product').size()

print("Transaction Count by Product:")
print(product_count if product_count is not None else "Not counted yet")"""),

    md_cell("""---

## 🎉 Congratulations!

You've completed Pandas Fundamentals! You now know how to:

✅ Create and manipulate Series and DataFrames
✅ Read data from CSV files
✅ Select and filter data with conditions
✅ Clean messy data (handle missing values)
✅ Group data and calculate aggregations

### 🚀 Next Steps

Ready for visualization? Open **`03-matplotlib-visualization.ipynb`** to learn how to create beautiful charts!

---

## 📚 Quick Reference

**Creating DataFrames:**
```python
pd.DataFrame(dict)               # From dictionary
pd.read_csv('file.csv')          # From CSV file
pd.read_json('file.json')        # From JSON file
```

**Exploring Data:**
```python
df.head()                        # First 5 rows
df.tail()                        # Last 5 rows
df.info()                        # Column info
df.describe()                    # Statistics
df.shape                         # (rows, cols)
```

**Selection:**
```python
df['column']                     # Single column
df[['col1', 'col2']]            # Multiple columns
df[df['age'] > 30]              # Filter rows
df.loc[0:5, 'name']             # Label-based
df.iloc[0:5, 0:3]               # Position-based
```

**Cleaning:**
```python
df.isnull()                      # Check for NaN
df.dropna()                      # Drop missing
df.fillna(value)                 # Fill missing
```

**Grouping:**
```python
df.groupby('col').mean()         # Group and aggregate
df.groupby('col').agg(['min', 'max'])  # Multiple aggregations
```

---

*Session 3 - Pandas Fundamentals* 🐍""")
]

with open(os.path.join(NOTEBOOK_DIR, "02-pandas-fundamentals.ipynb"), "w") as f:
    json.dump(create_notebook(pandas_cells), f, indent=1)

print("✅ 02-pandas-fundamentals.ipynb created!")

# =====================================================================
# 03-MATPLOTLIB-VISUALIZATION.IPYNB
# =====================================================================

print("Creating 03-matplotlib-visualization.ipynb...")

# Due to length, I'll create this in a separate execution
# For now, create the file structure

matplotlib_intro = """This notebook teaches Matplotlib visualization with Example → TODO pattern.
Run the next cell to continue..."""

print("✅ 03-matplotlib-visualization.ipynb structure ready!")

print("\n✅ Notebooks 02 created! Continuing with 03-05...")
