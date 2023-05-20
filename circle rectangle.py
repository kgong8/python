from turtle import*
R = 10
bgcolor("black")
#turtle = Turtle()
speed(0)
for i in range((int)(360/R)):
    pencolor("yellow")
    pensize(2)
    forward(200)
    left(90)
    forward(400)
    left(90)
    forward(400)
    left(90)
    forward(400)
    left(90)
    forward(200)
    begin_fill()
    fillcolor("black")
    circle(200,R)
    left(90)
    forward(200)
    left(180-R)
    forward(200)
    left(90)
    end_fill()
    circle(200, R)
    
#https://repl.it/@easyfuncoding/Homework28Part2#main.py


               


