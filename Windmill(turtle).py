import turtle as t

t.speed(0)#max speed

t.bgcolor("black")#Baackground color
t.pencolor("red")#Pen colour

for i in range(190):
    t.left(30)
    t.forward(i)
    t.right(120)
    t.forward(i)
    t.right(120)
    t.forward(i)
    t.right(90)
    t.forward(i)
