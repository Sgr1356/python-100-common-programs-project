import math
x =float(input("Insert point X :"))
y =float(input("Insert point Y :"))
r =float(input("Insert Radius R :"))

hypotenius = math.sqrt(pow(x,2)+pow(y,2))

if hypotenius<=r:
    print("Point belong to Circle")
else:
    print("it Doesnot belong to circle")