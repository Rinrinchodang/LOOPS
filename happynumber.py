n=int(input("enter the number"))
h=n
while sum!=1 and sum!=4:
    sum=0
    while h!=0:
        rem=h%10
        sum=sum+rem*rem
        h=h//10
    h=sum
if sum==1:
    print("happy number")
else:
    print("sad number")

