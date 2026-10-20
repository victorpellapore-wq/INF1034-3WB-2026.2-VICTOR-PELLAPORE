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


#estrela(t,size,Pontas)




mainloop()