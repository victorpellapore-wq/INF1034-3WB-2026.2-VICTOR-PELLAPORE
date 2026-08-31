from turtle import *
from time import sleep

t = Turtle()

# Bandeira da França
t.fillcolor("#002654")
t.begin_fill()
t.fd(50)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(50)
t.lt(90)
t.fd(100)
t.lt(90)
t.end_fill()

t.pu()
t.goto(50, 0)
t.pd()

t.fillcolor("#ffffff")
t.begin_fill()
t.fd(50)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(50)
t.lt(90)
t.fd(100)
t.lt(90)
t.end_fill()

t.pu()
t.goto(100, 0)
t.pd()

t.fillcolor("#C81025")
t.begin_fill()
t.fd(50)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(50)
t.lt(90)
t.fd(100)
t.lt(90)
t.end_fill()

sleep(2)
t.clear()

mainloop()