n=int(input("enter no="))
i=0
a=1
while i<=n:
    j=1
    while j<=5:
        print(chr(64+a),end=" ")
        a+=1
        j+=1
    i+=1
    print()

i=65
a=65
while i<=70:
    j=65
    while j<=i:
        print(chr(a),end=" ")
        a+=1
        j+=1
    i+=1
    print()