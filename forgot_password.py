def forgot_password(username, password):
                    username = input("Enter your username:").lower()
                    password = input("Enter your password:").lower()
                    
while True:
    choice = ("\n1. Sign up"  "2. Login"  "3. Forgot Password") 
    if choice == '1':
        sign_updetails = ("\n1. {username} " "\n2. {password}")
        print(f"{sign_updetails}")  

    elif choice == '2':
            print(f"{sign_updetails}")


    


