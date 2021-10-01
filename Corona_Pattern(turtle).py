#Python code for a vibrant circle
#Corona like Pattern

from turtle import *

t=Turtle()
s=Screen()
s.bgcolor("black")
t.pencolor("cyan")
a,b=0,0
t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()

while True :
    t.forward(a)
    t.right(b)
    a+=3
    b+=1
    if b==210:
        break
        
t.hideturtle()
done()
