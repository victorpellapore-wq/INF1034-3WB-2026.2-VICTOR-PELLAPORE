from turtle import *
from random import *
from time import sleep
t = Turtle()
colormode(255)
t.hideturtle()
t.pu()
t.speed(0)
t.goto(-400, 0)
t.pd()

# desenho recursivo fácil
for i in range (8):
   for i in range(8):
        t.fd(70)
        t.lt(45)
   t.fd(100)

sleep(2)
t.clear()
t.pu()
t.goto(0,0)
t.pd()

# desenho recursivo medio
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

size = int(textinput("Tamanho da estrela","Entre o tamanho da estrela"))
Pontas = int(textinput("Número de puntas","Entre o número de puntas"))

estrela(t,size,Pontas)

sleep(2)
t.clear()
t.pu()
t.goto(0,0)
t.pd()

# desenho recursivo difícil
def SnowBranchFractal(t, size, angle, nivel):
    if size < 40:
        return
    t.pd()
    t.fd(size)

    t.rt(angle)
    t.fd(size)
    SnowBranchFractal(t, size * 0.8, angle, nivel - 1)
    t.back(size)
    t.pencolor(0, 255 // nivel, 0)

    t.lt(angle)
    t.fd(size)
    SnowBranchFractal(t, size * 0.8, angle, nivel - 1)
    t.back(size)
    t.pencolor(0, 255 // nivel, 0)

    t.lt(angle)
    t.fd(size)
    SnowBranchFractal(t, size * 0.8, angle, nivel - 1)
    t.back(size)
    t.pencolor(0, 255 // nivel, 0)

    t.lt(-angle)
    t.back(size)

for i in range (4):
    SnowBranchFractal(t, 80, 30, 20)
    t.rt(90)

mainloop()