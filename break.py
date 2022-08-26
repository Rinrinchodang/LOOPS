num=int(input("enter the number"))
i=1
j=0
while i<=num%2:
    if num%i==0:
        j=1
        break
        i=i+1
if j==0:
    print("it is not prime")
else:
    print("it is prime")
