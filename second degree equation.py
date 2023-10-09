import math
A=float(input("type the values of A"))
B=float(input("type the values of B"))
C=float(input("type the values of C"))
D = (-B**2)-4*A*C
if D < 0 :
    print("NO REAL SOLUTION")
elif D == 0 :
    X = (-B)/(2*A)
    print("THE SOLUTION IS:"+ X)
else :
    X1 = (-B + math.sqrt(D))/(2*A)
    X2 = (-B - math.sqrt(D))/(2*A)
    print("THE SOLUTIONS ARE:", X1 ,"ET", X2)
