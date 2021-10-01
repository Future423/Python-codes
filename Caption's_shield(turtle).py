from turtle import *
bgcolor("white")
pencolor("red")
hideturtle()
speed(0)

penup()
goto(0,-200)
pendown()
pensize(5)
circle(240)

penup()
goto(0,-160)
pendown()
circle(200)

penup()
goto(0,-120)
pendown()
circle(160)

penup()
goto(0,-80)
pendown()
circle(120)

penup()
goto(0,40)
pendown()
pencolor("blue")

for i in range(220):    #for star
    forward(i)
    right(144)
