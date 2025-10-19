# Matplotlib Tutorial Outline
## Comprehensive Data Visualization Workshop

---

## Course Overview

**Duration:** 120 minutes
**Level:** Beginner to Intermediate
**Prerequisites:** Basic Python knowledge, familiarity with lists and loops
**Project:** Build a complete Data Dashboard with multiple visualization types

---

## Learning Objectives

By the end of this tutorial, participants will be able to:
- Install and configure Matplotlib for data visualization
- Create and customize line plots, scatter plots, bar charts, histograms, and pie charts
- Apply professional styling with colors, markers, labels, and legends
- Organize multiple visualizations using subplots
- Build a complete data dashboard project
- Apply best practices for data visualization

---

## Workshop Structure

### Session Format
- **Theory & Demonstration:** 40%
- **Live Coding:** 35%
- **Hands-on Exercises:** 25%

### Project-Based Learning
Students will build a **Personal Data Dashboard** that visualizes:
- Daily activity tracker (line plot)
- Exercise intensity comparison (scatter plot)
- Weekly workout types (bar chart)
- Step count distribution (histogram)
- Activity time allocation (pie chart)
- Complete multi-panel dashboard (subplots)

---

## Detailed Module Breakdown

### Module 1: Introduction & Setup (10 minutes)
**Objective:** Understand Matplotlib and prepare the development environment

#### Topics:
- What is Matplotlib?
- History and ecosystem (NumPy, Pandas, SciPy)
- Installation and verification
- First visualization: "Hello World" plot

#### Project Step:
Create your first plot showing daily steps over a week

#### Code Exercise:
```python
import matplotlib.pyplot as plt
import numpy as np

# Your first visualization
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
steps = [8000, 9500, 7200, 10500, 11200, 6800, 9200]

plt.plot(days, steps)
plt.show()
```

#### Key Takeaways:
- Matplotlib is the foundation for Python data visualization
- Always import as `plt` for consistency
- `plt.show()` displays your visualization

---

### Module 2: Pyplot Basics & Line Plots (15 minutes)
**Objective:** Master basic plotting with pyplot interface

#### Topics:
- Understanding pyplot module
- Creating simple line plots
- Working with NumPy arrays
- Plotting multiple lines
- Default behaviors and shortcuts

#### Project Step:
Visualize steps, calories, and distance over time

#### Code Exercise:
```python
import matplotlib.pyplot as plt
import numpy as np

# Multi-metric tracking
days = np.array([1, 2, 3, 4, 5, 6, 7])
steps = np.array([8000, 9500, 7200, 10500, 11200, 6800, 9200])
calories = np.array([2100, 2300, 2000, 2500, 2600, 1900, 2200])

# Plot multiple lines
plt.plot(days, steps, label='Steps')
plt.plot(days, calories, label='Calories')
plt.legend()
plt.show()
```

#### Key Takeaways:
- NumPy arrays are preferred for numerical data
- Multiple plots can be overlaid
- Always label multiple lines for clarity

---

### Module 3: Customization - Markers & Lines (12 minutes)
**Objective:** Enhance visualizations with markers and line styles

#### Topics:
- Marker types and usage
- Marker size and color customization
- Line styles (solid, dashed, dotted, dashdot)
- Line width and colors
- Format string notation

#### Project Step:
Enhance your activity tracker with professional styling

#### Code Exercise:
```python
import matplotlib.pyplot as plt
import numpy as np

days = np.array([1, 2, 3, 4, 5, 6, 7])
steps = np.array([8000, 9500, 7200, 10500, 11200, 6800, 9200])

# Styled plot
plt.plot(days, steps,
         marker='o',           # Circle markers
         markersize=10,        # Larger markers
         linestyle='--',       # Dashed line
         color='#FF6B6B',      # Custom hex color
         linewidth=2)          # Thicker line

plt.show()
```

#### Key Takeaways:
- Markers emphasize data points
- Line styles convey different data types
- Color choice affects readability

---

### Module 4: Labels, Titles & Legends (10 minutes)
**Objective:** Add context and professionalism to visualizations

#### Topics:
- Adding axis labels with `xlabel()` and `ylabel()`
- Creating titles with `title()`
- Font customization with `fontdict`
- Title positioning
- Creating and positioning legends
- Best practices for text elements

#### Project Step:
Add complete labeling to your activity dashboard

#### Code Exercise:
```python
import matplotlib.pyplot as plt
import numpy as np

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
steps = [8000, 9500, 7200, 10500, 11200, 6800, 9200]
goal = [10000] * 7

# Custom fonts
title_font = {'family': 'serif', 'color': 'darkblue', 'size': 18, 'weight': 'bold'}
label_font = {'family': 'serif', 'color': 'darkred', 'size': 12}

plt.plot(days, steps, marker='o', label='Actual Steps')
plt.plot(days, goal, linestyle='--', color='green', label='Goal')

plt.title('Weekly Step Tracker', fontdict=title_font, loc='center')
plt.xlabel('Day of Week', fontdict=label_font)
plt.ylabel('Steps', fontdict=label_font)
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)

plt.show()
```

