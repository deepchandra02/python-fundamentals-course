# Module 15: Working with JSON
# JSON (JavaScript Object Notation) - Data Interchange Format

"""
Learning Objectives:
- Understand what JSON is and why it's used
- Convert Python objects to JSON (serialization)
- Parse JSON strings to Python objects (deserialization)
- Read and write JSON files
- Format JSON output for readability
"""

import json

# ==========================================
# PART 1: JSON BASICS
# ==========================================

print("=" * 60)
print("PART 1: Understanding JSON")
print("=" * 60)

# JSON is a text-based format for data exchange
# It looks similar to Python dictionaries but has slight differences:
# - JSON uses true/false (lowercase)
# - Python uses True/False (capitalized)
# - JSON uses null
# - Python uses None

# TODO 1.1: Create a Python dictionary representing a person
person = {
    # Add your data here
}

print("\nPython dictionary:")
print(person)

# ==========================================
# PART 2: CONVERTING PYTHON TO JSON
# ==========================================

print("\n" + "=" * 60)
print("PART 2: Python to JSON (json.dumps)")
print("=" * 60)

# json.dumps() converts Python object to JSON string
# dumps = "dump string"

# TODO 2.1: Convert the person dictionary to a JSON string
json_string = json.dumps(person)
print("\nJSON string:")
print(json_string)
print(f"Type: {type(json_string)}")

# TODO 2.2: Pretty print with indentation
pretty_json = json.dumps(person, indent=4)
print("\nPretty JSON (with indentation):")
print(pretty_json)

# TODO 2.3: Try sorting the keys alphabetically
sorted_json = json.dumps(person, indent=4, sort_keys=True)
print("\nSorted JSON:")
print(sorted_json)

# ==========================================
# PART 3: PARSING JSON TO PYTHON
# ==========================================

print("\n" + "=" * 60)
print("PART 3: JSON to Python (json.loads)")
print("=" * 60)

# json.loads() converts JSON string to Python object
# loads = "load string"

# TODO 3.1: Parse this JSON string
user_json = '{"username": "alice123", "email": "alice@example.com", "age": 25}'
user_data = json.loads(user_json)

print("\nParsed data:")
print(user_data)
print(f"Type: {type(user_data)}")

# TODO 3.2: Access individual values
print(f"\nUsername: {user_data['username']}")
print(f"Email: {user_data['email']}")
print(f"Age: {user_data['age']}")

# ==========================================
# PART 4: PYTHON TO JSON TYPE CONVERSION
# ==========================================

print("\n" + "=" * 60)
print("PART 4: Type Conversions")
print("=" * 60)

# Different Python types convert to JSON differently

# TODO 4.1: Create a dictionary with various data types
data_types_demo = {
    "string": "Hello",
    "integer": 42,
    "float": 3.14,
    "boolean_true": True,
    "boolean_false": False,
    "none_value": None,
    "list": [1, 2, 3],
    "tuple": (4, 5, 6),
    "nested_dict": {"key": "value"}
}

# TODO 4.2: Convert to JSON and see how types change
converted = json.dumps(data_types_demo, indent=2)
print("\nPython types converted to JSON:")
print(converted)

# Notice:
# - True → true
# - False → false
# - None → null
# - tuple → array (same as list)

# ==========================================
# PART 5: WORKING WITH FILES
# ==========================================

print("\n" + "=" * 60)
print("PART 5: Reading and Writing JSON Files")
print("=" * 60)

# TODO 5.1: Create a student record
student = {
    "student_id": 12345,
    "name": "Emma Watson",
    "major": "Computer Science",
    "year": 3,
    "gpa": 3.8,
    "courses": ["Python Programming", "Data Structures", "Algorithms"],
    "graduated": False
}

# TODO 5.2: Write to a JSON file
filename = "student_record.json"
with open(filename, 'w') as file:
    json.dump(student, file, indent=4)  # dump (no 's') for files

print(f"\n✅ Student record saved to {filename}")

# TODO 5.3: Read from the JSON file
with open(filename, 'r') as file:
    loaded_student = json.load(file)  # load (no 's') for files

print("\n📖 Loaded student record:")
print(json.dumps(loaded_student, indent=2))

# ==========================================
# PART 6: ERROR HANDLING
# ==========================================

print("\n" + "=" * 60)
print("PART 6: Handling JSON Errors")
print("=" * 60)

# TODO 6.1: Try parsing invalid JSON
invalid_json = '{"name": "Alice", age: 25}'  # age should be in quotes

