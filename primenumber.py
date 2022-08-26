# num=int(input("enter the number"))
# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             print(num ,"is not prime")
#             break
#         else:
#             print(num,"is prime")

a=int(input("enter the number"))
i=1
j=0
while i<=a:
    if a%i==0 and a%a==0:
        j+=1
    i+=1
if j==0:
    print("it is a prime")
else:
    print("it is not prime")


# i=1
# while i<=100:
#     if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 :
#         print(i,"prime")
#     if i==3 or i==5 or i==7:
#         print(i,"prime")
#     i+=1


