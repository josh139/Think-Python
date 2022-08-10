import turtle
import math
bob = turtle.Turtle()


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    for i in range(n):
        t.lt(step_angle)
        t.fd(step_length)


arc(bob, 50, 180)

turtle.mainloop()
