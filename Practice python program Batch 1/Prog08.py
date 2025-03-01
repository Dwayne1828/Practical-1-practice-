odd_count = 0

for i in range (10): 
    num = int(input(f"Enter the {i+1} number: "))
    if num % 2 != 0:
        odd_count += 1
    
print(f"The count of odd numbers is: {odd_count}")
        

