#Ryne Bigueras
#3/5/2022

#Problem 5 Squares

import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

mv = -10

for sz in range(20, 101, 20):
    drawSquare(alex, sz)
    alex.penup()
    alex.goto(mv,mv)
    alex.pendown()
    mv = mv -10

wn.exitonclick()
