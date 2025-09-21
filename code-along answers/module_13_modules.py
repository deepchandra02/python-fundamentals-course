# Module 13: Modules & Advanced Features
# Duration: 6 minutes | Time: 1:38-1:44

# 🔨 Live Coding - Calculator v4.0 FINAL

# TODO: Import the math module


# TODO: Create scientific operations function
def scientific_operations():
    print("🔬 SCIENTIFIC CALCULATOR")

    # TODO: Create operations dictionary with lambda functions
    operations = {
        "1": ("Square Root", lambda x: ),
        "2": ("Sine (degrees)", lambda x: ),
        "3": ("Natural Log", lambda x: ),
        "4": ("Power of e", lambda x: )
    }

    # TODO: Display options
    for key, (name, _) in operations.items():
        print(f"{key}. {name}")

    choice = input("Choose (1-4): ")
    if choice in operations:
        # TODO: Get number and calculate
        num = float(input("Enter number: "))
        name, func = operations[choice]
        result = func(num)
        print(f"✨ {name}({num}) = {result:.4f}")

# TODO: Create professional formatting function
def format_result(num1, op, num2, result):
    """Professional result formatting"""
    return f"📊 {num1:,.2f} {op} {num2:,.2f} = {result:,.2f}"

# TODO: Create BMI calculator
def calculate_bmi():
    print("💪 BMI CALCULATOR")
    # TODO: Get weight and height
    weight =
    height =

    # TODO: Calculate BMI
    bmi =

    print(f"BMI: {bmi:.1f}")

    # TODO: Add BMI categories
    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal weight")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")

# Test the functions
print("Testing scientific operations:")
scientific_operations()

print("\nTesting BMI calculator:")
calculate_bmi()

# ⚡ Quick Exercise (1 min):
# 1. Add cosine and tangent functions
# 2. Add more constants like math.pi and math.e
# 3. Create a temperature converter function