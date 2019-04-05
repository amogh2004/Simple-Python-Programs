from turtle import *
x=100; n=4

def polygon(n,x):
    angle=360//n
    for i in range(n):
        forward(x); left(angle)
    penup(); forward(x); pendown()

polygon(4,50)
polygon(5,60)
polygon(4,50)