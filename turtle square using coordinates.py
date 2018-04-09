P=eval(input("Enter the x and y coordinate of the square = "))
l=eval(input("Enter the length of the square = "))
n=4
from turtle import *
showturtle()
def square(P,l,n):
    goto(P[0],P[1])
    for i in range (0,n):
        forward(l)
        right(90)
square(P,l,n)
