import turtle

wn = turtle.Screen()
wn.screensize(1000)
wn.bgcolor("black")

v = turtle.Turtle()
v.speed(10)
w = turtle.Turtle()
w.speed(10)
x = turtle.Turtle()
x.speed(10)
y = turtle.Turtle()
y.speed(10)
z = turtle.Turtle()
z.speed(10)

a = turtle.Turtle()
a.pensize(5)
a.speed(10)

b = turtle.Turtle()
b.speed(10)
b.pensize(1)
b.shape("circle")

w.penup(); w.goto(400,200); w.pendown()
x.penup(); x.goto(400,-200); x.pendown()
y.penup(); y.goto(-400,200); y.pendown()
z.penup(); z.goto(-400,-200); z.pendown()

angle = 135


for i in range(60):
    for color in["red", "darkgoldenrod", "darkolivegreen", "dodgerblue" ]:
        for nm in["1", "2", "3", "4"]:
            gradient = color + nm
            v.color(gradient)
            j = i*4
            v.circle(i,angle)
            v.penup()
            v.forward(j)
            v.left(10)
            v.pendown()

for numw in range(75):
     for colorw in["firebrick", "red", "indianred", "brown" ]:
        w.color(colorw)
        j = numw*3
        w.circle(numw,angle)
        w.penup()
        w.forward(j)
        w.left(25)
        w.pendown()

for numx in range(75):
    for colorx in["deepskyblue", "dodgerblue", "royalblue", "steelblue" ]:
        x.color(colorx)
        j = numx*3
        x.circle(numx,angle)
        x.penup()
        x.forward(j)
        x.left(40)
        x.pendown()

for numy in range(75):
     for colory in["seagreen", "springgreen", "darkolivegreen", "darkseagreen" ]:
        y.color(colory)
        j = numy*3
        y.circle(numy,angle)
        y.penup()
        y.forward(j)
        y.left(60)
        y.pendown()

for numz in range(75):
    for colorz in["goldenrod", "darkgoldenrod", "gold", "lightgoldenrod" ]:
        z.color(colorz)
        j = numz*3
        z.circle(numz,angle)
        z.penup()
        z.forward(j)
        z.left(75)
        z.pendown()

for i in range(0, 9):
    a.color("royalblue")
    a.penup()
    a.forward(150)
    a.pendown()
    a.forward(10)
    a.penup()
    a.forward(20)
    a.stamp()
    a.forward(-180)
    a.right(10)

for i in range(9, 18):
    a.color("darkgoldenrod")
    a.penup()
    a.forward(150)
    a.pendown()
    a.forward(10)
    a.penup()
    a.forward(20)
    a.stamp()
    a.forward(-180)
    a.right(10)

for i in range(18, 27):
    a.color("darkolivegreen")
    a.penup()
    a.forward(150)
    a.pendown()
    a.forward(10)
    a.penup()
    a.forward(20)
    a.stamp()
    a.forward(-180)
    a.right(10)

for i in range(27, 36):
    a.color("firebrick")
    a.penup()
    a.forward(150)
    a.pendown()
    a.forward(10)
    a.penup()
    a.forward(20)
    a.stamp()
    a.forward(-180)
    a.right(10)

for i in range(0, 9):
    b.color("royalblue")
    b.penup()
    b.forward(200)
    b.stamp()
    b.forward(-200)
    b.right(10)

for i in range(9, 18):
    b.color("darkgoldenrod")
    b.penup()
    b.forward(200)
    b.stamp()
    b.forward(-200)
    b.right(10)

for i in range(18, 27):
    b.color("darkolivegreen")
    b.penup()
    b.forward(200)
    b.stamp()
    b.forward(-200)
    b.right(10)

for i in range(27, 36):
    b.color("firebrick")
    b.penup()
    b.forward(200)
    b.stamp()
    b.forward(-200)
    b.right(10)

wn.exitonclick()