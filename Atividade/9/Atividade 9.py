from turtle import*
t = Turtle()
t.hideturtle()
t.pu()
t.goto(-400,0)
t.pd()
t.speed()

for i in range (5):
        t.fd(20)
        t.lt(72)
        t.fd(20)
        t.rt(144)

for i in range (8):
    for i in range(8):
        t.fd(100)
        t.lt(45)
    t.fd(100)

def estrella(t,size,ponta):
    for i in range (ponta):
        if ponta<3:
             return
        else:
        t.fd(size)
        t.lt(360/ponta)
        t.fd(size)
        t.rt(360)



mainloop()



