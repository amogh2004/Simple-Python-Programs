import turtle

turt=turtle.Turtle()
turt.speed(30)

def square(size,change,color):
    turt.color(color)
    turt.begin_fill()
    for i in range(4):
      turt.fd(size)
      turt.lt(90)
    turt.end_fill()
    turt.fd(size)

def row(size,change,c1,c2):
    for i in range(4):
        if(change==True):
            square(size,change,c1)
            square(size,change,c2)
        else:
            square(size,change,c2)
            square(size,change,c1)

def chessboard(size,change,c1,c2):
    turt.pu()
    turt.goto(-(size*4),(size*4))
    for i in range(8):
        row(size,change,c1,c2)
        turt.bk(size*8)
        turt.rt(90)
        turt.fd(size)
        turt.lt(90)
        if(change==True):
            change=False
        else:
            change=True

chessboard(50,True,'light blue','black')
            

turt.done()
