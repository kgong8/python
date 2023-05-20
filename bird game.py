from turtle import *
from random import *
pipes = []

def checkOverlap(R,Xc, Yc, X1, Y1, X2, Y2):
    Xn = max(X1, min(Xc, X2)) 
    Yn = max(Y1, min(Yc, Y2))
    Dx=Xn-Xc
    Dy=Yn-Yc
    return (Dx**2+Dy**2)<R**2
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
bird = point(0,0)
def goLeft():
    bird.x -=30
    if bird.x <= -400:
        bird.x = -400
def goRight():
    bird.x +=30
    if bird.x >= 400:
        bird.x = 400
def goUp():
    bird.y +=30
    if bird.y >= 200:
        bird.y = 200
def rect(x,y):
    color("green")
    begin_fill()
    if y >=0:
        forward(50)
        left(90)
        forward(200-y)
        left(90)
        forward(50)
        left(90)
        forward(200-y)
        left(90)
    else:
        forward(50)
        right(90)
        forward(200-abs(y))
        right(90)
        forward(50)
        right(90)
        forward(200-y)
        right(90)
    end_fill()
def draw():
    clear()
    goto(bird.x, bird.y)
    dot(20, 'red')
    for pipe in pipes:
        goto(pipe.x, pipe.y)
        rect(pipe.x, pipe.y)
        #dot(40, 'black')
    
    update()

def refresh():
    for pipe in pipes:
        Xc=bird.x
        Yc=bird.y
        X1=pipe.x
        if pipe.y>0:
            Y1=pipe.y
            X2=X1+50
            Y2=200
        if checkOverlap(20, Xc, Yc, X1, Y1, X2, Y2):
            setposition(bird.x, bird.y)
            write("Game Over!", font=("Arial", 16, "normal"))
            bird.x = 0
            bird.y = 0
        if pipe.y<0:
            Y1=-200
            X2=X1+50
            Y2=pipe.y
            if checkOverlap(20, Xc, Yc, X1, Y1, X2, Y2):
                setposition(bird.x, bird.y)
                write("Game Over!", font = ("Arial", 16, "normal"))
                bird.y=0
                bird.y=0
    bird.y -=4
    if bird.y <=-200:
        bird.y = -200
    draw()
    for pipe in pipes:
        pipe.x -=10
        
    if randint(1, 15) ==5:
        yPos = randint(-200, 200)
        posPipe = point(200, yPos)
        pipes.append(posPipe)

    ontimer(refresh, 50)
ht()
penup()
tracer(0)
onkeypress(goUp, "space")
onkeypress(goRight, "Right")
onkeypress(goLeft, "Left")

listen()
refresh()
