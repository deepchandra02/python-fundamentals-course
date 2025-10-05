# Python JSON Tutorial

## Overview
JSON (JavaScript Object Notation) is a lightweight data interchange format used for storing and exchanging data in Python.

## Key Concepts

### JSON Module
Python has a built-in `json` module for working with JSON data:

```python
import json
```

### Converting JSON to Python
Use `json.loads()` to parse JSON into a Python dictionary:

```python
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])  # Outputs: 30
```

### Converting Python to JSON
Use `json.dumps()` to convert Python objects to JSON strings:

```python
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)
print(y)
```

## Convertible Python Types
The following Python types can be converted to JSON:
- dict → JSON Object
- list → JSON Array
- tuple → JSON Array
- string → JSON String
- int → JSON Number
- float → JSON Number
- True → JSON true
- False → JSON false
- None → JSON null

### Data Type Conversion Table

| Python | JSON |
|--------|------|
| dict | Object |
| list | Array |
| tuple | Array |
| str | String |
| int | Number |
| float | Number |
| True | true |
| False | false |
| None | null |

## JSON Methods

### `json.loads()` - Parse JSON String
Converts a JSON string into a Python object (dictionary):

```python
import json

json_string = '{"name": "Alice", "age": 25}'
python_dict = json.loads(json_string)
print(python_dict)  # {'name': 'Alice', 'age': 25}
print(type(python_dict))  # <class 'dict'>
```

### `json.dumps()` - Convert to JSON String
Converts a Python object into a JSON string:

```python
import json

python_dict = {"name": "Alice", "age": 25}
json_string = json.dumps(python_dict)
print(json_string)  # '{"name": "Alice", "age": 25}'
print(type(json_string))  # <class 'str'>
```

### `json.load()` - Read from File
Reads JSON data from a file:

```python
import json

with open('data.json', 'r') as file:
    data = json.load(file)
print(data)
```

### `json.dump()` - Write to File
Writes Python object to a file as JSON:

```python
import json

data = {"name": "Alice", "age": 25}
with open('data.json', 'w') as file:
    json.dump(data, file)
```

## Formatting JSON Output

### Add Indentation for Readability
```python
import json

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# Pretty-print with indentation
print(json.dumps(x, indent=4))
```

Output:
```json
{
    "name": "John",
    "age": 30,
    "city": "New York"
}
```

### Custom Separators
```python
# Custom separators (item_separator, key_separator)
print(json.dumps(x, indent=4, separators=(", ", ": ")))

# Different style
print(json.dumps(x, indent=4, separators=(". ", " = ")))
```

### Sort Keys Alphabetically
```python
print(json.dumps(x, indent=4, sort_keys=True))
```

## Complex JSON Example

### Working with Nested Data
```python
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "children": ("Ann", "Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# Convert to JSON
json_string = json.dumps(x, indent=2)
print(json_string)
```

Output:
```json
{
  "name": "John",
  "age": 30,
  "married": true,
  "children": [
    "Ann",
    "Billy"
  ],
  "pets": null,
  "cars": [
    {
      "model": "BMW 230",
      "mpg": 27.5
    },
    {
      "model": "Ford Edge",
      "mpg": 24.1
    }
  ]
}
```

## Common Use Cases

### API Data Exchange
```python
import json

# Simulating API response
api_response = '{"status": "success", "data": {"user_id": 123, "username": "alice"}}'
response_data = json.loads(api_response)
print(response_data["data"]["username"])  # alice
```

### Configuration Files
```python
import json

# Save configuration
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "username": "admin"
    },
    "debug_mode": True
}

with open('config.json', 'w') as f:
    json.dump(config, f, indent=4)

# Load configuration
with open('config.json', 'r') as f:
    loaded_config = json.load(f)
    print(loaded_config["database"]["host"])
```

### Data Serialization
```python
import json

# Save data to file
data = {
    "students": [
        {"name": "Alice", "grade": 90},
        {"name": "Bob", "grade": 85}
    ]
}

with open('students.json', 'w') as f:
    json.dump(data, f, indent=2)
```

## Error Handling

### JSONDecodeError
```python
import json

try:
    invalid_json = '{"name": "John", age: 30}'  # Missing quotes around age
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"Error parsing JSON: {e}")
```

## Best Practices

1. **Always use proper JSON formatting** - Use double quotes, not single quotes
2. **Handle errors** - Use try/except for JSON parsing
3. **Use indentation** - Makes JSON readable for debugging
4. **Validate data** - Check data types after parsing
5. **Close files properly** - Use context managers (`with` statement)
6. **Use appropriate methods**:
   - `loads()`/`dumps()` for strings
   - `load()`/`dump()` for files

## Key Takeaways

- ✅ **JSON is a text format** for data exchange
- ✅ **`json.loads()`** converts JSON string → Python dict
- ✅ **`json.dumps()`** converts Python dict → JSON string
- ✅ **`json.load()`** reads JSON from file
- ✅ **`json.dump()`** writes JSON to file
- ✅ **Formatting options** make JSON readable
- ✅ **Many Python types** convert to JSON automatically