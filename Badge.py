import turtle

turtle.pencolor('blue')
turtle.speed(90)
for i in range(190):
    turtle.forward(200)
    turtle.right(30)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(50)
    turtle.right(30)

    turtle.penup()
    turtle.setposition(0,0)
    turtle.pendown()

    turtle.right(2)

input()