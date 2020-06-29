print("Insert length of traingle :")
x=float(input("x :"))
y=float(input("y :"))
z=float(input("z :"))

if x==y==z:
    print("It is a Traingle ")
elif x==y or y==z or z==x:
    print(" It is a Isosceles Traingle ")
elif x!=y or y!=z or z!=x:
    print("It is a Scalene Traingle")