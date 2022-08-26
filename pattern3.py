i=1
while i<=5:
    j=1
    while j<=i:
        if i==2 or i==4:
            print("*",end=" ")
        else:
            print(j,end=" ")
        j+=1
    i+=1
    print()

n=5
i=1
while i<=n:
    j=1
    while j<=i:
        if i%2!=0:
            print(j,end=" ")
        else:
            print("*",end=" ")
        j+=1
    i=i+1
    print()
