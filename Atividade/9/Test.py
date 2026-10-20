import turtle
t = turtle.Turtle()
turtle.colormode(255)


def treeFractal(t, size, angle, nivel):
    if size < 40:
        return
    t.pd()
    t.fd(size)

    t.rt(angle)
    t.fd(size)
    treeFractal(t, size * 0.8, angle, nivel - 1)
    t.back(size)
    turtle.pencolor(0, 255 // nivel, 0)

    t.lt(angle)
    t.fd(size)
    treeFractal(t, size * 0.8, angle, nivel - 1)
    t.back(size)
    turtle.pencolor(0, 255 // nivel, 0)

    t.lt(angle)
    t.fd(size)
    treeFractal(t, size * 0.8, angle, nivel - 1)
    t.back(size)
    turtle.pencolor(0, 255 // nivel, 0)

    t.rt(angle)
    t.back(size)

treeFractal(t, 80, 40, 20)

mainloop()