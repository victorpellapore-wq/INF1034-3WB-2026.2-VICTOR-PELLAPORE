import pygame, sys, os
from pygame.locals import QUIT, KEYDOWN

clock = pygame.time.Clock()

#tive um problema para acesar os meus documentos, entao criou isso
DOSSIER=os.path.dirname(os.path.abspath(__file__))

Laype_img = pygame.image.load(os.path.join(DOSSIER, "Laype.png"))

curr_frame = 0
anim_time = 0

monstre_spritesheet = pygame.image.load(os.path.join(DOSSIER, "monstre_walk.png"))
Attack1 = pygame.image.load(os.path.join(DOSSIER, "Attack1.png"))

run_animation = False
curr_frame_att = 0
anim_time_att = 0

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Atividade 11!')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #alterei a linha de codigo seguinte para que se atualize o estado do teclado
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        run_animation = True

    clock.tick(60)
    dt = clock.get_time()

    anim_time = anim_time + dt
    anim_time_sec = anim_time/1000

    if anim_time_sec > 0.15:
        curr_frame = curr_frame + 1
        if curr_frame > 3:
            curr_frame = 0
        anim_time = 0

    if run_animation:
        anim_time_att = anim_time_att + dt
        anim_time_att_sec = anim_time_att/1000
        if anim_time_att_sec > 0.1:
            curr_frame_att = curr_frame_att+ 1
            if curr_frame_att > 5:
                curr_frame_att = 0
                run_animation = False
            anim_time_att = 0

    # Desenho dos elementos na tela
    screen.fill((255,255,255))

    screen.blit(Laype_img, (500, 300))
    screen.blit(monstre_spritesheet, (0, 0), (96*curr_frame, 0, 96, 96))
    screen.blit(Attack1, (200, 200), (96*curr_frame_att, 0, 96, 96))


    # if curr_frame_mm < 5:
    #     screen.blit(megaman_spritesheet, (200, 200), (60 * curr_frame_mm, 0, 60, 60))
    # else:
    #     screen.blit(megaman_spritesheet, (200, 200), (60 * (curr_frame_mm - 5), 60, 60, 60))
    
    #screen.blit(megaman_spritesheet, (200, 200), (60*(curr_frame_mm%5), 60*(curr_frame_mm//5), 60, 60))

    pygame.display.update()