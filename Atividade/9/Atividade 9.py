from turtle import*
t = Turtle()
t.hideturtle()
t.pu()
t.goto(-400,0)
t.pd()
t.speed(0)



size = int(textinput("Tamaño da estrela","Ingrese o tamaño da estrela"))
Pontas = int(textinput("Número de puntas","Ingrese el número de puntas"))

def estrela(t,size,angulo):
    for i in range (angulo):
        if angulo<4:
             return
        else:
            t.fd(size)
            t.rt(180 - 180/angulo)
            t.fd(size)
            t.lt(180 - 180/angulo)
            t.rt(360/angulo)


for i in range (Pontas):
    estrela(t,size,Pontas)
    t.pu()
    t.fd(size*3)
    t.pd()



for i in range (8):
    for i in range(8):
        t.fd(100)
        t.lt(45)
    t.fd(100)


mainloop()



