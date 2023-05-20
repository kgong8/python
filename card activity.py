from turtle import *
from random import *
from time import *

bgcolor("hotpink")
tracer(0)
def drawHeart(x,y,c,r):
    penup()
    goto(x,y)
    pendown()
    color(c)
    begin_fill()
    setheading(90)
    circle(r, 180)
    setheading(90)
    circle(r, 180)
    setheading(-60)
    forward(4*r)
    setheading(60)
    forward(4*r)
    end_fill()

while True:
    update()
    clear()
    for i in range(50):
        x = randint(-500, 500)
        y = randint(-300, 300)
        c = [random() for i in range(3)]
        r= randint(10,30)
        drawHeart(x,y,c,r)
    penup()
    goto(0,0)
    write("Happy Mother's Day!", align='center', font=('Arial', 40, 'italic bold'))
    ht()
    sleep(1)
    
