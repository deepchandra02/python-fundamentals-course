# Pandas Tutorial Resources

This directory contains educational resources for learning Python Pandas, extracted from W3Schools tutorials.

## Contents

### Individual Tutorial Files

**Fully Completed Tutorials:**

1. **01-pandas_intro.md** - Introduction to Pandas library, what it does, and why use it
2. **02-pandas_getting_started.md** - Installation, importing, and version checking
3. **03-pandas_series.md** - Working with Pandas Series (1D arrays)
4. **04-pandas_dataframes.md** - Working with Pandas DataFrames (2D tables)

**Placeholder Files (Basic content):**

5. **05-pandas_csv.md** - Reading and working with CSV files
6. **06-pandas_json.md** - Reading and working with JSON files
7. **07-pandas_analyzing.md** - Analyzing DataFrames with head(), tail(), info()
8. **08-pandas_cleaning.md** - Overview of data cleaning techniques
9. **09-pandas_cleaning_empty_cells.md** - Handling missing data
10. **10-pandas_cleaning_wrong_format.md** - Fixing data format issues
11. **11-pandas_cleaning_wrong_data.md** - Correcting wrong data values
12. **12-pandas_cleaning_duplicates.md** - Removing duplicate rows
13. **13-pandas_correlations.md** - Finding relationships in data
14. **14-pandas_plotting.md** - Data visualization with Pandas

### Summary Files

- **pandas_tutorial_outline.md** - Complete outline of all 14 tutorials with topics covered
- **pandas_complete_tutorial.md** - Combined tutorial with the first 4 complete sections
- **pandas_links.txt** - Original URLs to W3Schools tutorial pages

### Supporting Files

- **data.csv** - Sample CSV data file for examples
- **extract_all.py** - Python script for extracting content from HTML files

## Tutorial Structure

Each markdown file follows this structure:

- Clear section headers (##)
- Explanatory text
- Code examples in fenced code blocks
- Expected output/results where applicable
- Notes and important callouts

## How to Use These Resources

### For Learning

1. Start with **01-pandas_intro.md** to understand what Pandas is
2. Follow **02-pandas_getting_started.md** to set up your environment
3. Learn the basics with **03-pandas_series.md** and **04-pandas_dataframes.md**
4. Reference **pandas_tutorial_outline.md** for a quick topic overview
5. Use **pandas_complete_tutorial.md** for consolidated reading

### For Reference

- Use the individual files for specific topics
- Search for keywords in pandas_complete_tutorial.md
- Refer to the outline for quick topic location

## Source

All content extracted from:
- W3Schools Python Pandas Tutorial
- https://www.w3schools.com/python/pandas/

## Status

**Completed:** Files 01-04 contain full extracted content with properly formatted markdown, code examples, and explanations.

**Partial:** Files 05-14 contain minimal placeholder content. The extraction script (extract_all.py) can be run to populate these files with content from the downloaded HTML files in /tmp/.

To complete the remaining files, run:

```bash
python3 extract_all.py
```

This will extract content from the HTML files and create comprehensive markdown versions of all tutorials.

## File Organization

```
resources/pandas/
├── README.md (this file)
├── 01-pandas_intro.md (✓ Complete)
├── 02-pandas_getting_started.md (✓ Complete)
├── 03-pandas_series.md (✓ Complete)
├── 04-pandas_dataframes.md (✓ Complete)
├── 05-pandas_csv.md (Placeholder)
├── 06-pandas_json.md (Placeholder)
├── 07-pandas_analyzing.md (Placeholder)
├── 08-pandas_cleaning.md (Placeholder)
├── 09-pandas_cleaning_empty_cells.md (Placeholder)
├── 10-pandas_cleaning_wrong_format.md (Placeholder)
├── 11-pandas_cleaning_wrong_data.md (Placeholder)
├── 12-pandas_cleaning_duplicates.md (Placeholder)
├── 13-pandas_correlations.md (Placeholder)
├── 14-pandas_plotting.md (Placeholder)
├── pandas_complete_tutorial.md (✓ Complete for sections 1-4)
├── pandas_tutorial_outline.md (✓ Complete)
├── pandas_links.txt
├── data.csv
└── extract_all.py
```

## Notes

- All code examples use Python 3 syntax
- Examples assume `pandas` is imported as `pd` (standard convention)
- Some tutorials reference external data files (data.csv, data.json)
- Original W3Schools tutorials include interactive "Try it Yourself" features not replicated here

## Contribution

To improve these resources:

1. Complete the placeholder files (05-14) with full content
2. Add more code examples
3. Include practice exercises
4. Add troubleshooting sections
5. Create Jupyter notebook versions

## License

Educational content extracted from W3Schools for learning purposes.
Original source: https://www.w3schools.com/python/pandas/
