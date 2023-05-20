from turtle import *
from random import *
tracer(0)
global timer1
timer1 = 0
def disappear(x,y):
    global score1
    for ball in ballList:
        if (x - ball.xcor())**2 + (y - ball.ycor())**2 < 400:
        #if ball.xcor()-20<x< ball.xcor()+20 and ball.ycor()-20<y <ball.ycor()+20:
            ball.ht()
            ballList.remove(ball)
            score1 = score1 + 1
ballList = []
colormode(255)
for i in range(100):
    ball = Turtle()
    ball.penup()
    ball.shape("circle")
    ball.goto(randint(-200, 200), randint(-200, 200))
    ball.dx = randint(-2, 2)
    ball.dy = -1
    ball.onclick(disappear)
    ball.color(randint(0, 255), randint(0, 255), randint(0, 255))
    ballList.append(ball)


score1 = 0
score = Turtle()
score.penup()
score.goto(0, 220)
score.ht()
timer = Turtle()
timer.penup()
timer.goto(-300, 220)
timer.ht()
while True:
    update()
    timer1 = timer1+0.032
    score.clear()
    score.write("Score: " + str(score1), font = ("Arial", 30, "normal"))
    timer.clear()
    timer.write("Time Used: " +str(timer1), font = ("Arial", 10, "normal"))
    for ball in ballList:
        ball.sety(ball.ycor()+ball.dy*0.3)
        ball.setx(ball.xcor()+ball.dx*0.3)
        if ball.ycor()>200 or ball.ycor() <-200:
            ball.dy = -ball.dy
        if ball.xcor()>200 or ball.xcor()<-200:
            ball.dx = -ball.dx
        
