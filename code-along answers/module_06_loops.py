# Module 6: Loop Power
# Duration: 8 minutes | Time: 0:55-1:03

# 🔨 Live Coding - Calculator v2.0

print("🧮 Never-Ending Calculator v2.0")

# TODO: Create an infinite loop
while True:
    # TODO: Display menu
    print("\n🎯 CALCULATOR MENU")
    print("1️⃣ Basic Math")
    print("2️⃣ Exit")

    # TODO: Get user choice
    choice =

    # TODO: Handle menu choices
    if choice == "2":
        print("👋 Thanks for calculating!")
        # TODO: Break out of the loop

    elif choice == "1":
        # TODO: Get numbers and operation
        num1 =
        op =
        num2 =

        # TODO: Calculate result based on operation
        if op == "+":
            result =
        elif op == "-":
            result =
        elif op == "*":
            result =
        elif op == "/":
            result = num1 / num2 if num2 != 0 else "Error!"

        print(f"✅ Result: {result}")
    else:
        print("❌ Invalid choice!")

# ⚡ Quick Exercise (2 min):
# Add a "3️⃣ Power Operations" option to the menu