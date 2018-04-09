r=int(input("Enter the radius"))
import turtle
def colored_circle(r):
    for i in range (0,36):
        import random
        n=random.randint(0,1000)
        color='#'
        color += str(n)
        turtle.color(color)
        turtle.circle(r)
        turtle.right(10)
colored_circle(r)


