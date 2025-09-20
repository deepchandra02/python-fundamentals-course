# Module 9: Tuples & Constants
# Duration: 5 minutes | Time: 1:16-1:21

# 🔨 Live Coding - Calculator v2.3

# TODO: Create tuple of mathematical constants
MATH_CONSTANTS = ()  # π, e, √2
CONSTANT_NAMES = ()  # "Pi", "Euler's e", "√2"

# TODO: Display constants using zip
print("🔢 MATH CONSTANTS")
for i, (name, value) in enumerate(zip(CONSTANT_NAMES, MATH_CONSTANTS), 1):
    print(f"{i}. {name} = {value}")

# TODO: Create coordinate tuples
point1 = ()
point2 = ()
print(f"Distance calculation between {point1} and {point2}")

# Example: Returning multiple values using tuples
def get_circle_info(radius):
    # TODO: Calculate area and circumference
    area = 3.14159 * radius ** 2
    circumference = 2 * 3.14159 * radius
    return area, circumference  # Returns a tuple!

# TODO: Unpack the returned tuple
area, circumference = get_circle_info(5)
print(f"Circle: Area = {area}, Circumference = {circumference}")

# ⚡ Quick Exercise (1 min):
# 1. Add more mathematical constants
# 2. Create a tuple for your favorite numbers
# 3. Try changing a tuple value (what happens?)