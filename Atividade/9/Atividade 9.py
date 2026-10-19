from turtle import*
t = Turtle()
t.hideturtle()
t.pu()
t.goto(-400,0)
t.pd()
t.speed(0)

for i in range (8):
    for i in range(8):
        t.fd(100)
        t.lt(45)
    t.fd(100)




mainloop()



