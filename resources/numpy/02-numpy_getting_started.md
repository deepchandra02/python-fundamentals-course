# NumPy Getting Started


---


## Installation of NumPy

If you have Python and PIP already installed on a system, then installation of 
NumPy is very easy.

Install it using this command:

```python
C:\Users\
Your Name
>pip install numpy
```

```python
C:\Users\
Your Name
>pip install numpy
```

If this command fails, then use a python distribution that already has NumPy installed like, Anaconda, Spyder etc.


---


## Import NumPy

Once NumPy is installed, import it in your applications by adding the
import keyword:

```python
import numpy
```

```python
import numpy
```

Now NumPy is imported and ready to use.

```python
import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)
```


### Example

```python
import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)
```


---


## NumPy as np

NumPy is usually imported under the np 
alias.

alias: In Python alias are an alternate name for referring 
  to the same thing.

Create an alias with the as keyword while importing:

```python
import numpy as np
```

```python
import numpy as np
```

Now the NumPy package can be referred to as np instead of numpy.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
```


### Example

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
```


---


## Checking NumPy Version

The version string is stored under __version__ 
attribute.

```python
import numpy as np
print(np.__version__)
```


### Example

```python
import numpy as np
print(np.__version__)
```


---

