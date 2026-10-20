from turtle import *
from random import *
t = Turtle()
colormode(255)
t.hideturtle()
t.pu()
t.pd()
t.speed(0)



#for i in range (8):
   # for i in range(8):
   #    t.fd(100)
   #     t.lt(45)
    #t.fd(100)

#size = int(textinput("Tamanho da estrela","Entre o tamanho da estrela"))
#Pontas = int(textinput("Número de puntas","Entre o número de puntas"))

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


def SnowFractal(t, size, angle, nivel):
    if size < 40:
        return
    t.pd()
    t.fd(size)

    # right tree 
    t.rt(angle)
    t.fd(size)
    SnowFractal(t, size * 0.8, angle, nivel - 1)
    t.back(size)
    t.pencolor(0, 255 // nivel, 0)

    t.lt(angle)
    t.fd(size)
    SnowFractal(t, size * 0.8, angle, nivel - 1)
    t.back(size)
    t.pencolor(0, 255 // nivel, 0)

    t.lt(angle)
    t.fd(size)
    SnowFractal(t, size * 0.8, angle, nivel - 1)
    t.back(size)
    t.pencolor(0, 255 // nivel, 0)

    t.lt(-angle)
    t.back(size)

    


t.lt(90)
SnowFractal(t, 80, 30, 20)

#estrela(t,size,Pontas)




mainloop()