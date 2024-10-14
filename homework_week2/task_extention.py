password=input("Plsase enter the password")
values=0
if len(password)>=8 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password):
    if len(password)>=12:
        for i in password:
            if not(90>=ord(i)>=65 and 122>=ord(i)>=97 and 57>=ord(i)>=48):
                values+=1            
    if values>0:
        print("strong")
    else:
        print("Moderate")    
else:
    print("weak")
