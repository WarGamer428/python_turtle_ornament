from turtle import *
speed(0)
rt(90)
def square():
    for x in range(10):
        fd(50)
        lt(36)
def ornamentThingy():
    for x in range(21):
        square()
        lt(10)
ornamentThingy()
done()