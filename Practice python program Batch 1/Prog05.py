
while True:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if num2 == 0:
        print("Division by zero is not possible")
        continue
    else:
        print(f"The Quotient of {num1} and {num2} is:", float(num1/num2))
        break

 