for col in range(7):
    for row in range(5):
        if ((row==0 or row==4 )and col!=0 )or ((col==0 or col ==3 )and(row>0 and row<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
 

for col in range(7):
    for row in range(5):
        if (row==0 )or (row==4 and col!=0 and col!=3 and col!=6) or ((col==0 or col==3 or col==6)and(row>0 and row<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()

for col in range(7):
    for row in range(5):
        if ((row==0 and col!=0 and col!=6)or(col==0 or col==6)and (row>0 and row<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()



































