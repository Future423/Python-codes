import turtle as t

t.bgcolor("black")
#setting background color <black>

t.color("red")
#setting pen color <red>

t.hideturtle()
#hiding turtle

t.speed(3)
#setting speed <max speed is 0>

#for loop for star 
for i in range(500):
    t.forward(i)
    t.right(144)
