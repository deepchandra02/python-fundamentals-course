---
marp: true
---

# Working with JSON in Python 📄

## Data Interchange Made Easy

**JSON (JavaScript Object Notation)**

---

## What is JSON? 🤔

**JSON** is a lightweight, text-based data format for storing and exchanging data:

- **Human-readable** - Easy to read and write
- **Language-independent** - Works with any programming language
- **Widely used** - APIs, config files, data storage
- **Simple structure** - Objects and arrays

### Why Use JSON?

- ✅ **Web APIs** - Most APIs return JSON
- ✅ **Configuration files** - Store app settings
- ✅ **Data exchange** - Share data between programs
- ✅ **Data storage** - Lightweight alternative to databases

---

## JSON vs Python Syntax 🔄

### JSON Format

```json
{
  "name": "Alice",
  "age": 25,
  "active": true,
  "skills": ["Python", "JavaScript"],
  "address": null
}
```

### Python Dictionary

```python
{
  "name": "Alice",
  "age": 25,
  "active": True,
  "skills": ["Python", "JavaScript"],
  "address": None
}
```

**Notice the differences**: `true` vs `True`, `null` vs `None`

---

## The JSON Module 📦

### Importing JSON

```python
import json
```

### Four Essential Methods

| Method         | Purpose                                 | Use Case      |
| -------------- | --------------------------------------- | ------------- |
| `json.loads()` | Parse JSON **string** → Python object   | API responses |
| `json.dumps()` | Convert Python object → JSON **string** | Sending data  |
| `json.load()`  | Read JSON from **file** → Python object | Config files  |
| `json.dump()`  | Write Python object → JSON **file**     | Save data     |

**Remember**: `s` = string, no `s` = file

---

## Parsing JSON Strings 📥

### `json.loads()` - String to Python

```python
import json

# JSON string (notice double quotes!)
json_string = '{"name": "Alice", "age": 25, "city": "NYC"}'

# Parse to Python dictionary
data = json.loads(json_string)

print(data)              # {'name': 'Alice', 'age': 25, 'city': 'NYC'}
print(type(data))        # <class 'dict'>
print(data["name"])      # Alice
print(data["age"])       # 25
```

---

### Key Points

- ✅ **Input is a string** with JSON format
- ✅ **Output is a Python dict** (or list for arrays)
- ✅ **Use double quotes** in JSON strings

---

## Creating JSON Strings 📤

### `json.dumps()` - Python to String

```python
import json

# Python dictionary
user = {
    "name": "Bob",
    "age": 30,
    "email": "bob@example.com",
    "active": True
}

# Convert to JSON string
json_string = json.dumps(user)

print(json_string)
# {"name": "Bob", "age": 30, "email": "bob@example.com", "active": true}
```

---

## Pretty Printing JSON ✨

### Basic Formatting with `indent`

```python
import json

user = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "JavaScript", "SQL"]
}

# Pretty print with 4-space indentation
print(json.dumps(user, indent=4))
```

---

**Output:**

```json
{
  "name": "Alice",
  "age": 25,
  "skills": ["Python", "JavaScript", "SQL"]
}
```

---

## Advanced Formatting Options 🎨

### Sort Keys Alphabetically

```python
data = {"name": "Alice", "age": 25, "city": "NYC"}

# Sort keys alphabetically
print(json.dumps(data, indent=2, sort_keys=True))
```

**Output:**

```json
{
  "age": 25,
  "city": "NYC",
  "name": "Alice"
}
```

---

### Custom Separators

```python
# Default separators
print(json.dumps(data, indent=2))

# Custom separators (item_separator, key_separator)
print(json.dumps(data, indent=2, separators=(", ", ": ")))

# Creative separators
print(json.dumps(data, indent=2, separators=("; ", " = ")))
```

**Output:**

```json
{
  "name" = "Alice";
  "age" = 25;
  "city" = "NYC"
}
```

---

## Reading JSON from Files 📂

### `json.load()` - Read File

```python
import json

# Read JSON file
with open('user_data.json', 'r') as file:
    data = json.load(file)  # No 's' - reads from file

print(data)
print(data["name"])
```

**Example File: `user_data.json`**

```json
{
  "name": "Alice",
  "age": 25,
  "city": "New York"
}
```

---

### Why Use `with` Statement?

- ✅ **Auto-closes file** even if error occurs
- ✅ **Best practice** for file operations
- ✅ **Prevents resource leaks**

---

## Writing JSON to Files 💾

### `json.dump()` - Write File

```python
import json

# Python data
user_profile = {
    "username": "alice123",
    "email": "alice@example.com",
    "settings": {
        "theme": "dark",
        "notifications": True
    }
}
# Write to JSON file
with open('profile.json', 'w') as file:
    json.dump(user_profile, file, indent=4)

print("Data saved to profile.json!")
```

---

## Working with Complex JSON 🏗️

### Nested Structures

