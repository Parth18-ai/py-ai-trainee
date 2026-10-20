import day7

while True:
    print("\nCalculator Menu")
    print("Press 1 for Addition")
    print("Press 2 for Subtraction")
    print("Press 3 for Division")
    print("Press 4 for Multiplication")
    print("Press 5 for Exit")

    choice = int(input("Enter your Choice: "))

    if choice == 5:
        print("Goodbye!")
        break

    if choice not in (1, 2, 3, 4):
        print("Invalid choice, please try again.")
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        result = day7.cal_Add(a, b)
    elif choice == 2:
        result = day7.cal_Subtract(a, b)
    elif choice == 3:
        result = day7.cal_Divide(a, b)
    elif choice == 4:
        result = day7.cal_Multiply(a, b)

    print("Result:", result)