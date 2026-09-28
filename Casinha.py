from pygame import *
import math

init()
screen = display.set_mode((800,600))

#recursos
bat_imagem = image.load("scooby")
bat_imagem = transform.scale(bat_imagem, (200,200))
bat_fonte= font.Font("AlienBlock-Regular.ttf", 30)
mixer.music.load("ScoobyDoo_Generic.mp3")
mixer.music.play(-1)

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

    ## desenhar os elementos na tela
    # screen.fill(151,209,250)
    screen.fill("#97D1FA")

    draw.rect(screen, "#489D25", (0,500,800,100))
    draw.circle(screen, "#FFF251", centre,50)
    lignes_autour_cercle(screen,centre,100,8)

    touches = key.get_pressed()
    
    if touches[K_LEFT]:
        centre[0]-=5
    if touches[K_RIGHT]:
        centre[0]+=5
    if touches[K_UP]:
        centre[1]-=5
    if touches[K_DOWN]:
        centre[1]+=5



    x += speed
    if x >= 600:
        speed = -1
    if x <= 50:
        speed = 1
    
    draw.circle(screen, "white", (x,100),50)
    draw.circle(screen, "white", (x+50,100),50)
    draw.circle(screen, "white", (x+100,100),50)
    draw.circle(screen, "white", (x+150,100),50)

    # HOUSE
    draw.polygon(screen, "#F2883B",((100,300),(200,200),(300,300)))
    draw.polygon(screen, "grey",((100,300),(300,300),(300,500),(100,500)))
    draw.polygon(screen, "brown",((200,350),(275,350),(275,500),(200,500)))
    draw.circle(screen, "black", (210,425),5)
    draw.polygon(screen, "blue",((110,375),(160,375),(160,450),(110,450)))

    # TREE
    draw.polygon(screen, "brown",((600,400),(630,400),(630,500),(600,500)))
    draw.circle(screen, "#489D25", (615,350),80)

    screen.blit(bat_imagem,(400,400))

    steve_text = bat_fonte.render("Scooby-Doo by-DOOOOOOO!", True, "#000000")
    screen.blit(steve_text,(300,300))


    display.update()

