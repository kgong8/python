from turtle import*

#circle(radius, extent)
#circle(100): a full circle
#Circle(100, 180): semicircle
R = 20
speed(0)
for i in range((int)(360/R)):
    begin_fill()
    if i%2 == 0:
        fillcolor("black")
    else:
        fillcolor("red")
    circle(200,R)
    left(90)
    forward(200)
    left(180-R)
    forward(200)
    left(90)
    end_fill()
    circle(200, R)

pensize(10)
pencolor("black")
circle(200)
goto(0,100)
pencolor("purple")
circle(100)
penup()
goto(0,200)
dot(10,"red")
