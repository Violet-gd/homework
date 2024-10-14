grade=input("Please enter a number")
if grade.isalpha():
    print("Error: Please enter a number")
elif 100>=int(grade)>=80:
    print("Your grade is: A")
elif 79>=int(grade)>=60:
    print("Your grade is: B")
elif 59>=int(grade)>=50:
    print("Your grade is: C")
elif 49>=int(grade)>=40:
    print("Your grade is: D")
elif 39>=int(grade)>=0:
    print("Your grade is: F")
elif int(grade)>100 or int(grade)<0:
    print("Error: Grades must be between 0 and 100")
else:
    print("Error: Please enter a number")