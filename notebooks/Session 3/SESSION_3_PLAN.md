# Session 3: Data Handling & ML Workshop Plan

**Workshop Focus:** Introduction to Data Handling and Machine Learning in Python
**Format:** 100% Jupyter Notebooks with Interactive Learning
**Duration:** ~3-4 hours total

---

## Current Progress Assessment

### ✅ Completed:
1. **Reference Materials Extracted:**
   - **NumPy**: 16 individual tutorials + complete tutorial ✓
   - **Pandas**: 14 individual tutorials + complete tutorial ✓
   - **Matplotlib**: Complete tutorial compiled ✓

2. **Notebook Structure Started:**
   - Created `/notebooks/Session 3/` folder ✓
   - Created `00-setup-verification.ipynb` (installation checks) ✓
   - Created `datasets/` folder ✓

3. **Planning Documentation:**
   - This plan document saved for resumption ✓

---

## Workshop Design Philosophy

**Interactive Learning Pattern:**
Each notebook follows this structure for every concept:

1. **📚 Concept Introduction** (Markdown cell)
   - Clear explanation of the concept
   - Why it's important
   - Real-world use cases

2. **💡 Example Code** (Code cell - Pre-filled, runnable)
   - Complete working example demonstrating the concept
   - Well-commented code
   - Students run this to see output

3. **✏️ Your Turn - TODO Exercise** (Code cell - Partial code with TODOs)
   - Similar problem for students to solve
   - Strategic comments with `# TODO:` instructions
   - Students type code to complete the exercise
   - Builds muscle memory and understanding

4. **🎯 Expected Output** (Markdown cell - optional)
   - Shows what the completed TODO should produce
   - Helps students verify their work

---

## Notebooks to Create

### **00-setup-verification.ipynb** ✅ COMPLETED
- Verify NumPy, Pandas, Matplotlib, Scikit-learn installations
- Test basic functionality
- System information check

### **01-numpy-basics.ipynb** (~30-40 minutes)

**Topics with Example → TODO pattern:**

1. **Creating Arrays**
   - Example: Create array from list
   - TODO: Create arrays using arange(), zeros(), ones(), random()

2. **Array Indexing and Slicing**
   - Example: Access elements and slices
   - TODO: Extract specific rows, columns, ranges

3. **Array Operations**
   - Example: Mathematical operations
   - TODO: Perform calculations, aggregations (sum, mean, max)

4. **Reshaping Arrays**
   - Example: Reshape 1D to 2D
   - TODO: Reshape arrays to different dimensions

5. **Boolean Indexing and Filtering**
   - Example: Filter values > threshold
   - TODO: Create custom filters

**Learning Outcomes:**
- Understand NumPy arrays vs Python lists
- Perform vectorized operations
- Manipulate array shapes and dimensions
- Filter and select data efficiently

---

### **02-pandas-fundamentals.ipynb** (~40-50 minutes)

**Topics with Example → TODO pattern:**

1. **Series Creation and Manipulation**
   - Example: Create Series, access elements
   - TODO: Create Series with custom index, perform operations

2. **DataFrame Basics**
   - Example: Create DataFrame from dict
   - TODO: Create DataFrame, access rows/columns

3. **Reading Data (CSV/JSON)**
   - Example: Load sample CSV file
   - TODO: Load data and explore with head(), info(), describe()

4. **Data Selection and Filtering**
   - Example: Filter rows by condition
   - TODO: Multi-condition filtering, column selection

5. **Data Cleaning**
   - Example: Handle missing values
   - TODO: Clean dataset (drop nulls, fill values, fix types)

6. **Grouping and Aggregation**
   - Example: Group by category and aggregate
   - TODO: Perform complex groupby operations

**Learning Outcomes:**
- Create and manipulate Pandas data structures
- Load real-world data from files
- Clean and prepare data for analysis
- Perform aggregations and grouping operations

---

### **03-matplotlib-visualization.ipynb** (~40-50 minutes)

**Topics with Example → TODO pattern:**

1. **Basic Line Plots**
   - Example: Simple line plot
   - TODO: Create multi-line plot with styling

2. **Scatter Plots**
   - Example: Basic scatter
   - TODO: Colored scatter with size variation

3. **Bar Charts**
   - Example: Vertical bars
   - TODO: Horizontal bars, grouped bars

4. **Customization (Labels, Titles, Legends)**
   - Example: Fully labeled plot
   - TODO: Add professional styling to your plot

5. **Subplots**
   - Example: 2x2 subplot grid
   - TODO: Create custom dashboard layout

6. **Pie Charts and Histograms**
   - Example: Basic pie chart
   - TODO: Create histogram with customization

**Learning Outcomes:**
- Create various plot types for different data
- Customize visualizations professionally
- Build multi-panel dashboards
- Choose appropriate chart types for data

---

### **04-data-exploration.ipynb** (~30-40 minutes)

**End-to-end project combining all libraries**

**Structure:**
1. **Load Dataset**
   - Example: Load real dataset (CSV with interesting data)
   - TODO: Explore dataset structure and contents

2. **Data Cleaning**
   - Example: Complete cleaning workflow for one aspect
   - TODO Section 1: Students clean another portion of data

3. **Data Analysis**
   - Example: Perform statistical analysis
   - TODO Section 2: Students explore different columns/relationships

4. **Data Visualization**
   - Example: Create comprehensive visualization
   - TODO Section 3: Students create different charts

