num=int(input("enter the number"))
temp=num
sum=0
rem=0
while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10
if temp%sum==0:
    print("harshad number")
else:
    print("not a harshad number")