C=eval(input("enter the center point"))
P=eval(input("enter the point on the circumference"))
def distance(C,P):
    x=C[0]-P[0]
    y=C[1]-P[1]
    import math
    dis=math.sqrt(x**2+y**2)
    return dis
r=distance(C,P)
def area(r):
    A=(22*r*r)/7
    return A
print('the distance between the center and the point on the circle is',distance(C,P),'and the area of the circle is',area(r))
