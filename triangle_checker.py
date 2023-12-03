print("enter three sides of triangle")
side1=int(input("enter the length of first side: "))
side2=int(input("enter the length of first side: "))
side3=int(input("enter the length of first side: "))
if (side1==side2)& (side2==side3):
    print("this is equilateral triangle")
elif side1==side2 or side2==side3 or side3==side1:
    print("this is isocles triangle")
else:
    print("this is scalane triangle")