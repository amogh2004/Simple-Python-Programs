from turtle import *
x=100; n=5
angle = 360//n

for i in range (n):
    forward(x) ; left(angle)

penup(); forward(x); forward(x); pendown()


for i in range(n):
    forward(x); left(angle)

penup(); forward(x); forward(x); pendown()

for i in range(n):
    forward(x);left(angle)

penup(); forward(x); forward(x); pendown()

input()