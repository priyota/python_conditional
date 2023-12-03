import cmath
print("enter three coefficients of qudratic equation")
a=int(input("enter coefficient a: "))
b=int(input("enter coefficient b: "))
c=int(input("enter coefficient c: "))
d=(b**2)-(4*a*c)
sol1=(-b+cmath.sqrt(d))/(2*a)
sol2=(-b-cmath.sqrt(d))/(2*a)
print(sol1,sol2)