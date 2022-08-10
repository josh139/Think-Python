import turtle
bob = turtle.Turtle()


def polygon(t, length, n):
    for i in range(n):
        t.lt(360 / n)
        t.fd(length)


polygon(bob, 100, 9)

turtle.mainloop()
