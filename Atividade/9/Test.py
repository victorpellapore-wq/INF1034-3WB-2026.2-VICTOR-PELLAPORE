from turtle import *
t = Turtle()
t.speed(0)



def estrela(t, size, angulo):
    if size <4:
        return

    for i in range(angulo):
        t.fd(size)
        estrela(t, size/3, angulo)
        t.rt(180 - 180 / angulo)
        t.fd(size)
        t.lt(180 - 180 / angulo)
        t.rt(360 / angulo)

estrela(t, 100, 4)


mainloop()