5. **Final Challenge**
   - Open-ended analysis question
   - Students apply all learned skills

**Learning Outcomes:**
- Execute complete data analysis workflow
- Integrate NumPy, Pandas, and Matplotlib
- Make data-driven insights
- Present findings visually

---

### **05-mnist-digit-recognition.ipynb** (~50-60 minutes)

**Step-by-step ML walkthrough with scaffolded learning**

**Structure:**

1. **Introduction to MNIST**
   - Markdown: What is MNIST? Why is it important?
   - Example: Load dataset, show structure
   - TODO: Display sample digits, check dimensions

2. **Data Exploration**
   - Markdown: Understanding the data
   - Example: Visualize first 10 digits in a grid
   - TODO: Create grid of random samples, analyze label distribution

3. **Data Preprocessing**
   - Markdown: Why preprocessing matters
   - Example: Normalize pixel values (0-255 to 0-1)
   - TODO: Reshape data for model, split train/test sets

4. **Model Training** (Using scikit-learn)
   - Markdown: Introduction to machine learning classifier
   - Example: Train basic model (e.g., Logistic Regression or Random Forest)
   - TODO: Adjust parameters, retrain, compare results

5. **Model Evaluation**
   - Markdown: Understanding model performance
   - Example: Calculate accuracy, show confusion matrix
   - TODO: Analyze per-digit accuracy, identify difficult digits

6. **Visualizing Results**
   - Markdown: Interpreting predictions
   - Example: Show correct vs incorrect predictions
   - TODO: Visualize misclassified digits, analyze patterns

7. **Interactive Testing**
   - Markdown: Testing the model
   - Example: Predict single digit with visualization
   - TODO: Test multiple predictions, create prediction dashboard

**Learning Outcomes:**
- Understand ML workflow from data to predictions
- Preprocess image data for machine learning
- Train and evaluate a classification model
- Interpret model predictions and errors
- Visualize ML results effectively

---

## TODO Cell Format

Each TODO cell follows this template:

```python
# ✏️ YOUR TURN: [Clear instruction of what to do]
#
# Task: [Specific task description]
# Hint: [Helpful tip if needed]
# Expected output: [Description of what result should look like]

# Your code here

```

**Progressive Difficulty Levels:**
- **Early TODOs**: Very guided, fill-in-the-blank style
- **Middle TODOs**: More independence, with hints
- **Later TODOs**: Open-ended, minimal guidance

---

## Dataset Requirements

Create/gather datasets for:

1. **02-pandas-fundamentals.ipynb**
   - `students_data.csv` - Student grades/demographics
   - `sales_data.csv` - Sales transactions

2. **04-data-exploration.ipynb**
   - `real_world_data.csv` - Rich dataset (e.g., Titanic, housing prices, or weather)

3. **05-mnist-digit-recognition.ipynb**
   - MNIST dataset (loaded via scikit-learn, no file needed)

---

## Implementation Checklist

### Phase 1: Core Learning Notebooks
- [ ] Create `01-numpy-basics.ipynb`
  - [ ] All concepts with Example + TODO pattern
  - [ ] Test all code cells execute correctly
  - [ ] Verify TODO exercises are appropriate difficulty

- [ ] Create `02-pandas-fundamentals.ipynb`
  - [ ] Prepare sample datasets
  - [ ] All concepts with Example + TODO pattern
  - [ ] Test all code cells execute correctly
  - [ ] Verify TODO exercises are appropriate difficulty

- [ ] Create `03-matplotlib-visualization.ipynb`
  - [ ] All concepts with Example + TODO pattern
  - [ ] Ensure visual outputs are clear
  - [ ] Test all code cells execute correctly
  - [ ] Verify TODO exercises are appropriate difficulty

### Phase 2: Integration Projects
- [ ] Create `04-data-exploration.ipynb`
  - [ ] Source/create rich dataset
  - [ ] Design end-to-end workflow
  - [ ] Create scaffolded TODO sections
  - [ ] Test complete workflow

- [ ] Create `05-mnist-digit-recognition.ipynb`
  - [ ] Structure complete ML pipeline
  - [ ] Create step-by-step walkthrough
  - [ ] Design visualization exercises
  - [ ] Test all model training/evaluation code

### Phase 3: Supporting Materials
- [ ] Create sample datasets in `datasets/` folder
- [ ] Add README.md in Session 3 folder with overview
- [ ] Optional: Create solutions notebook for instructors

---

## Success Criteria

Each notebook should:
- ✅ Run from top to bottom without errors (when TODOs are completed)
- ✅ Have clear markdown explanations before code
- ✅ Include working example code for every concept
- ✅ Provide TODO exercises that reinforce learning
- ✅ Produce visual outputs where appropriate
- ✅ Build progressively in difficulty
- ✅ Be completable in estimated time

---

## Notes for Resumption

**Current State:**
- All reference materials extracted and available in `resources/` folder
- Notebook structure created in `notebooks/Session 3/`
- Setup verification notebook completed
- Ready to create 5 main learning notebooks

**Next Steps:**
1. Start with `01-numpy-basics.ipynb`
2. Follow the Example → TODO pattern for each concept
3. Test thoroughly after each notebook creation
4. Gather/create necessary datasets
5. Create remaining notebooks in sequence

**Resources Available:**
- NumPy reference: `resources/numpy/`
- Pandas reference: `resources/pandas/`
- Matplotlib reference: `resources/matplotlib/`

---

*Plan created: 2025-10-19*
*Status: Ready for implementation*
