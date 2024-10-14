password=input("Plsase enter the password")
if len(password)>=8 and password.isalnum():
    if password.isdigit():
        print("Your password must contain at least 8 characters, and a mix of letters and numbers")
    else:
        print('Your password is valid')
else:
    print("Your password must contain at least 8 characters, and a mix of letters and numbers")
