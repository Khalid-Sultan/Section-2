r=int(input("Enter the radius"))
n=36

import turtle
turtle.showturtle()

def color():
    import random
    color='#'
    for a in range (0,6):
        r = random.randint(0,14)
        if r>=10:
            color += chr(ord('a') + (r-10))
        else:
            color += str(r)
    return color

def circle(r):
    for i in range(0,n):
        turtle.begin_fill()
        turtle.circle(r)
        turtle.right(10)
        turtle.color(color())
        turtle.end_fill()
        turtle.speed(1000)
    turtle.right(10)
circle(r)
