from turtle import *
P=eval(input("Enter the starting point:"))
s=int(input("Enter the number of sides:"))
l=int(input("Enter the side lenghts:"))
def polygon(s,l,P):
    a=360/s
    penup()
    goto(P)
    pendown()
    for i in range(0,s):
        forward(l)
        left(a)
polygon(s,l,P)
