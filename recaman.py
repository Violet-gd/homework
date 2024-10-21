k=int(input("The length of the sequence"))
a=[0]*k
for i in range(1,k):
    if a[i-1]-i>0 and not(a[i-1]-i in a):
        a[i]=a[i-1]-i
    else:
        a[i]=a[i-1]+i

print(f"The first {k} numbers in the sequence are: {a}")