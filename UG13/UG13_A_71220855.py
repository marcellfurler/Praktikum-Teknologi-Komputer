import turtle
t=turtle.Turtle()
s=turtle.Screen()

# keterangan nama "M"arcell Ma"N"uhutu 71220"855"
# jadinya M855N

# M
t.pensize(15)
s.bgcolor("#22A7F0")


t.right(90)
t.forward(150)
t.backward(150)

t.left(45)
t.forward(90)

t.left(95)
t.forward(90)

t.right(140)
t.forward(150)

t.right(270)
t.penup()
t.forward(50)

t.pendown()


# 8
# t.circle(45, 180)
# t.circle(45, 360)
# t.penup()
# t.goto(50, 100)
# t.pendown()
# t.circle(45, 180)
# t.circle(45, 360)

# 8
t.left(90)
t.forward(75)
for i in range(4):
    t.right(90)
    t.forward(75)

t.forward(75)
t.right(90)
t.forward(75)
t.right(90)
t.forward(150)


# 5
t.right(270)
t.penup()
t.forward(50)

t.pendown()

t.forward(75)
t.left(90)
t.forward(75)
t.left(90)
t.forward(75)
t.right(90)
t.forward(75)
t.right(90)
t.forward(75)


# 5
t.right(180)

t.forward(75)
t.left(90)
t.forward(75)
t.left(90)
t.forward(75)
t.right(90)
t.forward(75)

t.right(270)
t.penup()
t.forward(50)

t.pendown()

t.right(270)
t.penup()
t.forward(0)

t.pendown()

t.right(90)
t.forward(75)
t.left(90)
t.forward(75)
t.left(90)
t.forward(75)
t.right(90)
t.forward(75)
t.right(90)
t.forward(75)

t.right(180)

t.forward(75)
t.left(90)
t.forward(75)
t.left(90)
t.forward(75)
t.right(90)
t.forward(75)

t.right(270)
t.penup()
t.forward(50)

t.pendown()


# N
t.left(90)
t.forward(150)
t.right(150)
t.forward(180)
t.left(150)
t.forward(155)

t.hideturtle()


s.exitonclick()