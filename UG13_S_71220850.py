import turtle


t = turtle.Turtle()

t.reset()
t.pencolor('blue')
t.pensize(5)
t.penup()
t.goto(-200, 100)

# Draw The Letter 'S'
t.pendown()
t.rt(180)
t.fd(20)
t.circle(30, 180)
t.circle(-30, 180)
t.fd(20)

t.penup()
t.goto(-140, 100)

# Draw The Letter '8'
t.pendown()
t.lt(180)
t.circle(-30, 180)
t.circle(30, 180)
t.circle(30, 180)
t.circle(-30, 180)

t.penup()
t.goto(-20, 100)

# Draw The Letter '5'
t.pendown()
t.rt(180)
t.fd(60)
t.lt(90)
t.fd(50)
t.lt(90)
t.fd(30)
t.circle(-30, 180)
t.fd(30)

t.penup()
t.goto(40, 100)

# Draw The Letter '0'
t.pendown()
t.lt(180)
t.circle(-30, 90)
t.fd(50)
t.circle(-30, 90)
t.circle(-30, 90)
t.fd(50)
t.circle(-30, 90)

t.penup()
t.goto(110, 100)

# Draw The Letter 'N'
t.pendown()
t.rt(90)
t.fd(100)
t.bk(100)
t.lt(40)
t.fd(120)
t.lt(140)
t.fd(100)


turtle.exitonclick()