l=eval(input("Enter the length of the square: "))
n=eval(input("Enter the number of sides: "))
from turtle import *
showturtle()
def square(l):
    for i in range (0,n):
        forward(l)
        right(360/n)
for i in range(0,360,10):
    square(l)
    right(10)
