i=10
a=1
while i<=50:
    j=a
    while j<=i:
        if j%2!=0:
            print(a,end=" ")
        a+=1
        j+=1
    i+=10
    print()