try:
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"\n❌ JSON Error: {e}")
    print("Tip: JSON keys must be in double quotes!")

# TODO 6.2: Parse valid JSON
valid_json = '{"name": "Alice", "age": 25}'
try:
    data = json.loads(valid_json)
    print(f"\n✅ Successfully parsed: {data}")
except json.JSONDecodeError as e:
    print(f"Error: {e}")

# ==========================================
# EXERCISE 1: CONTACT BOOK
# ==========================================

print("\n" + "=" * 60)
print("EXERCISE 1: Contact Book")
print("=" * 60)

# TODO: Create a contact book with at least 3 contacts
contacts = {
    "contacts": [
        # Add your contacts here
        # Each contact should have: name, phone, email, address
    ]
}

# TODO: Save contacts to a file


# TODO: Load contacts from the file


# TODO: Print all contact names


# ==========================================
# EXERCISE 2: APP CONFIGURATION
# ==========================================

print("\n" + "=" * 60)
print("EXERCISE 2: Application Configuration")
print("=" * 60)

# TODO: Create an app configuration
app_config = {
    "app_name": "",
    "version": "",
    "settings": {
        # Add settings: theme, language, notifications, etc.
    },
    "features": {
        # Add feature flags: dark_mode, auto_save, etc.
    }
}

# TODO: Save to config.json


# TODO: Load and display specific settings


# ==========================================
# EXERCISE 3: API RESPONSE SIMULATION
# ==========================================

print("\n" + "=" * 60)
print("EXERCISE 3: Simulating API Response")
print("=" * 60)

# TODO: Simulate a weather API response
weather_api_response = '''
{
    "location": "New York",
    "temperature": 72,
    "condition": "Partly Cloudy",
    "humidity": 65,
    "wind_speed": 10,
    "forecast": [
        {"day": "Monday", "high": 75, "low": 60},
        {"day": "Tuesday", "high": 78, "low": 62},
        {"day": "Wednesday", "high": 72, "low": 58}
    ]
}
'''

# TODO: Parse the API response


# TODO: Extract and display weather information


# TODO: Display the forecast


# ==========================================
# EXERCISE 4: DATA ANALYSIS
# ==========================================

print("\n" + "=" * 60)
print("EXERCISE 4: Student Grades Analysis")
print("=" * 60)

# TODO: Create a class roster with student grades
classroom = {
    "class_name": "Python 101",
    "teacher": "Dr. Smith",
    "students": [
        # Add at least 5 students with grades
        # {"name": "Alice", "grades": [90, 85, 92], "attendance": 95}
    ]
}

# TODO: Save to classroom.json


# TODO: Load the data


# TODO: Calculate class statistics
# - Average grade per student
# - Class average
# - Highest and lowest grades
# - Students with perfect attendance


# ==========================================
# ADVANCED CHALLENGE
# ==========================================

print("\n" + "=" * 60)
print("ADVANCED CHALLENGE: Custom JSON Encoder")
print("=" * 60)

# Challenge: Create a program that:
# 1. Manages a product inventory (name, price, quantity, category)
# 2. Saves inventory to JSON file
# 3. Loads inventory and displays it
# 4. Calculates total inventory value
# 5. Finds products below a certain stock level
# 6. Supports adding new products and updating quantities

# TODO: Implement the inventory management system


# ==========================================
# KEY TAKEAWAYS
# ==========================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)

print("""
✅ JSON Module Methods:
   - json.loads(string)  → Parse JSON string to Python
   - json.dumps(object)  → Convert Python to JSON string
   - json.load(file)     → Read JSON from file
   - json.dump(obj, file)→ Write JSON to file

✅ Common Formatting Options:
   - indent=4           → Pretty print with indentation
   - sort_keys=True     → Sort keys alphabetically
   - separators=(", ", ": ") → Custom separators

✅ Type Conversions:
   - dict   → JSON Object
   - list   → JSON Array
   - str    → JSON String
   - int    → JSON Number
   - float  → JSON Number
   - True   → JSON true
   - False  → JSON false
   - None   → JSON null

✅ Best Practices:
   - Always use 'with' statement for files
   - Handle JSONDecodeError exceptions
   - Use double quotes in JSON strings
   - Validate JSON before parsing
   - Use indentation for readable output

✅ Common Use Cases:
   - Configuration files
   - API data exchange
   - Data serialization
   - Web applications
   - Data storage
""")

print("\n🎉 Great job! You now know how to work with JSON in Python!")
print("Practice by creating config files, parsing API responses, and storing data!")
