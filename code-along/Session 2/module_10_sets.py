# Module 10: Sets & Unique Operations
# 🔨 Live Coding - Calculator v2.4

# TODO: Create sets to track unique operations
operations_used =
available_operations =

# Simulate user performing operations
# TODO: Add operations to the set as user performs them
operation_name = "add"  # example


# TODO: Show what operations the user has tried
print(f"🎯 Operations you've tried: ")

# TODO: Show what operations they haven't tried yet
print(f"📝 Try these next: ")

# TODO: Check if user has tried everything
if len(operations_used) == len(available_operations):
    print("🏆 Calculator Master! You've tried everything!")

# Example: Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# TODO: Try different set operations
print(f"Union: {set1 | set2}")           # All items
print(f"Intersection: {set1 & set2}")    # Common items
print(f"Difference: {set1 - set2}")      # Items in set1 but not set2

# ⚡ Quick Exercise:
# 1. Track unique numbers used in calculations
# 2. What happens if you add the same operation twice?
# 3. Try set operations with your own sets