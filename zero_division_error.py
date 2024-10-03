try:
    first_num = int(input("Enter the first number"))
    second_num = int(input("Enter the second number"))
    
    divide_operation = first_num / second_num

except ZeroDivisionError:
    
    print("Cannot divide by zero")
