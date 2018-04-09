def color():
    import random
    color='#'
    for j in range(0,6):
        n=random.randint(14,50)
        if r>= 10:
            color+=chr(ord('a') + (n-10))
        else:
            color+=str(n)
    return color
r=eval(input("Enter the radius of the square = "))
import turtle
t=turtle.Turtle()
t.circle(r)
def circle(r):
    for i in range(0,360,10):
        turtle.color()
        right(10)
circle(r)
