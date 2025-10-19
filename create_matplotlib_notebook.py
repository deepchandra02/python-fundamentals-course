#!/usr/bin/env python3
import json
import os

NOTEBOOK_DIR = "notebooks/Session 3"

def create_notebook(cells):
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
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
    return {"cell_type": "markdown", "metadata": {}, "source": content.split("\n")}

def code_cell(content):
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": content.split("\n")}

print("Creating 03-matplotlib-visualization.ipynb...")

cells = [
    md_cell("""# 📊 Matplotlib Visualization - Session 3
## Python Fundamentals Workshop: Data Science & ML

**What you'll learn in this notebook:**
- ✅ Create basic line plots
- ✅ Make scatter plots for relationships
- ✅ Build bar charts for comparisons
- ✅ Customize plots with labels, titles, and legends
- ✅ Create multi-panel dashboards with subplots
- ✅ Make pie charts and histograms

**Estimated time:** 40-50 minutes

---"""),

    md_cell("""## 🎯 Why Matplotlib?

Matplotlib is the foundational plotting library for Python:

- **Versatile:** Create any type of visualization
- **Customizable:** Control every aspect of your plots
- **Industry standard:** Used everywhere in data science
- **Foundation:** Powers other libraries like Seaborn and Pandas plotting

A picture is worth a thousand words - let's start visualizing!"""),

    code_cell("""import matplotlib.pyplot as plt
import numpy as np

print("✅ Matplotlib imported successfully!")
print("Let's create some beautiful visualizations!")"""),

    md_cell("""---

## 1️⃣ Basic Line Plots

Line plots are perfect for showing trends over time or continuous data."""),

    md_cell("""### 💡 Example: Simple Line Plot"""),

    code_cell("""# Daily temperature data
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures = [22, 25, 23, 27, 26, 24, 25]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(days, temperatures, marker='o', linewidth=2, markersize=8, color='coral')

# Add labels and title
plt.title('Weekly Temperature Trend', fontsize=16, fontweight='bold')
plt.xlabel('Day of Week', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.grid(True, alpha=0.3)

plt.show()

print("📈 Line plot created!")"""),

    md_cell("""### ✏️ Your Turn: Create a Line Plot"""),

    code_cell("""# ✏️ YOUR TURN: Create a line plot showing daily step counts

# Data: Your daily steps for a week
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
steps = [8500, 10200, 7800, 11500, 9200, 12000, 10800]

# Task 1: Create a figure
# Hint: plt.figure(figsize=(10, 6))
# Your code here


# Task 2: Create a line plot with markers
# Hint: plt.plot(x, y, marker='o', color='blue', linewidth=2)
# Your code here


# Task 3: Add title: "My Weekly Step Count"
# Your code here


# Task 4: Add labels: xlabel='Day', ylabel='Steps'
# Your code here


# Task 5: Add a grid
# Your code here


# Task 6: Show the plot
# Your code here


print("✅ Your line plot should appear above!")"""),

    md_cell("""---

## 2️⃣ Scatter Plots

Scatter plots show relationships between two variables."""),

    md_cell("""### 💡 Example: Scatter Plot with Color Coding"""),

    code_cell("""# Study time vs test scores
study_hours = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
test_scores = [65, 70, 75, 78, 82, 85, 88, 90, 92, 95]
student_ids = range(1, 11)

# Create scatter plot
plt.figure(figsize=(10, 6))
scatter = plt.scatter(study_hours, test_scores, 
                     s=200,  # Size of points
                     c=test_scores,  # Color based on scores
                     cmap='viridis',  # Color map
                     alpha=0.7,  # Transparency
                     edgecolors='black',  # Border color
                     linewidth=2)

# Add colorbar to show score scale
plt.colorbar(scatter, label='Test Score')

plt.title('Study Time vs Test Score', fontsize=16, fontweight='bold')
plt.xlabel('Study Hours', fontsize=12)
plt.ylabel('Test Score', fontsize=12)
plt.grid(True, alpha=0.3)

plt.show()

print("📊 Scatter plot created!")"""),

    md_cell("""### ✏️ Your Turn: Create a Scatter Plot"""),

    code_cell("""# ✏️ YOUR TURN: Create a scatter plot showing price vs rating

# Data: Product prices and customer ratings
prices = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
ratings = [3.8, 4.0, 4.2, 4.1, 4.5, 4.3, 4.6, 4.4, 4.7, 4.8]

# Task 1: Create a figure
# Your code here


# Task 2: Create a scatter plot
# Hint: plt.scatter(x, y, s=100, c='red', alpha=0.6)
# Your code here


# Task 3: Add title: "Product Price vs Rating"
# Your code here


# Task 4: Add xlabel='Price ($)' and ylabel='Rating (out of 5)'
# Your code here


# Task 5: Add a grid
# Your code here


# Task 6: Show the plot
# Your code here


print("✅ Your scatter plot should appear above!")"""),

    md_cell("""---

## 3️⃣ Bar Charts

Bar charts are excellent for comparing categories."""),

    md_cell("""### 💡 Example: Colorful Bar Chart"""),

    code_cell("""# Monthly sales by product
products = ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard']
sales = [45, 78, 32, 56, 23]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']

# Create bar chart
plt.figure(figsize=(12, 6))
bars = plt.bar(products, sales, color=colors, edgecolor='black', linewidth=1.5)

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}',
             ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.title('Monthly Sales by Product', fontsize=16, fontweight='bold')
plt.xlabel('Product', fontsize=12)
plt.ylabel('Units Sold', fontsize=12)
plt.grid(axis='y', alpha=0.3)

plt.show()

print("📊 Bar chart created!")"""),

    md_cell("""### ✏️ Your Turn: Create a Bar Chart"""),

    code_cell("""# ✏️ YOUR TURN: Create a bar chart showing employee count by department

# Data: Department names and employee counts
departments = ['Engineering', 'Sales', 'Marketing', 'HR', 'Finance']
employee_count = [45, 32, 28, 15, 20]

# Task 1: Create a figure
# Your code here


# Task 2: Create a bar chart
# Hint: plt.bar(categories, values, color='skyblue')
# Your code here


# Task 3: Add title: "Employees by Department"
# Your code here


# Task 4: Add labels
# Your code here


# Task 5: Add a grid on the y-axis
# Hint: plt.grid(axis='y', alpha=0.3)
# Your code here


# Task 6: Show the plot
# Your code here


print("✅ Your bar chart should appear above!")"""),

    md_cell("""---

## 4️⃣ Customization: Labels, Titles, and Legends

Make your plots professional and informative!"""),

    md_cell("""### 💡 Example: Fully Customized Plot"""),

    code_cell("""# Create data for multiple lines
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
revenue_2023 = [45, 52, 48, 61, 58, 72]
revenue_2024 = [50, 58, 55, 68, 65, 80]
target = [60, 60, 60, 60, 60, 60]

# Create plot
plt.figure(figsize=(12, 7))

# Plot three lines
plt.plot(months, revenue_2023, marker='o', linewidth=2, markersize=8, 
         color='#3498db', label='2023 Revenue')
plt.plot(months, revenue_2024, marker='s', linewidth=2, markersize=8, 
         color='#2ecc71', label='2024 Revenue')
plt.plot(months, target, linestyle='--', linewidth=2, color='#e74c3c', 
         label='Target')

# Customization
plt.title('Revenue Comparison: 2023 vs 2024', 
          fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Month', fontsize=14, fontweight='bold')
plt.ylabel('Revenue ($1000s)', fontsize=14, fontweight='bold')

# Legend
plt.legend(loc='upper left', fontsize=12, frameon=True, shadow=True)

# Grid
plt.grid(True, alpha=0.3, linestyle='--')

# Tight layout
plt.tight_layout()

plt.show()

print("✨ Fully customized plot created!")"""),

    md_cell("""### ✏️ Your Turn: Customize Your Plot"""),

    code_cell("""# ✏️ YOUR TURN: Create a customized multi-line plot

# Data: Daily website visitors
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
desktop = [1200, 1350, 1180, 1420, 1380, 980, 1050]
mobile = [1800, 2100, 1950, 2250, 2180, 1650, 1720]

# Task 1: Create figure
# Your code here


# Task 2: Plot desktop visitors with blue line and circle markers
# Hint: Include label='Desktop'
# Your code here


# Task 3: Plot mobile visitors with green line and square markers
# Hint: marker='s', label='Mobile'
# Your code here


# Task 4: Add title: "Website Traffic by Device"
# Your code here


# Task 5: Add xlabel='Day' and ylabel='Visitors'
# Your code here


# Task 6: Add a legend
# Hint: plt.legend()
# Your code here


# Task 7: Add a grid
# Your code here


# Task 8: Show the plot
# Your code here


print("✅ Your customized plot should appear above!")"""),

    md_cell("""---

## 5️⃣ Subplots: Multi-Panel Dashboards

Create multiple plots in one figure!"""),

    md_cell("""### 💡 Example: 2x2 Dashboard"""),

    code_cell("""# Create data
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
sales = [120, 135, 128, 145, 150]
customers = [45, 52, 48, 58, 62]
avg_purchase = [2.67, 2.60, 2.67, 2.50, 2.42]
ratings = [4.2, 4.5, 4.3, 4.6, 4.8]

# Create 2x2 subplot grid
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Line plot
ax1.plot(days, sales, marker='o', color='#3498db', linewidth=2)
ax1.set_title('Daily Sales', fontsize=14, fontweight='bold')
ax1.set_ylabel('Sales ($)')
ax1.grid(True, alpha=0.3)

# Plot 2: Bar chart
ax2.bar(days, customers, color='#2ecc71')
ax2.set_title('Customer Count', fontsize=14, fontweight='bold')
ax2.set_ylabel('Customers')
ax2.grid(axis='y', alpha=0.3)

# Plot 3: Line plot
ax3.plot(days, avg_purchase, marker='s', color='#e74c3c', linewidth=2)
ax3.set_title('Average Purchase Value', fontsize=14, fontweight='bold')
ax3.set_xlabel('Day')
ax3.set_ylabel('Value ($)')
ax3.grid(True, alpha=0.3)

# Plot 4: Scatter plot
ax4.scatter(days, ratings, s=200, c=ratings, cmap='viridis')
ax4.set_title('Customer Ratings', fontsize=14, fontweight='bold')
ax4.set_xlabel('Day')
ax4.set_ylabel('Rating')
ax4.grid(True, alpha=0.3)

# Overall title
fig.suptitle('Weekly Business Dashboard', fontsize=18, fontweight='bold', y=0.995)

plt.tight_layout()
plt.show()

print("📊 Dashboard created with 4 subplots!")"""),

    md_cell("""### ✏️ Your Turn: Create a Dashboard"""),

    code_cell("""# ✏️ YOUR TURN: Create a 2x2 dashboard for fitness tracking

# Data
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
steps = [8500, 10200, 7800, 11500, 9200, 12000, 10800]
calories = [2100, 2300, 2000, 2500, 2200, 2600, 2400]
sleep_hours = [7, 6.5, 8, 7.5, 6, 8.5, 9]
water_glasses = [6, 7, 5, 8, 7, 9, 8]

# Task 1: Create a 2x2 subplot grid
# Hint: fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
# Your code here


# Task 2: Plot steps as a line plot in ax1
# Your code here


# Task 3: Plot calories as a bar chart in ax2
# Your code here


# Task 4: Plot sleep hours as a line plot in ax3
# Your code here


# Task 5: Plot water glasses as a bar chart in ax4
# Your code here


# Task 6: Add titles to each subplot
# Your code here


# Task 7: Add overall title "Weekly Fitness Dashboard"
# Hint: fig.suptitle('Title', fontsize=16)
# Your code here


# Task 8: Add tight_layout and show
# Your code here


print("✅ Your dashboard should appear above!")"""),

    md_cell("""---

## 6️⃣ Pie Charts and Histograms

Special plot types for specific use cases."""),

    md_cell("""### 💡 Example: Pie Chart and Histogram"""),

    code_cell("""# Create figure with 2 subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# PIE CHART: Budget allocation
categories = ['Housing', 'Food', 'Transport', 'Entertainment', 'Savings']
amounts = [1200, 600, 300, 200, 700]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
explode = (0.1, 0, 0, 0, 0.1)  # Explode Housing and Savings

ax1.pie(amounts, labels=categories, colors=colors, explode=explode,
        autopct='%1.1f%%', startangle=90, shadow=True)
ax1.set_title('Monthly Budget Allocation', fontsize=14, fontweight='bold')

# HISTOGRAM: Test scores distribution
np.random.seed(42)
test_scores = np.random.normal(75, 10, 100)  # Mean=75, SD=10, 100 students

ax2.hist(test_scores, bins=20, color='#3498db', edgecolor='black', alpha=0.7)
ax2.axvline(test_scores.mean(), color='red', linestyle='--', linewidth=2, 
            label=f'Mean: {test_scores.mean():.1f}')
ax2.set_title('Test Scores Distribution', fontsize=14, fontweight='bold')
ax2.set_xlabel('Score')
ax2.set_ylabel('Number of Students')
ax2.legend()
ax2.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

print("🥧 Pie chart and 📊 histogram created!")"""),

    md_cell("""### ✏️ Your Turn: Create Pie Chart and Histogram"""),

    code_cell("""# ✏️ YOUR TURN: Create a pie chart and histogram

# Task 1: Create a figure with 2 subplots (1 row, 2 columns)
# Hint: fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
# Your code here


# Task 2: Create a pie chart showing time spent on daily activities
# Data provided below
activities = ['Sleep', 'Work', 'Exercise', 'Meals', 'Leisure']
hours = [8, 9, 1, 2, 4]

# Your code here (create pie chart in ax1)


# Task 3: Add title "Daily Time Allocation" to pie chart
# Your code here


# Task 4: Create a histogram of daily step counts
# Data: Random step counts for 30 days
np.random.seed(42)
daily_steps = np.random.normal(9000, 1500, 30)

# Your code here (create histogram in ax2 with 15 bins)


# Task 5: Add title "30-Day Step Count Distribution" to histogram
# Your code here


# Task 6: Add xlabel 'Steps' and ylabel 'Days' to histogram
# Your code here


# Task 7: Add a vertical line at the mean
# Hint: ax2.axvline(daily_steps.mean(), color='red', linestyle='--')
# Your code here


# Task 8: Apply tight_layout and show
# Your code here


print("✅ Your pie chart and histogram should appear above!")"""),

    md_cell("""---

## 🎉 Congratulations!

You've completed Matplotlib Visualization! You now know how to:

✅ Create line plots for trends
✅ Make scatter plots for relationships
✅ Build bar charts for comparisons
✅ Customize plots with labels, titles, and legends
✅ Create multi-panel dashboards with subplots
✅ Make pie charts and histograms

### 🚀 Next Steps

Ready for real-world data analysis? Open **`04-data-exploration.ipynb`** to combine NumPy, Pandas, and Matplotlib!

---

## 📚 Quick Reference

**Basic Plots:**
```python
plt.plot(x, y)                   # Line plot
plt.scatter(x, y)                # Scatter plot
plt.bar(x, y)                    # Bar chart
plt.hist(data, bins=20)          # Histogram
plt.pie(sizes, labels=labels)    # Pie chart
```

**Customization:**
```python
plt.title('Title')               # Add title
plt.xlabel('X Label')            # X-axis label
plt.ylabel('Y Label')            # Y-axis label
plt.legend()                     # Add legend
plt.grid(True)                   # Add grid
```

**Subplots:**
```python
fig, (ax1, ax2) = plt.subplots(1, 2)  # 1 row, 2 cols
fig, axes = plt.subplots(2, 2)        # 2 rows, 2 cols
```

**Display:**
```python
plt.show()                       # Show plot
plt.savefig('plot.png')          # Save to file
plt.tight_layout()               # Optimize spacing
```

---

*Session 3 - Matplotlib Visualization* 🐍""")
]

with open(os.path.join(NOTEBOOK_DIR, "03-matplotlib-visualization.ipynb"), "w") as f:
    json.dump(create_notebook(cells), f, indent=1)

print("✅ 03-matplotlib-visualization.ipynb created!")
