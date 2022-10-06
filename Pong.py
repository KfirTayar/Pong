from importlib import import_module
from tkinter import CENTER

import winsound
import turtle
import time
import keyboard

window = turtle.Screen() #Create a screeen
window.title("Pong by KfirTayar")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0) #Speed up the game

#Score
scoreA = 0
scoreB = 0

#Paddale A
paddleA = turtle.Turtle() #Create an object 
paddleA.speed(0)
paddleA.shape("square")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.color("white")
paddleA.penup()
paddleA.goto(-350, 0)

#Paddale B
paddleB = turtle.Turtle() #Create an object 
paddleB.speed(0)
paddleB.shape("square")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.color("white")
paddleB.penup()
paddleB.goto(350, 0)

#Ball
ball = turtle.Turtle() #Create an object 
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() #Hiding the object
pen.goto(0, 260)
pen.write("Player A:  0   ||   Player B:  0", align="center", font=("David", 24, "normal"))

#Functions
def paddleAUp():
    y = paddleA.ycor()
    y +=20
    paddleA.sety(y)

def paddleADown():
    y = paddleA.ycor()
    y -=20
    paddleA.sety(y)

def paddleBUp():
    y = paddleB.ycor()
    y +=20
    paddleB.sety(y)

def paddleBDown():
    y = paddleB.ycor()
    y -=20
    paddleB.sety(y)    

#Color mode
answer = turtle.textinput("Color mode", "Write L for Light or D for Dark ")
if (answer == "L"):
    paddleA.color("black")
    paddleB.color("black")
    ball.color("black")
    window.bgcolor("white")
    pen.color("black")

#Keyboard binding
window.listen()
window.onkeyrelease(paddleAUp, "w")
window.onkeyrelease(paddleADown, "s")
window.onkeyrelease(paddleBUp, "Up")
window.onkeyrelease(paddleBDown, "Down")
    
# Main game loop
while True:
    window.update()
    time.sleep(1/60)

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0,0)
        scoreA += 1 
        ball.dx = 2
        ball.dy = 2
        ball.dx *= -1 
        pen.clear()
        pen.write("Player A:  {}   ||   Player B:  {}".format(scoreA, scoreB), align="center", font=("David", 24, "normal"))
        winsound.PlaySound("point.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0,0)
        scoreB += 1
        ball.dx = 2
        ball.dy = 2
        ball.dx *= 1
        pen.clear()
        pen.write("Player A:  {}   ||   Player B:  {}".format(scoreA, scoreB), align="center", font=("David", 24, "normal"))
        winsound.PlaySound("point.wav", winsound.SND_ASYNC)


    #Paddle & ball collisions
    if ((ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 40)):
        ball.setx(340)
        ball.dx *= -1.2
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)

    if ((ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() - 40)):
        ball.setx(-340)
        ball.dx *= -1.2
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)

    #Winning the game
    if (scoreA == 3 or scoreB == 3):
        pen.clear()
        pen.write("Paddle {pronoun} is the winner!!".format(pronoun="A" if scoreA > scoreB else "B"), align="center", font=("David", 24, "normal"))
        winsound.PlaySound("win.wav", winsound.SND_ASYNC)
        time.sleep(5)
        pen.clear()
        pen.write("For a new game, please press ENTER", align="center", font=("David", 24, "normal"))

        #Wait until press ENTER
        start = time.time()
        keyboard.wait("enter")
        end = time.time()
        time_lapsed = end - start

        #Start a new game
        pen.clear()
        scoreA = scoreB = 0
        pen.write("Player A:  {}   ||   Player B:  {}".format(scoreA, scoreB), align="center", font=("David", 24, "normal"))


