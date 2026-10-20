from turtle import *
from random import *
t = Turtle()
colormode(255)
t.hideturtle()
t.pu()
t.pd()
t.speed(0)



for i in range (8):
    for i in range(8):
        t.fd(100)
        t.lt(45)
    t.fd(100)

size = int(textinput("Tamanho da estrela","Entre o tamanho da estrela"))
Pontas = int(textinput("Número de puntas","Entre o número de puntas"))

def randomColor():
    return (randint(0, 100), randint(0, 100), randint(100, 255))

def estrela(t, size, angulo):
    if size < 4:
        return
    t.begin_fill()
    t.fillcolor(randomColor())
    for i in range(angulo):
        t.fd(size)
        t.rt(180 - 180 / angulo)
        t.fd(size)
        t.lt(180 - 180 / angulo)
        t.rt(360 / angulo)
        estrela(t, size / 3, angulo)
    t.end_fill()


def treeFractal(t, size, angle, nivel):
    if size < 40:
        return
    t.pd()
    t.fd(size)

    # right tree 
    t.rt(angle)
    t.fd(size)
    treeFractal(t, size * 0.8, angle, nivel - 1)
    t.back(size)

    turtle.pencolor(0, 255 // nivel, 0)

    # left tree
    t.lt(2 * angle)
    t.fd(size)
    treeFractal(t, size * 0.8, angle, nivel - 1)
    t.back(size)

    turtle.pencolor(0, 255 // nivel, 0)
    t.lt(-angle)
    t.back(size)


#estrela(t,size,Pontas)




mainloop()