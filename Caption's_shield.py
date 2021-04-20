import turtle as t
t.bgcolor("white")
t.pencolor("red")
t.hideturtle()
t.speed(0)

t.penup()
t.goto(0,-200)
t.pendown()
t.pensize(5)
t.circle(240)

t.penup()
t.goto(0,-160)
t.pendown()
t.circle(200)

t.penup()
t.goto(0,-120)
t.pendown()
t.circle(160)

t.penup()
t.goto(0,-80)
t.pendown()
t.circle(120)

t.penup()
t.goto(0,40)
t.pendown()
t.pencolor("blue")

for i in range(220):    #for star
    t.forward(i)
    t.right(144)
