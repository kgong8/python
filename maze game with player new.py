from turtle import *
maze=[
    "PXXXXXXXXXXXXXXXXXXX",
    "  XXXXXXXXXXX XXXXXX",
    "X X   XXXXXXX XXXXXX",
    "X X X XXXXXXX XXXXXX",
    "X X X XXXXX     XXXX",
    "X X X XXXXX XXX XXXX",
    "X   X XXXXX XXX XXXX",
    "X XXX XXXXX XXX XXXX",
    "XXXXX       XXX XXXX",
    "XXXXXXXX XXXXXX XXXX",
    "XXXXXXXX XXX XX    X",
    "XXXXXXXX XXX XXXXX X",
    "XXXXXXXX XXX XXXXX X",
    "X XXX XXXXXX XXXXXEX",
    ]

bgcolor("black")
penup()
tracer(0)

player = Turtle()
player.color('red')
player.shape('turtle')
player.penup()


def drawMaze():
    global player
    global pxPos
    global pyPos
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            char = maze[i][j]
            xPos = 25*j-200
            yPos = -25*i+200
            if char == "X":
                goto(xPos, yPos)
                color("white")
                shape("square")
                stamp()
            if char == "E":
                goto(xPos, yPos)
                color("green")
                shape("circle")
                stamp()
            if char == "P":
                pxPos = xPos
                pyPos = yPos
                player.goto(xPos, yPos) 

def goUp():
    global player
    player.left(90)
    player.forward(25)
    player.right(90)
    i = int((player.ycor()-200)/(-25))
    j = int((player.xcor()+200)/25)
    if maze[i][j] == "X":
        player.goto(pxPos, pyPos)
    if  player.ycor() > 200:
                player.goto(pxPos, pyPos)
            
            
def goDown():
    global player
    player.right(90)
    player.forward(25)
    player.left(90)
    i = int((player.ycor()-200)/(-25))
    j = int((player.xcor()+200)/25)
    if maze[i][j] == "X":
        player.goto(pxPos, pyPos)
    if maze[i][j] == "E":
            player.write("You win", font=("Arial", 30, "normal"))
                    
          
def goLeft():
    global player
    player.left(180)
    player.forward(25)
    player.right(180)
    i = int((player.ycor()-200)/(-25))
    j = int((player.xcor()+200)/25)
    if maze[i][j] == "X":
        player.goto(pxPos, pyPos)
    if  player.xcor() < -200:
                player.goto(pxPos, pyPos)
    
    
    
def goRight():
    global player
    player.forward(25)
    i = int((player.ycor()-200)/(-25))
    j = int((player.xcor()+200)/25)
    if maze[i][j] == "X":
        player.goto(pxPos, pyPos)
   
    
drawMaze()
onkey(goLeft, "Left")
onkey(goRight, "Right")
onkey(goUp, "Up")
onkey(goDown, "Down")
listen()

while True:
    update()
