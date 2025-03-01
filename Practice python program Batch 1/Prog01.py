print("Enter 2 Numbers")

while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        if num1 > num2:
            print("The number", num1, "is greater than", num2)
        elif num1 < num2:
            print("The number", num2, "is greater than", num1)   
    except ValueError:
        print("Please enter a valid number")
        continue

    choice = input("Do you want to continue? (Y/N): ").strip()
    if choice == 'N' or choice == 'n':
        break
        


