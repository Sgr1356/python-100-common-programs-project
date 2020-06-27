x=int(input("Enter 1st number"))
y=int(input("Enter 2nd number"))
z=int(input("Enter 3rd number"))

print("The maximum number is : " ,end="")

if(y<=x>=z):
    print(x)
elif(x<=y>=z):
    print(y)
elif(x<=z>=y):
    print(z)