n=int(input("enter the number"))
temp=n
sum=0
while n>0:
    dig=n%10
    j=1
    for i in range(1,dig+1):
        j=j*1
    sum=sum+j
    n=n//10
if temp==sum:
    print("strong")
else:
    print("weak")

num=int(input("enter the number"))
s=0
strong=num
while strong>0:
    f=1
    i=1
    r=strong%10
    while i<=r:
        f=f*i
        i=i+1
    s=s+f
    strong=strong//10
if s==num:
    print("strong number")
else:
    print("weak number")
