n=int(input("enter the number"))
sum=0
temp=n
z=len(str(temp))
while temp>0:
    r=temp%10
    sum=sum+(r**z)
    temp=temp//10
if sum==n:
    print("it is armstrong number")
else:
    print("it is not armstrong number")


i=1
j=0
while i<=100:
    if i%2!=0 and i%3!=0 and  i%5!=0 and i%7!=0:
        print(i,"prime")
        j+=1
    if i==3 or i==5 or i==7:
        print(i,"prime")
    i+=1
if j==0:
    print("prime")

num=int(input("enter the number"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num,"it is not prime")
            break
        else:
            print(num,"it is prime")

num=int(input("enter the number"))
i=2
n=0
while i<=num/2:
    if num%i==0:
        n=1
        break
    i+=1
if n==0:
    print("prime")
else:
    print("not prime")
