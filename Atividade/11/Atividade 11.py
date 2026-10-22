from pygame import *
import math

init()
screen = display.set_mode((1000,800))

#recursos
scooby_imagem = image.load("Atividade/5/scooby.png")
scooby_imagem = transform.scale(scooby_imagem, (200,200))
scooby_fonte= font.Font("Atividade/5/AlienBlock-Regular.ttf", 30)


def lignes_autour_cercle(screen, centre, rayon, nombre):
    for i in range(nombre):
        angle = i * 360 / nombre
        x = centre[0]+rayon*math.cos(math.radians(angle))
        y = centre[1]+rayon*math.sin(math.radians(angle))
        draw.line(screen, "#FFF251", centre, (x, y), 8)
        draw.circle(screen, "#FFF251", centre, 4)
        draw.circle(screen, "#FFF251", (x, y), 4)

clock = time.Clock()
centre = [100, 100]


x=500
speed=1

running = True
while running:
    clock.tick(60)
    touches = key.get_pressed()

    for ev in event.get():
        if ev.type == QUIT:
            running = False
        if ev.type == MOUSEMOTION:
             centre[0], centre[1] = ev.pos
             if centre[0]<= 100:
                    centre[0] = 100
             if centre[0]>= 700:
                    centre[0] = 700
             if centre[1]<= 100:
                    centre[1] = 100
             if centre[1]>= 500:
                    centre[1] = 500


    screen.fill("#87CEEB")
    draw.circle(screen, "#FFF251", centre,50)
    lignes_autour_cercle(screen,centre,100,8)

    
    if touches[K_LEFT]:
        centre[0]-=5
    if touches[K_RIGHT]:
        centre[0]+=5
    if touches[K_UP]:
        centre[1]-=5
    if touches[K_DOWN]:
        centre[1]+=5
    if centre[0]<= 100:
        centre[0] = 100
    if centre[0]>= 700:
        centre[0] = 700
    if centre[1]<= 100:
        centre[1] = 100
    if centre[1]>= 500:
        centre[1] = 500


    x += speed
    if x >= 600:
        speed = -1
    if x <= 50:
        speed = 1
    
    draw.circle(screen, "white", (x,100),50)
    draw.circle(screen, "white", (x+50,100),50)
    draw.circle(screen, "white", (x+100,100),50)
    draw.circle(screen, "white", (x+150,100),50)

    screen.blit(scooby_imagem,(400,400))


    display.update()

