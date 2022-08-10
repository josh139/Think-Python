import turtle
import math
bob = turtle.Turtle()


def polygon(t, length, n):
    for i in range(n):
        t.lt(360 / n)
        t.fd(length)
    return n


def circle(t, r):
    circumference = 2 * math.pi * r
    length = circumference / 360
    n = polygon(t, length, 360)
    if circumference == length * n:
        print(True)
    else:
        print(False)


circle(bob, 50)

turtle.mainloop()