```python
import json
company_data = {
    "company": "Tech Corp",
    "employees": [
        {
            "name": "Alice",
            "position": "Developer",
            "skills": ["Python", "JavaScript"]
        },
        {
            "name": "Bob",
            "position": "Designer",
            "skills": ["Photoshop", "Illustrator"]
        }
    ],
    "founded": 2020,
    "active": True
}
# Convert and save
json_output = json.dumps(company_data, indent=2)
print(json_output)
```

---

### Accessing Nested Data

```python
import json

json_string = '''
{
  "user": {
    "name": "Alice",
    "contact": {
      "email": "alice@example.com",
      "phone": "123-456-7890"
    }
  }
}
'''

data = json.loads(json_string)

# Access nested values
print(data["user"]["name"])                    # Alice
print(data["user"]["contact"]["email"])        # alice@example.com
print(data["user"]["contact"]["phone"])        # 123-456-7890
```

---

## Real-World Example: Config File ⚙️

### Saving Configuration

```python
import json

# Application configuration
config = {
    "app_name": "My Python App",
    "version": "1.0.0",
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp_db"
    }
}

# Save to config file
with open('config.json', 'w') as f:
    json.dump(config, f, indent=4)
```

---

### Loading Configuration

```python
import json

# Load configuration
with open('config.json', 'r') as f:
    config = json.load(f)

# Use configuration values
app_name = config["app_name"]
db_host = config["database"]["host"]

print(f"Starting {app_name}")
print(f"Connecting to database at {db_host}")
```

---

## Error Handling 🚨

### JSONDecodeError

```python
import json

# Invalid JSON (missing quotes around key)
invalid_json = '{"name": "Alice", age: 25}'

try:
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"❌ Error parsing JSON: {e}")
    print("Check your JSON syntax!")
```

---

### Common JSON Errors

- ❌ **Single quotes** instead of double quotes
- ❌ **Trailing commas** in arrays or objects
- ❌ **Missing quotes** around keys
- ❌ **Invalid escape sequences**
- ❌ **Undefined values** (use `null`)

---

## Practical Example: Student Records 📚

### Complete Workflow

```python
import json

# Create student records
students = {
    "class": "Python 101",
    "students": [
        {"id": 1, "name": "Alice", "grade": 95},
        {"id": 2, "name": "Bob", "grade": 87},
        {"id": 3, "name": "Charlie", "grade": 92}
    ],
    "semester": "Fall 2024"
}

# Save to file
with open('students.json', 'w') as f:
    json.dump(students, f, indent=2)

# Later: Load from file
with open('students.json', 'r') as f:
    loaded_data = json.load(f)

# Calculate average grade
grades = [student["grade"] for student in loaded_data["students"]]
average = sum(grades) / len(grades)
print(f"Average grade: {average:.1f}")
```

---

## API Integration Example 🌐

### Simulating API Response

```python
import json

# Simulated API response (would come from requests.get())
api_response = '''
{
  "status": "success",
  "data": {
    "weather": {
      "temperature": 72,
      "condition": "sunny",
      "humidity": 45
    },
    "location": "New York"
  }
}
'''

# Parse the response
response = json.loads(api_response)

# Extract data
status = response["status"]
temp = response["data"]["weather"]["temperature"]
condition = response["data"]["weather"]["condition"]
location = response["data"]["location"]

print(f"{location}: {temp}°F and {condition}")
```

---

## JSON Best Practices 💎

### Do's ✅

- ✅ **Use `with` statements** for file operations
- ✅ **Handle errors** with try/except
- ✅ **Use indentation** for readable output
- ✅ **Validate JSON** before parsing
- ✅ **Use double quotes** for JSON strings
- ✅ **Close files properly**

---

## JSON Best Practices 💎

### Don'ts ❌

- ❌ **Don't use single quotes** in JSON
- ❌ **Don't forget to import json** module
- ❌ **Don't mix up loads/load** and dumps/dump
- ❌ **Don't leave files unclosed**
- ❌ **Don't ignore JSONDecodeError**

---

## Quick Reference Card 📋

```python
import json

# STRING operations (with 's')
json.loads(json_string)    # Parse JSON string → Python
json.dumps(python_obj)      # Convert Python → JSON string

# FILE operations (no 's')
json.load(file_object)      # Read JSON file → Python
json.dump(python_obj, file) # Write Python → JSON file

# Formatting options
json.dumps(data, indent=4)              # Pretty print
json.dumps(data, sort_keys=True)        # Sort alphabetically
json.dumps(data, separators=(", ", ": ")) # Custom separators
```

---

## Key Takeaways 📚

### What You Learned

- ✅ **JSON is a text format** for data exchange
- ✅ **`json.loads()`** - Parse JSON string to Python
- ✅ **`json.dumps()`** - Convert Python to JSON string
- ✅ **`json.load()`** - Read JSON from file
- ✅ **`json.dump()`** - Write JSON to file
- ✅ **Formatting options** make output readable
- ✅ **Error handling** prevents crashes
- ✅ **Common in APIs** and config files

### Next Steps

- Practice with real API data
- Create configuration files for your apps
- Store and retrieve complex data structures

**JSON makes data exchange simple and universal! 🌍**
