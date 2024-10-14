a=input("What the is it today").capitalize()

num={"Monday":1,"Tuseday":2,"Wendesday":3,"Thursday":4,"Friday":5,"Saturday":6,"Sunday":7}
if a in num.keys():
    print(f"{a} is the day {num[a]}")
else:
    print("Please enter a valid day")