i=1
a=1
while i<=4:
    j=1
    while j<=i:
        print(a,end=" ")
        a+=1
        j+=1
    i+=1
    print()


i=1
a=4
while i<=4:
    j=i+a
    while j>=i:
        print(a,end=" ")
        a+=1
        j-=1
    i+=1
    print()

