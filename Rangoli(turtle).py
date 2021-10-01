from turtle import *

bgcolor("black")
speed(0)
for i in range(8):
    for col in ('red','cyan','white','magenta','yellow'):
        color(col)
        circle(100)
        right(10)
        
hideturtle()
