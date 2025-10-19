#!/usr/bin/env python3
"""
Create all Session 3 Jupyter notebooks
"""
import json
import os

OUTPUT_DIR = "/Users/deepc/MCP access Folder/python-fundamentals-course/notebooks/Session 3"

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

def md(text):
    """Create a markdown cell"""
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in text.split("\n")]
    }

def code(source):
    """Create a code cell"""
    return {
        "cell_type": "code",
        "execution_count": null,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in source.split("\n")]
    }

def save_nb(notebook, filename):
    """Save notebook to file"""
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, 'w') as f:
        json.dump(notebook, f, indent=2)
    print(f"✅ Created: {filename}")

# The notebooks will be created using this script
# Running it now...

print("📚 Creating Session 3 Jupyter Notebooks...")
print("="*60)
print("✅ 00-setup-verification.ipynb already created!")
print("Now creating remaining notebooks...")
print("="*60)
