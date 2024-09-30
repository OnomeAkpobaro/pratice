def calculator():
    while True:
        print("Options: 1. Add  2. Subtract  3. Multiply  4. Divide  5. Exit")
        choice = input("Choose an option: ")
        if choice =='5':
            print("Exiting calculator.")
            break

        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))

        if choice == '1':
            print(f"Result: {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1 * num2}")
        elif choice == '4':
            if num2 == 0:
                print("Cannot divide by zero!")
            else:
                print(f"Result: {num1 / num2}")
        else:
            print("Invalid choice")

calculator()
    
            
