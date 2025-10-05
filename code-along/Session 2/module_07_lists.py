# Module 7: Lists & History
# 🔨 Live Coding - Calculator v2.1

# TODO: Create an empty list to store calculation history
history =

# TODO: Create function to add calculations to history
def add_to_history(calc_string):
    # Add the calculation to the history list


# TODO: Create function to show history
def show_history():
    print("\n📋 CALCULATION HISTORY")
    # TODO: Check if history has items
    if history:
        # TODO: Loop through history with numbers
        for i, calc in enumerate(history, 1):
            print(f"{i}. {calc}")
    else:
        print("No calculations yet!")

# Example usage (you'll integrate this into your main calculator):
# After doing a calculation:
num1, num2, op, result = 10, 5, "+", 15
calc_string = f"{num1} {op} {num2} = {result}"
add_to_history(calc_string)

# TODO: Call show_history to test it
show_history()

# ⚡ Quick Exercise:
# 1. Add more calculations to history
# 2. Add "3️⃣ Show History" option to your calculator menu
# 3. Think about how to clear history