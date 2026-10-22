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
Walk = pygame.image.load(os.path.join(DOSSIER, "Walk.png"))
Walk_espelho = pygame.transform.flip(Walk, True, False)



run_animation = False
walk_lt_animation = False
walk_rt_animation = False
curr_frame_walk_lt = 0
curr_frame_att = 0
anim_time_att = 0
anim_time_walk = 0
centre = [100, 100]

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

    if keys[pygame.K_LEFT]:
        walk_lt_animation = True
        centre[0]-=5
    if keys[pygame.K_RIGHT]:
        centre[0]+=5
        walk_rt_animation = True
    if centre[0]<= 10:
        centre[0] = 10
    if centre[0]>= 790:
        centre[0] = 790

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
    
    if walk_lt_animation:
        anim_time_walk = anim_time_walk + dt
        anim_time_walk_sec = anim_time_walk/1000
        if anim_time_walk_sec > 0.1:
            curr_frame_walk_lt = curr_frame_walk_lt + 1
            if curr_frame_walk_lt > 5:
                curr_frame_walk_lt = 0
                walk_lt_animation = False
            anim_time_walk = 0

    if walk_rt_animation:
            anim_time_walk = anim_time_walk + dt
            anim_time_walk_sec = anim_time_walk/1000
            if anim_time_walk_sec > 0.1:
                curr_frame_walk_rt = curr_frame_walk_rt + 1
                if curr_frame_walk_rt > 5:
                    curr_frame_walk_rt = 0
                    walk_rt_animation = False
                anim_time_walk = 0
        

    
    screen.fill((255,255,255))

    screen.blit(Laype_img, (500, 300))
    screen.blit(monstre_spritesheet, (0, 0), (96*curr_frame, 0, 96, 96))
    screen.blit(Attack1, (200, 200), (96*curr_frame_att, 0, 96, 96))
    if walk_lt_animation :
        screen.blit(Walk, (centre[0],300), (96*curr_frame_walk_lt, 0, 96, 96))
    else:
        screen.blit(Walk_espelho, (centre[0], 200), (96*(5 - curr_frame_att), 0, 96, 96))






    # if curr_frame_mm < 5:
    #     screen.blit(megaman_spritesheet, (200, 200), (60 * curr_frame_mm, 0, 60, 60))
    # else:
    #     screen.blit(megaman_spritesheet, (200, 200), (60 * (curr_frame_mm - 5), 60, 60, 60))
    
    #screen.blit(megaman_spritesheet, (200, 200), (60*(curr_frame_mm%5), 60*(curr_frame_mm//5), 60, 60))

    pygame.display.update()