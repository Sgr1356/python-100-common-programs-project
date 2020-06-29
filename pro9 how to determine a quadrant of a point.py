x= float(input("insert quardinates of X point :"))
y= float(input("insert quardinates of Y point :"))

if x==0 and y==0:
    print("Your Quadrant is in Origin from both side")
elif x>0 and y>0:
    print("Your Point is in 1st Quadrant and both are Positive")
elif x<0 and y>0:
    print("Your Point is in 2nd Quadrant and x is Negative and y is Positive")
elif x<0 and y<0:
    print("Your Point is in 3rd  Quadrant and both are Negative")
elif x>0 and y<0:
    print("Your Point is in 4th Quadrant and x is Positive and y is Negative")
