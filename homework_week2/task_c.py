password=input("Plsase enter the password")
if len(password)>=8 and password.isalnum():
    print('Your password is valid')
else:
    print('Your password is not valid')
