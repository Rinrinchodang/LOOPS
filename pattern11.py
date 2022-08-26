from tkinter.font import names


n=int(input("enter the number"))
i=n
while i>=0:
    j=0
    a=i+1
    while j<=i:
        print(a,end=" ")
        a+=1
        j+=1
    i-=1
    print()