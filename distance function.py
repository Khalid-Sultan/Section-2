P=eval(input("enter point P"))
Q=eval(input("enter point Q"))
def distance(P,Q):
    x=P[0]-Q[0]
    y=P[1]-Q[1]
    import math
    dis=math.sqrt(x**2+y**2)
    return dis
print('the distance between P and Q is',distance(P,Q))