#### Key Takeaways:
- Labels provide essential context
- Consistent font styling looks professional
- Legends explain multiple data series

---

### Module 5: Grid & Layout Enhancement (8 minutes)
**Objective:** Improve plot readability with grids

#### Topics:
- Adding grid lines with `grid()`
- Axis-specific grids (x, y, or both)
- Grid customization (color, style, width)
- When to use grids effectively
- Best practices for clean layouts

#### Project Step:
Add professional grid lines to activity plots

#### Code Exercise:
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y, marker='o', linewidth=2, color='#3498db')

plt.title('Heart Rate vs Calories Burned')
plt.xlabel('Average Heart Rate (bpm)')
plt.ylabel('Calories Burned')

# Professional grid
plt.grid(axis='both', color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

plt.show()
```

#### Key Takeaways:
- Grids help users read exact values
- Subtle grids (low alpha) don't distract
- Consider grid necessity for each visualization

---

### Module 6: Subplots & Multi-Panel Layouts (15 minutes)
**Objective:** Create professional multi-panel dashboards

#### Topics:
- Understanding `subplot()` function
- Row and column layouts
- Subplot indexing
- Individual subplot customization
- Super titles with `suptitle()`
- Dashboard design principles

#### Project Step:
Create a complete 2x2 activity dashboard

#### Code Exercise:
```python
import matplotlib.pyplot as plt
import numpy as np

# Data preparation
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
steps = [8000, 9500, 7200, 10500, 11200, 6800, 9200]
calories = [2100, 2300, 2000, 2500, 2600, 1900, 2200]
distance = [5.2, 6.1, 4.8, 6.8, 7.2, 4.5, 5.9]
active_minutes = [45, 52, 38, 58, 62, 35, 48]

# Create 2x2 dashboard
plt.figure(figsize=(12, 10))

# Plot 1: Steps
plt.subplot(2, 2, 1)
plt.plot(days, steps, marker='o', color='#3498db')
plt.title('Daily Steps')
plt.ylabel('Steps')
plt.grid(True, alpha=0.3)

# Plot 2: Calories
plt.subplot(2, 2, 2)
plt.bar(days, calories, color='#e74c3c')
plt.title('Calories Burned')
plt.ylabel('Calories')

# Plot 3: Distance
plt.subplot(2, 2, 3)
plt.plot(days, distance, marker='s', linestyle='--', color='#2ecc71')
plt.title('Distance Covered')
plt.xlabel('Day')
plt.ylabel('Kilometers')
plt.grid(True, alpha=0.3)

# Plot 4: Active Minutes
plt.subplot(2, 2, 4)
plt.bar(days, active_minutes, color='#f39c12')
plt.title('Active Minutes')
plt.xlabel('Day')
plt.ylabel('Minutes')

# Overall title
plt.suptitle('Weekly Fitness Dashboard', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```

#### Key Takeaways:
- Subplots enable comprehensive data stories
- Consistent styling across panels looks professional
- `tight_layout()` prevents overlap

---

### Module 7: Scatter Plots (12 minutes)
**Objective:** Visualize relationships between variables

#### Topics:
- Creating scatter plots with `scatter()`
- Point customization (size, color, alpha)
- Using colormaps for third dimensions
- Adding colorbars
- Comparing multiple datasets
- Correlation visualization

#### Project Step:
Analyze relationship between workout intensity and calories

#### Code Exercise:
```python
import matplotlib.pyplot as plt
import numpy as np

# Workout data
workout_duration = np.array([30, 45, 25, 60, 50, 35, 55, 40, 65, 48])
calories_burned = np.array([250, 380, 200, 520, 420, 280, 480, 340, 580, 410])
heart_rate_avg = np.array([120, 145, 110, 165, 155, 125, 160, 135, 170, 150])

# Color-coded scatter plot
plt.scatter(workout_duration, calories_burned,
            s=heart_rate_avg*2,       # Size based on heart rate
            c=heart_rate_avg,          # Color based on heart rate
            cmap='YlOrRd',             # Yellow to Red colormap
            alpha=0.6,                 # Transparency
            edgecolors='black')

plt.colorbar(label='Avg Heart Rate (bpm)')
plt.title('Workout Duration vs Calories Burned')
plt.xlabel('Duration (minutes)')
plt.ylabel('Calories Burned')
plt.grid(True, alpha=0.3)

plt.show()
```

#### Key Takeaways:
- Scatter plots reveal relationships
- Size and color can encode additional data
- Colormaps add professional visual appeal

---

### Module 8: Bar Charts (12 minutes)
**Objective:** Compare categorical data effectively

#### Topics:
- Vertical bars with `bar()`
- Horizontal bars with `barh()`
- Bar customization (width, height, color)
- Grouped bar charts
- Stacked bar charts
- Best practices for bar chart design

#### Project Step:
Compare weekly workout types and intensity

#### Code Exercise:
```python
import matplotlib.pyplot as plt
import numpy as np

# Weekly workout breakdown
activities = ['Running', 'Cycling', 'Swimming', 'Yoga', 'Strength']
time_spent = [120, 90, 60, 75, 105]  # minutes
calories = [980, 720, 540, 300, 650]

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Vertical bar chart
colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6']
ax1.bar(activities, time_spent, color=colors, width=0.6)
ax1.set_title('Time Spent per Activity', fontsize=14, fontweight='bold')
ax1.set_ylabel('Minutes')
ax1.grid(axis='y', alpha=0.3)

# Horizontal bar chart
ax2.barh(activities, calories, color=colors, height=0.6)
ax2.set_title('Calories Burned per Activity', fontsize=14, fontweight='bold')
ax2.set_xlabel('Calories')
ax2.grid(axis='x', alpha=0.3)

plt.tight_layout()
plt.show()
```

#### Key Takeaways:
- Bar charts excel at categorical comparisons
- Color coding enhances readability
- Horizontal bars work well for long labels

---

### Module 9: Histograms (10 minutes)
**Objective:** Understand and visualize data distributions

#### Topics:
- What are histograms?
- Creating histograms with `hist()`
- Bin customization
- Frequency vs density plots
- Multiple histograms for comparison
- Distribution analysis

#### Project Step:
Analyze step count distribution patterns

#### Code Exercise:
```python
import matplotlib.pyplot as plt
import numpy as np

# Generate realistic step count data (30 days)
np.random.seed(42)
steps_data = np.random.normal(9000, 2000, 30)  # Mean: 9000, SD: 2000

plt.figure(figsize=(10, 6))

# Create histogram
plt.hist(steps_data, bins=10, color='#3498db', edgecolor='black', alpha=0.7)

# Add reference lines
plt.axvline(steps_data.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {steps_data.mean():.0f}')
plt.axvline(10000, color='green', linestyle='--', linewidth=2, label='Goal: 10000')

plt.title('30-Day Step Count Distribution', fontsize=16, fontweight='bold')
plt.xlabel('Steps per Day')
plt.ylabel('Frequency (Number of Days)')
plt.legend()
plt.grid(axis='y', alpha=0.3)

plt.show()
```

#### Key Takeaways:
- Histograms show data distribution patterns
- Bin size affects visualization interpretation
- Reference lines add valuable context

---

### Module 10: Pie Charts (10 minutes)
**Objective:** Show proportions and composition

#### Topics:
- Creating pie charts with `pie()`
- Labels and legends
- Exploding slices for emphasis
- Start angle customization
- Color schemes
- When to use (and not use) pie charts

#### Project Step:
Visualize daily time allocation across activities

#### Code Exercise:
```python
import matplotlib.pyplot as plt
import numpy as np

# Daily activity breakdown (hours)
activities = ['Sleep', 'Work', 'Exercise', 'Meals', 'Leisure', 'Other']
hours = [8, 9, 1.5, 2, 2.5, 1]
colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6', '#95a5a6']
explode = (0, 0, 0.1, 0, 0, 0)  # Emphasize exercise

plt.figure(figsize=(10, 8))

plt.pie(hours,
        labels=activities,
        colors=colors,
        explode=explode,
        autopct='%1.1f%%',
        startangle=90,
        shadow=True)

plt.title('Daily Time Allocation', fontsize=16, fontweight='bold')
plt.axis('equal')  # Equal aspect ratio ensures circular pie

plt.show()
```

#### Key Takeaways:
- Pie charts show parts of a whole
- Best for 5-7 categories maximum
- Exploding emphasizes key segments
- Percentages aid interpretation

---

### Module 11: Advanced Styling & Best Practices (8 minutes)
**Objective:** Create publication-quality visualizations

#### Topics:
- Color theory for data visualization
- Consistent styling with style sheets
- Figure size and DPI settings
- Saving visualizations (PNG, PDF, SVG)
- Accessibility considerations
- Common mistakes to avoid

#### Project Step:
Apply professional styling to final dashboard

#### Code Exercise:
```python
import matplotlib.pyplot as plt
import numpy as np

# Use professional style
plt.style.use('seaborn-v0_8-darkgrid')

# High-quality figure
fig, ax = plt.subplots(figsize=(12, 6), dpi=100)

days = np.array([1, 2, 3, 4, 5, 6, 7])
steps = np.array([8000, 9500, 7200, 10500, 11200, 6800, 9200])
goal = np.array([10000] * 7)

ax.plot(days, steps, marker='o', linewidth=3, markersize=10, label='Actual', color='#3498db')
ax.plot(days, goal, linestyle='--', linewidth=2, label='Goal', color='#2ecc71')
ax.fill_between(days, steps, goal, where=(steps < goal), alpha=0.3, color='red', label='Below Goal')

ax.set_title('Weekly Step Analysis', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Day', fontsize=14)
ax.set_ylabel('Steps', fontsize=14)
ax.legend(fontsize=12, loc='upper right')
ax.grid(True, alpha=0.3)

plt.tight_layout()

# Save high-quality version
plt.savefig('weekly_steps.png', dpi=300, bbox_inches='tight')
plt.show()
```

#### Key Takeaways:
- Consistent styling builds professionalism
- Save in appropriate format for use case
- Consider colorblind-friendly palettes
- Less is often more in visualization

---

### Module 12: Final Project - Complete Dashboard (10 minutes)
**Objective:** Integrate all concepts into a comprehensive project

#### Project Requirements:
Build a complete Personal Fitness Dashboard featuring:
1. Line plot: Weekly step trends
2. Scatter plot: Exercise intensity vs calories
3. Bar chart: Workout type comparison
4. Histogram: Step count distribution
5. Pie chart: Daily activity allocation
6. Professional styling and labels throughout

#### Deliverable:
A 2x3 subplot dashboard with:
- Consistent color scheme
- Professional labels and titles
- Appropriate visualization types for each metric
- Clean, readable layout
- High-quality export ready for sharing

#### Success Criteria:
- All six visualization types implemented
- Data tells a coherent story
- Professional appearance suitable for presentation
- Code is clean and well-commented

---

## Workshop Materials

### Prerequisites Checklist
- [ ] Python 3.7+ installed
- [ ] Matplotlib installed (`pip install matplotlib`)
- [ ] NumPy installed (`pip install numpy`)
- [ ] IDE or text editor ready
- [ ] Sample datasets downloaded

### Resources Provided
- Complete code examples for each module
- Sample datasets (CSV files)
- Cheat sheet for common Matplotlib functions
- Color palette reference guide
- Troubleshooting guide

### Post-Workshop Resources
- Extended documentation links
- Practice exercises with solutions
- Advanced topics guide (Seaborn, Plotly)
- Community resources and forums
- Next steps learning path

---

## Learning Outcomes Assessment

### Knowledge Checks
- Quiz after each major module
- Hands-on coding challenges
- Peer code review sessions

### Final Project Evaluation Criteria
1. **Technical Implementation (40%)**
   - Correct use of Matplotlib functions
   - Appropriate visualization choices
   - Code quality and organization

2. **Visual Design (30%)**
   - Professional appearance
   - Effective use of color
   - Clear labels and legends

3. **Data Storytelling (30%)**
   - Coherent narrative
   - Appropriate insights
   - Effective communication

---

## Instructor Notes

### Timing Adjustments
- **Fast Track:** Combine modules 3-4 for experienced learners
- **Extended:** Add 15-minute break after module 6
- **Flexible:** Modules 8-10 can be reordered based on interest

### Common Student Challenges
1. **NumPy array confusion** - Extra examples provided
2. **Subplot indexing** - Visual diagram in slides
3. **Color specification** - Color picker tool recommended
4. **Figure sizing** - DPI explanation often needed

### Engagement Strategies
- Live polling for visualization preferences
- Peer review of dashboard designs
- Real-world data visualization examples
- Q&A after each module

---

## Extensions & Advanced Topics

### For Students Who Finish Early
1. **Interactive Plots** with matplotlib widgets
2. **Animation** with FuncAnimation
3. **3D Plotting** with mplot3d
4. **Seaborn Integration** for statistical plots
5. **Custom Style Sheets** creation

### Next Course Recommendations
- Advanced Matplotlib (3D, animations, interactive)
- Seaborn for statistical visualization
- Plotly for interactive web dashboards
- Data Analysis with Pandas
- Machine Learning visualization techniques

---

## Summary

This comprehensive Matplotlib tutorial takes students from installation to creating professional multi-panel dashboards. Through hands-on, project-based learning, participants build practical skills while creating a complete personal fitness dashboard. The modular structure allows for flexible delivery while ensuring thorough coverage of all essential Matplotlib features.

**Key Success Factors:**
- Project-based approach maintains engagement
- Progressive complexity builds confidence
- Real-world examples aid retention
- Hands-on practice solidifies learning
- Professional output motivates completion
