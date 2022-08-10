import turtle
bob = turtle.Turtle()


def square(t, length):
    for i in range(4):
        t.lt(90)
        t.fd(length)


square(bob, 300)

turtle.mainloop()
