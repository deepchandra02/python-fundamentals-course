#!/usr/bin/env python3
"""
Script to create all Session 3 notebooks with Example → TODO pattern
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

# =====================================================================
# 01-NUMPY-BASICS.IPYNB
# =====================================================================

numpy_cells = [
    md_cell("""# 📊 NumPy Basics - Session 3
## Python Fundamentals Workshop: Data Science & ML

**What you'll learn in this notebook:**
- ✅ Create and manipulate NumPy arrays
- ✅ Perform array indexing and slicing
- ✅ Execute mathematical operations on arrays
- ✅ Reshape and transform arrays
- ✅ Filter arrays using boolean indexing

**Estimated time:** 30-40 minutes

---"""),

    md_cell("""## 🎯 Why NumPy?

NumPy (Numerical Python) is the foundation of data science in Python:

- **Fast:** Operations are 50-100x faster than Python lists
- **Memory efficient:** Uses less memory than lists
- **Powerful:** Built-in mathematical functions
- **Foundation:** Required by Pandas, Matplotlib, and most ML libraries

Let's start by importing NumPy!"""),

    code_cell("""import numpy as np

print(f"NumPy version: {np.__version__}")
print("✅ NumPy imported successfully!")"""),

    md_cell("""---

## 1️⃣ Creating Arrays

NumPy arrays are the fundamental data structure for numerical computing. Let's explore different ways to create them."""),

    md_cell("""### 💡 Example: Creating Arrays from Lists"""),

    code_cell("""# Create a 1D array from a Python list
temperatures = np.array([22, 25, 19, 23, 28, 30, 27])
print("Daily temperatures (°C):", temperatures)
print("Type:", type(temperatures))
print("Shape:", temperatures.shape)
print()

# Create a 2D array (matrix)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("2D Matrix:")
print(matrix)
print("Shape:", matrix.shape)  # (3 rows, 3 columns)"""),

    md_cell("""### ✏️ Your Turn: Create Arrays"""),

    code_cell("""# ✏️ YOUR TURN: Create different types of arrays
#
# Task 1: Create an array of numbers from 0 to 9 using np.arange()
# Hint: np.arange(start, stop) creates a range of numbers

# Your code here
numbers = None  # Replace with np.arange(...)

print("Numbers:", numbers)
print()

# Task 2: Create a 3x3 array filled with zeros using np.zeros()
# Hint: np.zeros((rows, cols)) creates an array of zeros

# Your code here
zeros_array = None  # Replace with np.zeros(...)

print("Zeros array:")
print(zeros_array)
print()

# Task 3: Create a 2x4 array filled with ones using np.ones()
# Hint: Similar to zeros, but use np.ones()

# Your code here
ones_array = None  # Replace with np.ones(...)

print("Ones array:")
print(ones_array)
print()

# Task 4: Create an array of 5 random numbers between 0 and 1
# Hint: Use np.random.random(size)

# Your code here
random_array = None  # Replace with np.random.random(...)

print("Random array:", random_array)"""),

    md_cell("""### 🎯 Expected Output
After completing the tasks above, you should see:
- An array with numbers 0-9
- A 3x3 matrix of zeros
- A 2x4 matrix of ones
- 5 random decimal numbers between 0 and 1"""),

    md_cell("""---

## 2️⃣ Array Indexing and Slicing

Access specific elements or portions of arrays using indexing and slicing."""),

    md_cell("""### 💡 Example: Accessing Array Elements"""),

    code_cell("""# Create sample data: weekly sales
sales = np.array([150, 200, 180, 220, 190, 250, 210])
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

print("Weekly Sales:", sales)
print()

# Single element access
print(f"Monday sales: ${sales[0]}")
print(f"Sunday sales: ${sales[-1]}")
print()

# Slicing: array[start:stop]
weekday_sales = sales[0:5]  # Monday to Friday
weekend_sales = sales[5:]   # Saturday and Sunday

print("Weekday sales:", weekday_sales)
print("Weekend sales:", weekend_sales)
print()

# 2D array indexing
data = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]])

print("2D Array:")
print(data)
print()
print("Element at row 1, col 2:", data[1, 2])  # 60
print("First row:", data[0, :])  # All columns of first row
print("Last column:", data[:, -1])  # All rows of last column"""),

    md_cell("""### ✏️ Your Turn: Slice and Dice Arrays"""),

    code_cell("""# ✏️ YOUR TURN: Practice array indexing and slicing

# Sample data: monthly revenue (in thousands)
revenue = np.array([45, 52, 48, 61, 58, 72, 68, 75, 70, 80, 85, 90])
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

print("Monthly Revenue (in $1000s):", revenue)
print()

# Task 1: Get the revenue for March (index 2)
# Your code here
march_revenue = None  # Use indexing

print(f"March revenue: ${march_revenue}k")
print()

# Task 2: Get Q1 revenue (first 3 months: Jan, Feb, Mar)
# Hint: Use slicing [start:stop]
# Your code here
q1_revenue = None  # Use slicing

print("Q1 Revenue:", q1_revenue)
print(f"Q1 Total: ${q1_revenue.sum() if q1_revenue is not None else 0}k")
print()

# Task 3: Get the last quarter (Oct, Nov, Dec)
# Hint: Use negative indexing or [-3:]
# Your code here
q4_revenue = None  # Use slicing

print("Q4 Revenue:", q4_revenue)
print(f"Q4 Total: ${q4_revenue.sum() if q4_revenue is not None else 0}k")
print()

# Task 4: Get every other month (Jan, Mar, May, Jul, Sep, Nov)
# Hint: Use step in slicing [start:stop:step]
# Your code here
alternate_months = None  # Use slicing with step

print("Every other month:", alternate_months)"""),

    md_cell("""---

## 3️⃣ Array Operations

NumPy allows vectorized operations - perform calculations on entire arrays without loops!"""),

    md_cell("""### 💡 Example: Mathematical Operations"""),

    code_cell("""# Product prices in USD
prices_usd = np.array([10, 25, 15, 30, 20])
print("Prices (USD):", prices_usd)
print()

# Vectorized operations - apply to ALL elements at once

# Add 20% tax to all prices
prices_with_tax = prices_usd * 1.20
print("Prices with 20% tax:", prices_with_tax)
print()

# Convert to EUR (assume 1 USD = 0.92 EUR)
prices_eur = prices_usd * 0.92
print("Prices (EUR):", prices_eur)
print()

# Apply 50% discount
discounted_prices = prices_usd / 2
print("50% off prices:", discounted_prices)
print()

# Statistical operations
print("=" * 40)
print("Statistical Summary:")
print(f"Sum: ${prices_usd.sum()}")
print(f"Mean (average): ${prices_usd.mean():.2f}")
print(f"Median: ${np.median(prices_usd):.2f}")
print(f"Min: ${prices_usd.min()}")
print(f"Max: ${prices_usd.max()}")
print(f"Standard deviation: ${prices_usd.std():.2f}")"""),

    md_cell("""### ✏️ Your Turn: Perform Array Calculations"""),

    code_cell("""# ✏️ YOUR TURN: Practice array operations

# Student test scores (out of 100)
scores = np.array([78, 85, 92, 68, 88, 76, 95, 82, 90, 72])
print("Original Test Scores:", scores)
print()

# Task 1: Add 5 bonus points to all scores
# Hint: Just add 5 to the entire array
# Your code here
bonus_scores = None  # Add bonus points

print("Scores with bonus:", bonus_scores)
print()

# Task 2: Calculate the average score
# Hint: Use .mean() method
# Your code here
average_score = None  # Calculate average

print(f"Average score: {average_score:.2f}" if average_score else "Not calculated yet")
print()

# Task 3: Find the highest and lowest scores
# Hint: Use .max() and .min() methods
# Your code here
highest_score = None  # Find max
lowest_score = None   # Find min

print(f"Highest score: {highest_score}" if highest_score else "Not calculated")
print(f"Lowest score: {lowest_score}" if lowest_score else "Not calculated")
print()

# Task 4: Calculate the range (difference between max and min)
# Your code here
score_range = None  # Calculate range

print(f"Score range: {score_range}" if score_range else "Not calculated")
print()

# Task 5: Round all scores to nearest 10 (e.g., 78 → 80, 92 → 90)
# Hint: Divide by 10, round, multiply by 10. Use np.round()
# Your code here
rounded_scores = None  # Round to nearest 10

print("Scores rounded to nearest 10:", rounded_scores)"""),

    md_cell("""---

## 4️⃣ Reshaping Arrays

Change the shape of arrays without changing their data."""),

    md_cell("""### 💡 Example: Reshape Arrays"""),

    code_cell("""# Create a 1D array of 12 numbers
data = np.arange(1, 13)
print("Original 1D array:")
print(data)
print("Shape:", data.shape)
print()

# Reshape to 3 rows x 4 columns
matrix_3x4 = data.reshape(3, 4)
print("Reshaped to 3x4:")
print(matrix_3x4)
print("Shape:", matrix_3x4.shape)
print()

# Reshape to 4 rows x 3 columns
matrix_4x3 = data.reshape(4, 3)
print("Reshaped to 4x3:")
print(matrix_4x3)
print("Shape:", matrix_4x3.shape)
print()

# Reshape to 2 rows x 6 columns
matrix_2x6 = data.reshape(2, 6)
print("Reshaped to 2x6:")
print(matrix_2x6)
print("Shape:", matrix_2x6.shape)
print()

# Flatten back to 1D
flattened = matrix_3x4.flatten()
print("Flattened back to 1D:")
print(flattened)
print("Shape:", flattened.shape)"""),

    md_cell("""### ✏️ Your Turn: Reshape Practice"""),

    code_cell("""# ✏️ YOUR TURN: Practice reshaping arrays

# Create an array of 24 numbers (representing 24 hours of temperature data)
hourly_temps = np.arange(20, 44)  # Temperatures from 20°C to 43°C
print("24-hour temperature data:")
print(hourly_temps)
print("Shape:", hourly_temps.shape)
print()

# Task 1: Reshape into 4 rows x 6 columns (4 quarters of 6 hours each)
# Hint: Use .reshape(rows, cols)
# Your code here
temps_4x6 = None  # Reshape to 4x6

print("Reshaped to 4x6 (4 quarters):")
print(temps_4x6 if temps_4x6 is not None else "Not reshaped yet")
print()

# Task 2: Reshape into 6 rows x 4 columns
# Your code here
temps_6x4 = None  # Reshape to 6x4

print("Reshaped to 6x4:")
print(temps_6x4 if temps_6x4 is not None else "Not reshaped yet")
print()

# Task 3: Reshape into 3D array: 2 x 3 x 4
# This could represent: 2 days x 3 time periods x 4 hours
# Hint: reshape works with any number of dimensions
# Your code here
temps_3d = None  # Reshape to 2x3x4

print("Reshaped to 3D (2x3x4):")
print(temps_3d if temps_3d is not None else "Not reshaped yet")
if temps_3d is not None:
    print("Shape:", temps_3d.shape)
print()

# Task 4: Flatten the 3D array back to 1D
# Hint: Use .flatten()
# Your code here
temps_flat = None  # Flatten

print("Flattened back to 1D:")
print(temps_flat if temps_flat is not None else "Not flattened yet")"""),

    md_cell("""---

## 5️⃣ Boolean Indexing and Filtering

Filter arrays based on conditions - incredibly powerful for data analysis!"""),

    md_cell("""### 💡 Example: Filter Arrays with Conditions"""),

    code_cell("""# Daily step counts for 2 weeks
steps = np.array([8500, 12000, 9800, 7500, 11200, 13000, 6800,
                  9200, 10500, 8800, 11800, 9500, 12500, 10000])

print("Daily step counts:")
print(steps)
print()

# Create a boolean mask: which days had 10,000+ steps?
goal_met = steps >= 10000
print("Days that met 10k goal (True/False):")
print(goal_met)
print()

# Use the mask to filter the array
high_activity_days = steps[goal_met]
print("Step counts on days that met goal:")
print(high_activity_days)
print(f"Number of days goal was met: {len(high_activity_days)}")
print()

# Shorthand: combine condition and filtering in one line
low_activity_days = steps[steps < 9000]
print("Step counts on low activity days (<9000):")
print(low_activity_days)
print()

# Multiple conditions using & (and) or | (or)
moderate_days = steps[(steps >= 9000) & (steps < 11000)]
print("Moderate activity days (9000-11000 steps):")
print(moderate_days)"""),

    md_cell("""### ✏️ Your Turn: Filter Like a Pro"""),

    code_cell("""# ✏️ YOUR TURN: Practice boolean indexing and filtering

# Product sales data (units sold per day for 15 days)
sales = np.array([45, 67, 89, 34, 56, 78, 92, 43, 71, 88, 39, 95, 62, 81, 76])

print("Daily sales (units):")
print(sales)
print()

# Task 1: Find all days where sales exceeded 70 units
# Hint: Use sales > 70
# Your code here
high_sales_days = None  # Filter for sales > 70

print("Days with high sales (>70 units):")
print(high_sales_days if high_sales_days is not None else "Not filtered yet")
print(f"Number of high sales days: {len(high_sales_days) if high_sales_days is not None else 0}")
print()

# Task 2: Find days with low sales (less than 50 units)
# Your code here
low_sales_days = None  # Filter for sales < 50

print("Days with low sales (<50 units):")
print(low_sales_days if low_sales_days is not None else "Not filtered yet")
print()

# Task 3: Find days with sales in the target range (60-80 units)
# Hint: Use (sales >= 60) & (sales <= 80)
# Note: Use & for 'and', and wrap each condition in parentheses
# Your code here
target_range_days = None  # Filter for 60-80 range

print("Days in target range (60-80 units):")
print(target_range_days if target_range_days is not None else "Not filtered yet")
print()

# Task 4: Calculate average sales for high-performing days (>70)
# Hint: First filter, then use .mean()
# Your code here
avg_high_sales = None  # Average of days with sales > 70

print(f"Average sales on high-performing days: {avg_high_sales:.2f} units" if avg_high_sales is not None else "Not calculated yet")
print()

# Task 5: Count how many days had sales exactly at or above the median
# Hint: First calculate median with np.median(), then filter
# Your code here
median_sales = None  # Calculate median
above_median = None  # Filter for >= median

print(f"Median sales: {median_sales}" if median_sales is not None else "Median not calculated")
print(f"Days at or above median: {len(above_median) if above_median is not None else 0}")"""),

    md_cell("""---

## 🎉 Congratulations!

You've completed NumPy Basics! You now know how to:

✅ Create arrays using various methods
✅ Access elements with indexing and slicing
✅ Perform vectorized mathematical operations
✅ Reshape arrays into different dimensions
✅ Filter data using boolean indexing

### 🚀 Next Steps

Ready to move on? Open **`02-pandas-fundamentals.ipynb`** to learn how to work with structured data!

---

## 📚 Quick Reference

**Creating Arrays:**
```python
np.array([1, 2, 3])          # From list
np.arange(0, 10)             # Range of numbers
np.zeros((3, 4))             # Array of zeros
np.ones((2, 3))              # Array of ones
np.random.random(5)          # Random numbers
```

**Indexing & Slicing:**
```python
arr[0]                       # First element
arr[-1]                      # Last element
arr[1:4]                     # Elements 1 to 3
arr[::2]                     # Every other element
```

**Operations:**
```python
arr.sum()                    # Sum all elements
arr.mean()                   # Average
arr.min(), arr.max()         # Min and max
arr.std()                    # Standard deviation
```

**Reshaping:**
```python
arr.reshape(3, 4)            # Change shape
arr.flatten()                # Convert to 1D
```

**Filtering:**
```python
arr[arr > 10]                # Values greater than 10
arr[(arr >= 5) & (arr < 20)] # Multiple conditions
```

---

*Session 3 - NumPy Basics* 🐍""")
]

# Save NumPy notebook
print("Creating 01-numpy-basics.ipynb...")
with open(os.path.join(NOTEBOOK_DIR, "01-numpy-basics.ipynb"), "w") as f:
    json.dump(create_notebook(numpy_cells), f, indent=1)
print("✅ 01-numpy-basics.ipynb created!")

print("\n✅ All notebooks created successfully!")
