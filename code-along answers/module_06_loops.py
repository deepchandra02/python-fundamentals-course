# Module 6: Loop Power
# 🔨 Live Coding - Calculator v2.0

print("🧮 Never-Ending Calculator v2.0")

# TODO: Create an infinite loop
while True:
    # TODO: Display menu
    print("\n🎯 CALCULATOR MENU")
    print("1️⃣ Basic Math")
    print("2️⃣ Exit")

    # TODO: Get user choice
    choice = input("Choose (1-2): ")

    # TODO: Handle menu choices
    if choice == "2":
        print("👋 Thanks for calculating!")
        break
    elif choice == "1":
        # TODO 6.4: Get numbers and operation
        num1 = float(input("First number: "))
        op = input("Operation (+,-,*,/): ")
        num2 = float(input("Second number: "))

        # TODO 6.5: Calculate based on operation
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2 if num2 != 0 else "Error!"

        print(f"✅ Result: {result}")
    else:
        print("❌ Invalid choice!")

# ⚡ Quick Exercise:
# Add a "3️⃣ Power Operations" option to the menu
