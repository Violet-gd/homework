grade=int(input("What is your grade."))
if 100>=grade>=80:
    print("Your grade is A")
elif 79>=grade>=60:
    print("Your grade is B")
elif 59>=grade>=50:
    print("Your grade is C")
elif 49>=grade>=40:
    print("Your grade is D")
elif 0>=grade>=39:
    print("Your grade is F")
else:
    print("Error:Please enter a number")