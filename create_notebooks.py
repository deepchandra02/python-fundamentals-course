#!/usr/bin/env python3
"""
Script to create Jupyter notebooks for Session 3
"""
import json
import os

def create_notebook(cells):
    """Create a Jupyter notebook structure"""
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
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
    return notebook

def markdown_cell(text):
    """Create a markdown cell"""
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": text.split('\n')
    }

def code_cell(code, outputs=None):
    """Create a code cell"""
    cell = {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "source": code.split('\n'),
        "outputs": outputs or []
    }
    return cell

def save_notebook(notebook, filepath):
    """Save notebook to file"""
    with open(filepath, 'w') as f:
        json.dump(notebook, f, indent=2)
    print(f"✅ Created: {filepath}")

# ====================
# 00 - Setup Verification Notebook
# ====================
def create_setup_verification():
    cells = [
        markdown_cell("""# 🔧 Setup Verification - Session 3
## Python Fundamentals Workshop: Data Science & ML

Welcome to Session 3! Before we begin, let's verify that all required libraries are installed and working correctly.

This notebook will check:
- ✅ NumPy - For numerical computing
- ✅ Pandas - For data manipulation
- ✅ Matplotlib - For visualization
- ✅ Scikit-learn - For machine learning

**Expected time:** 2 minutes"""),

        markdown_cell("""---
## 📦 Step 1: Import Libraries

Let's try importing all the libraries we'll need today."""),

        code_cell("""print("🔍 Checking library installations...\\n")

try:
    import numpy as np
    print("✅ NumPy imported successfully!")
    print(f"   Version: {np.__version__}")
except ImportError as e:
    print("❌ NumPy not found!")
    print(f"   Error: {e}")
    print("   Install with: pip install numpy")

try:
    import pandas as pd
    print("\\n✅ Pandas imported successfully!")
    print(f"   Version: {pd.__version__}")
except ImportError as e:
    print("\\n❌ Pandas not found!")
    print(f"   Error: {e}")
    print("   Install with: pip install pandas")

try:
    import matplotlib.pyplot as plt
    import matplotlib
    print("\\n✅ Matplotlib imported successfully!")
    print(f"   Version: {matplotlib.__version__}")
except ImportError as e:
    print("\\n❌ Matplotlib not found!")
    print(f"   Error: {e}")
    print("   Install with: pip install matplotlib")

try:
    import sklearn
    print("\\n✅ Scikit-learn imported successfully!")
    print(f"   Version: {sklearn.__version__}")
except ImportError as e:
    print("\\n❌ Scikit-learn not found!")
    print(f"   Error: {e}")
    print("   Install with: pip install scikit-learn")

print("\\n" + "="*50)
print("🎉 If you see all checkmarks above, you're ready to go!")
print("="*50)"""),

        markdown_cell("""---
## 🧪 Step 2: Quick Functionality Test

Let's test each library with a simple operation to make sure everything works!"""),

        markdown_cell("""### NumPy Test - Create an array and do math"""),

        code_cell("""import numpy as np

# Create a simple array
numbers = np.array([1, 2, 3, 4, 5])
print("Original array:", numbers)
print("Multiplied by 2:", numbers * 2)
print("Sum:", numbers.sum())
print("\\n✅ NumPy is working perfectly!")"""),

        markdown_cell("""### Pandas Test - Create a simple DataFrame"""),

        code_cell("""import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 95]
}
df = pd.DataFrame(data)
print(df)
print("\\n✅ Pandas is working perfectly!")"""),

        markdown_cell("""### Matplotlib Test - Create a simple plot"""),

        code_cell("""import matplotlib.pyplot as plt
import numpy as np

# Create a simple line plot
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

plt.figure(figsize=(8, 4))
plt.plot(x, y, marker='o', color='blue', linewidth=2)
plt.title('Test Plot - If you see this, Matplotlib works!', fontsize=14, fontweight='bold')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True, alpha=0.3)
plt.show()

print("✅ Matplotlib is working perfectly!")"""),

        markdown_cell("""### Scikit-learn Test - Load a sample dataset"""),

        code_cell("""from sklearn.datasets import load_iris

# Load the famous Iris dataset
iris = load_iris()
print(f"Dataset loaded: {iris.data.shape[0]} samples")
print(f"Features: {iris.feature_names[:2]}... (and more)")
print(f"Target classes: {len(iris.target_names)}")
print("\\n✅ Scikit-learn is working perfectly!")"""),

        markdown_cell("""---
## 🎊 Step 3: Final System Check"""),

        code_cell("""import sys
import platform

print("="*60)
print("🖥️  SYSTEM INFORMATION")
print("="*60)
print(f"Python Version: {sys.version.split()[0]}")
print(f"Platform: {platform.system()} {platform.release()}")
print(f"Architecture: {platform.machine()}")
print("="*60)
print()
print("="*60)
print("📚 INSTALLED LIBRARIES")
print("="*60)

libraries = [
    ('NumPy', 'numpy'),
    ('Pandas', 'pandas'),
    ('Matplotlib', 'matplotlib'),
    ('Scikit-learn', 'sklearn')
]

all_good = True
for name, module_name in libraries:
    try:
        module = __import__(module_name)
        version = getattr(module, '__version__', 'Unknown')
        print(f"✅ {name:15s} v{version}")
    except ImportError:
        print(f"❌ {name:15s} NOT INSTALLED")
        all_good = False

print("="*60)
print()

if all_good:
    print("🎉 " * 15)
    print("    ALL SYSTEMS GO! YOU'RE READY FOR SESSION 3!")
    print("🎉 " * 15)
else:
    print("⚠️  Some libraries are missing. Please install them before continuing.")
    print("   Run: pip install numpy pandas matplotlib scikit-learn")"""),

        markdown_cell("""---
## 🚀 You're All Set!

If all tests passed, you're ready to dive into:
- 📊 **Module 1**: NumPy Basics
- 📈 **Module 2**: Pandas Fundamentals
- 🎨 **Module 3**: Matplotlib Visualization
- 🔍 **Module 4**: Data Exploration
- 🤖 **Module 5**: MNIST Digit Recognition (ML Project!)

**Next**: Open `01-numpy-basics.ipynb` to start learning!

---

### 🆘 Troubleshooting

If you encountered any errors:

1. **Libraries not found?**
   ```bash
   pip install numpy pandas matplotlib scikit-learn
   ```

2. **Old Python version?**
   - Make sure you're using Python 3.7 or higher
   - Check with: `python --version`

3. **Still having issues?**
   - Try creating a new virtual environment
   - Ask your instructor for help!

---

*Session 3 - Data Handling & Machine Learning* 🐍""")
    ]

    notebook = create_notebook(cells)
    return notebook

# Create and save the notebook
if __name__ == "__main__":
    output_dir = "/Users/deepc/MCP access Folder/python-fundamentals-course/notebooks/Session 3"

    print("Creating Session 3 notebooks...\n")

    # Create 00-setup-verification.ipynb
    setup_nb = create_setup_verification()
    save_notebook(setup_nb, os.path.join(output_dir, "00-setup-verification.ipynb"))

    print("\n✨ Notebook creation complete!")
