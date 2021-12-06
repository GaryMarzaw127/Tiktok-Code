import turtle
import random
import math

turtle.setup(1000,1000)
a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
d = turtle.Turtle()
e = turtle.Turtle()
f = turtle.Turtle()
g = turtle.Turtle()
h = turtle.Turtle()

a.color('brown')
b.color('green')
c.color('blue')
d.color('red')
e.color('purple')
f.color('yellow')
g.color('black')
h.color('orange')

tlist = []
tlist.append(a)
tlist.append(b)
tlist.append(c)
tlist.append(d)
tlist.append(e)
tlist.append(f)
tlist.append(g)
tlist.append(h)

turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
sum = 0
count = 0
for j in range(100):  
    for i in range(10000):
        for t in tlist:
            t.seth(random.randrange(0,350,90))
            t.fd(10)
        turtle.update()
    for t in tlist:
        sum += math.sqrt(t.xcor()*t.xcor() + t.ycor()*t.ycor())/10*2*math.sqrt(t.xcor()*t.xcor() + t.ycor()*t.ycor())/10*2/100
        count += 1
    for t in tlist:
        t.clear()
        t.up()
        t.goto(0,0)
        t.down()
    print(sum/count)

    


