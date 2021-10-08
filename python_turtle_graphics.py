import turtle

t = turtle.Turtle()
t.pencolor("red")
t.speed(0)
t.rt(90)

def square():
    for x in range(10):
        t.fd(50)
        t.lt(36)

def ornamentThingy():
    for x in range(23):
        square()
        t.lt(10)

ornamentThingy()
turtle.done()
