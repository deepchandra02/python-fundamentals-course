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
