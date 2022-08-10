import turtle
bob = turtle.Turtle()


def square(t):
    for i in range(4):
        t.lt(90)
        t.fd(100)


square(bob)

turtle.mainloop()
