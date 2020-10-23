import turtle
turtle.bgcolor("black")
#turtle.pensize(2)
turtle.speed(0)
for i in range(8):
    for col in ('red','cyan','white','magenta','yellow'):
        turtle.color(col)
        turtle.circle(100)
        turtle.right(10)
turtle.hideturtle()
