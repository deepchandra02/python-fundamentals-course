# Matplotlib Complete Tutorial

## Table of Contents
1. [Introduction](#1-introduction)
2. [Getting Started](#2-getting-started)
3. [Pyplot](#3-pyplot)
4. [Plotting](#4-plotting)
5. [Markers](#5-markers)
6. [Line Styles](#6-line-styles)
7. [Labels and Titles](#7-labels-and-titles)
8. [Grid](#8-grid)
9. [Subplots](#9-subplots)
10. [Scatter Plots](#10-scatter-plots)
11. [Bar Charts](#11-bar-charts)
12. [Histograms](#12-histograms)
13. [Pie Charts](#13-pie-charts)

---

## 1. Introduction

### What is Matplotlib?

Matplotlib is a low-level graph plotting library in Python that serves as a visualization utility. Key characteristics include:

- Created by John D. Hunter
- Open source and freely usable
- Primarily written in Python
- Some segments written in C, Objective-C, and JavaScript for platform compatibility

### Codebase Location

The source code for Matplotlib is hosted on GitHub at:
[https://github.com/matplotlib/matplotlib](https://github.com/matplotlib/matplotlib)

### Purpose

Matplotlib functions as a "visualization utility" that allows Python developers to create various types of graphs and plots, including:

- Line plots
- Scatter plots
- Bar charts
- Pie charts
- Histograms
- Subplots

### Learning Resources

The W3Schools Matplotlib tutorial covers multiple aspects of the library, such as:

- Getting started
- Pyplot
- Plotting techniques
- Markers
- Labels
- Grids
- Subplot creation
- Different chart types

The tutorial provides a comprehensive introduction for developers looking to learn data visualization in Python using Matplotlib.

---

## 2. Getting Started

### Installation

To install Matplotlib, use pip:

```bash
pip install matplotlib
```

**Note:** If the pip command fails, consider using a Python distribution like Anaconda or Spyder that comes with Matplotlib pre-installed.

### Importing Matplotlib

After installation, import the library in your Python script:

```python
import matplotlib
```

### Checking Matplotlib Version

You can check the Matplotlib version using the `__version__` attribute:

```python
import matplotlib

print(matplotlib.__version__)
```

### Key Takeaways
- Matplotlib is easily installed via pip
- Use `import matplotlib` to use the library
- Check version with `matplotlib.__version__`

### Prerequisites
- Python installed
- PIP installed (recommended)

### Recommended Distributions
- Anaconda
- Spyder

These distributions often come with Matplotlib and other data science libraries pre-installed, making setup easier for beginners.

---

## 3. Pyplot

### Overview
Matplotlib's pyplot is a submodule that provides plotting utilities, typically imported as `plt`:

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Basic Plotting Example

The tutorial demonstrates a simple line plot from (0,0) to (6,250):

```python
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()
```

### Key Concepts

- Most Matplotlib utilities are found under the `pyplot` submodule
- Typically imported with the alias `plt`
- Allows creating various types of plots and visualizations
- Requires NumPy for array manipulation
- Uses `plt.plot()` to create basic line plots
- `plt.show()` displays the created plot

### Learning Progression

The tutorial suggests that subsequent chapters will cover more advanced plotting techniques, including:
- Drawing different types of plots
- Customizing plot elements
- Working with various plot types

### Practical Takeaway

Pyplot provides a simple, straightforward interface for creating data visualizations in Python, making it accessible for beginners while offering powerful capabilities for data representation.

---

## 4. Plotting

### Basic Plotting

Matplotlib's `plot()` function is used to create diagrams and charts with points and lines.

#### Key Concepts

- The x-axis represents the horizontal axis
- The y-axis represents the vertical axis
- Points are plotted using NumPy arrays

#### Simple Line Plot Example

```python
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()
```

### Plotting Markers Only

Use the 'o' shortcut to plot only markers:

```python
plt.plot(xpoints, ypoints, 'o')
plt.show()
```

### Multiple Points

You can plot multiple points by providing arrays with matching lengths:

```python
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()
```

### Default X-Points

If x-points are not specified, Matplotlib automatically assigns default values:

```python
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints)
plt.show()
```

In this case, x-points will be `[0, 1, 2, 3, 4, 5]`

### Key Takeaways

- Use `numpy.array()` to create point collections
- `plt.plot()` can draw lines and markers
- X-points can be explicitly defined or automatically generated
- Always call `plt.show()` to display the plot

---

## 5. Markers

### Overview
Matplotlib allows you to emphasize data points using various marker styles and customize their appearance.

### Marker Types
Matplotlib supports numerous marker types, including:

- Circle: `'o'`
- Star: `'*'`
- Point: `'.'`
- X: `'x'`
- Plus: `'+'`
- Square: `'s'`
- Triangle (multiple orientations): `'^'`, `'v'`, `'<'`, `'>'`

### Basic Example
```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker='o')
plt.show()
```

### Marker Customization

#### Size
Use `markersize` or `ms` to set marker size:
```python
plt.plot(ypoints, marker='o', ms=20)
```

#### Color
Customize marker colors using:
- `markeredgecolor` (marker edge)
- `markerfacecolor` (marker interior)
- Supports color names, hex values, and shorthand color codes

```python
plt.plot(ypoints, marker='o', ms=20, mec='r', mfc='r')
```

### Format String Notation
Combine marker, line, and color in a single string:
- Syntax: `'marker|line|color'`
- Example: `'o:r'` (circle marker, dotted line, red color)

### Key Concepts
- Markers highlight individual data points
- Highly customizable in size, color, and style
- Can be used with various plot types
- Supports both predefined and custom color specifications

---

## 6. Line Styles

### Line Styles

Matplotlib offers several line style options:

| Style Name | Shorthand | Example |
|-----------|-----------|---------|
| 'solid' (default) | '-' | Solid continuous line |
| 'dotted' | ':' | Discrete dots |
| 'dashed' | '--' | Broken line segments |
| 'dashdot' | '-.' | Alternating dash and dot |
| 'None' | '' or ' ' | No line |

### Customization Options

#### Line Color
- Use `color` or `c` parameter
- Supports:
  - Color names (e.g., 'r', 'hotpink')
  - Hexadecimal values (e.g., '#4CAF50')
  - 140 predefined color names

#### Line Width
- Use `linewidth` or `lw` parameter
- Value is a floating point number representing points
- Example: `linewidth = '20.5'`

### Code Example

```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

# Dotted red line with width 20.5
plt.plot(ypoints,
         linestyle=':',
         color='r',
         linewidth='20.5')
plt.show()
```

### Multiple Lines

You can plot multiple lines by:
1. Using multiple `plt.plot()` calls
2. Specifying x and y values for each line in a single `plt.plot()` call

---

## 7. Labels and Titles

### Creating Labels for Plots

#### X and Y Axis Labels

You can add labels to the x and y axes using `xlabel()` and `ylabel()` functions:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show()
```

### Adding a Plot Title

Use the `title()` function to set a plot title:

```python
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y)
plt.show()
```

### Customizing Font Properties

You can customize font properties using the `fontdict` parameter:

```python
font1 = {'family':'serif', 'color':'blue', 'size':20}
font2 = {'family':'serif', 'color':'darkred', 'size':15}

plt.title("Sports Watch Data", fontdict=font1)
plt.xlabel("Average Pulse", fontdict=font2)
plt.ylabel("Calorie Burnage", fontdict=font2)
```

### Title Positioning

The `loc` parameter allows you to position the title:

```python
plt.title("Sports Watch Data", loc='left')  # Options: 'left', 'right', 'center'
```

#### Key Concepts
- Use `xlabel()` and `ylabel()` to add axis labels
- Use `title()` to add a plot title
- Customize fonts with `fontdict`
- Position titles with the `loc` parameter
- Default title position is 'center'

---

## 8. Grid

### Adding Grid Lines to Plots

#### Basic Grid Usage

You can add grid lines to a Matplotlib plot using the `grid()` function:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)
plt.grid()  # Adds grid lines to the entire plot
plt.show()
```

#### Grid Line Axis Control

You can specify which axis to display grid lines on:

- `plt.grid(axis='x')`: Only x-axis grid lines
- `plt.grid(axis='y')`: Only y-axis grid lines
- `plt.grid(axis='both')`: Grid lines on both axes (default)

#### Customizing Grid Line Appearance

You can customize grid line properties:

```python
plt.grid(
    color='green',     # Grid line color
    linestyle='--',    # Line style (dashed)
    linewidth=0.5      # Thickness of grid lines
)
```

### Key Concepts

- The `grid()` function adds visual reference lines to your plot
- You can control which axes display grid lines
- Grid lines can be customized for color, style, and width
- Grid lines help improve readability of data visualization

### Best Practices

- Use grid lines sparingly to avoid cluttering the plot
- Choose grid line colors and styles that complement your data visualization
- Consider the context of your plot when adding grid lines

---

## 9. Subplots

### Key Concepts

#### Subplot Function
The `subplot()` function allows you to create multiple plots in a single figure. It takes three arguments:
- Number of rows
- Number of columns
- Index of the current plot

#### Basic Syntax
```python
plt.subplot(rows, columns, plot_index)
```

### Examples

#### Two Plots Side by Side
```python
import matplotlib.pyplot as plt
import numpy as np

# Plot 1
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)
plt.plot(x, y)

# Plot 2
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 2)
plt.plot(x, y)

plt.show()
```

#### Two Plots Vertically Stacked
```python
plt.subplot(2, 1, 1)  # 2 rows, 1 column, first plot
plt.subplot(2, 1, 2)  # 2 rows, 1 column, second plot
```

#### Multiple Plots (6 Plots Example)
```python
plt.subplot(2, 3, 1)  # 2 rows, 3 columns, first plot
plt.subplot(2, 3, 2)  # 2 rows, 3 columns, second plot
# ... continue for remaining plots
```

### Adding Titles

#### Individual Plot Titles
```python
plt.subplot(1, 2, 1)
plt.title("SALES")

plt.subplot(1, 2, 2)
plt.title("INCOME")
```

#### Figure Super Title
```python
plt.suptitle("MY SHOP")
```

### Key Takeaways
- Subplots allow multiple plots in one figure
- Customize layout with rows, columns, and plot index
- Add individual and overall titles
- Flexible for various visualization layouts

---

## 10. Scatter Plots

### Basic Scatter Plot Creation

A scatter plot is created using the `scatter()` function in Matplotlib, which requires two arrays of equal length for x and y coordinates:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()
```

### Customizing Scatter Plots

#### Colors
You can customize marker colors in multiple ways:
- Set a single color for all points
- Use a specific color for each point
- Apply a colormap for gradient coloring

```python
# Single color
plt.scatter(x, y, color='hotpink')

# Multiple colors
colors = np.array(["red", "green", "blue", "yellow"])
plt.scatter(x, y, c=colors)

# Colormap
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
plt.scatter(x, y, c=colors, cmap='viridis')
plt.colorbar()  # Add colorbar
```

### Comparing Multiple Datasets

You can plot multiple scatter plots on the same figure to compare datasets:

```python
# First dataset
x1 = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y1 = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# Second dataset
x2 = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y2 = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])

plt.scatter(x1, y1, color='blue')
plt.scatter(x2, y2, color='red')
plt.show()
```

### Key Concepts
- Scatter plots visualize relationships between two variables
- Use `scatter()` function with x and y arrays
- Highly customizable with colors, sizes, and markers
- Supports colormaps for gradient visualizations
- Multiple datasets can be compared on the same plot

---

## 11. Bar Charts

### Creating Bar Graphs

#### Vertical Bars
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y)
plt.show()
```

#### Horizontal Bars
```python
plt.barh(x, y)
plt.show()
```

### Bar Customization

#### Color Options
You can customize bar colors using:
- Color names: `plt.bar(x, y, color="red")`
- Hex values: `plt.bar(x, y, color="#4CAF50")`

#### Bar Width and Height
- Vertical bars: Use `width` parameter
  ```python
  plt.bar(x, y, width=0.1)  # Thin bars
  ```
- Horizontal bars: Use `height` parameter
  ```python
  plt.barh(x, y, height=0.1)  # Thin bars
  ```

### Key Concepts
- Default bar width/height is 0.8
- `bar()` function for vertical bars
- `barh()` function for horizontal bars
- Supports 140 color names and hex color values
- Easily customize bar appearance with color, width, and height parameters

### Example with Multiple Customizations
```python
x = np.array(["APPLES", "BANANAS"])
y = np.array([400, 350])
plt.bar(x, y, color="hotpink", width=0.5)
plt.show()
```

---

## 12. Histograms

### Key Concepts

A histogram is a graph that shows frequency distributions, specifically displaying the number of observations within each given interval.

#### Example Scenario
In a height distribution of 250 people, a histogram might show:
- 2 people between 140-145cm
- 5 people between 145-150cm
- 15 people between 151-156cm
- And so on...

### Creating a Histogram

#### Basic Implementation
To create a histogram in Matplotlib, use the `hist()` function:

```python
import matplotlib.pyplot as plt
import numpy as np

# Generate random data with normal distribution
x = np.random.normal(170, 10, 250)

# Create histogram
plt.hist(x)
plt.show()
```

#### Key Components
- `np.random.normal()` generates a random array
  - First parameter: mean (170)
  - Second parameter: standard deviation (10)
  - Third parameter: number of values (250)
- `plt.hist()` creates the histogram
- `plt.show()` displays the graph

### Important Notes
- Histograms visualize data distribution
- Useful for understanding frequency of values
- Can be created easily with NumPy and Matplotlib
- Helps in analyzing statistical data patterns

The example demonstrates creating a histogram from a normally distributed dataset, showing how data is spread across different intervals.

---

## 13. Pie Charts

### Basic Pie Chart Creation

Matplotlib allows you to create pie charts using the `pie()` function. Here's a basic example:

```python
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
plt.pie(y)
plt.show()
```

### Key Concepts

#### Wedge Sizing
- Wedge size is determined by comparing values
- Calculated using the formula: `x/sum(x)`
- Default start is at x-axis, moving counterclockwise

### Customization Options

#### Labels
Add labels to each wedge:
```python
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels=mylabels)
```

#### Start Angle
Change the starting position:
```python
plt.pie(y, startangle=90)
```

#### Explode
Highlight specific wedges:
```python
myexplode = [0.2, 0, 0, 0]  # Pulls out the first wedge
plt.pie(y, explode=myexplode)
```

#### Additional Styling
- Add shadow: `shadow=True`
- Custom colors: `colors=['black', 'hotpink', 'b', '#4CAF50']`

### Legend
Add a legend with or without a title:
```python
plt.pie(y, labels=mylabels)
plt.legend()  # Basic legend
plt.legend(title="Four Fruits:")  # Legend with title
```

### Color Options
Matplotlib supports:
- Hexadecimal color values
- 140 named colors
- Shortcut color codes:
  - 'r' - Red
  - 'g' - Green
  - 'b' - Blue
  - 'c' - Cyan
  - 'm' - Magenta
  - 'y' - Yellow
  - 'k' - Black
  - 'w' - White

---

## Summary

This comprehensive tutorial covers all the essential aspects of Matplotlib:

1. **Introduction & Setup** - Understanding what Matplotlib is and how to install it
2. **Basic Plotting** - Creating simple line plots with pyplot
3. **Customization** - Markers, line styles, colors, and labels
4. **Layout** - Grids and subplots for organized visualizations
5. **Chart Types** - Scatter plots, bar charts, histograms, and pie charts

With these foundational concepts, you can create professional data visualizations for analysis, presentations, and reports. Practice with different datasets and explore the extensive customization options to master Matplotlib!
