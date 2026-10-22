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

monstre_direita = pygame.transform.flip(monstre_spritesheet, True, False)
monstre_direita.fill((255, 100, 100), special_flags=pygame.BLEND_RGB_MULT)
monstre_direita_x = 0
monstre_direita_ativo = False



run_animation = False
walk_animation = False
curr_frame_walk = 0
direçao = "esquerda"
curr_frame_att = 0
anim_time_att = 0
anim_time_walk = 0
centre = [100, 300]

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Atividade 11!')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
            monstre_direita_ativo =True
    if keys[pygame.K_RETURN]:
        run_animation = True
    if keys[pygame.K_LEFT]:
        centre[0]-=5
        walk_animation = True
        direçao = "esquerda"
    if keys[pygame.K_RIGHT]:
        centre[0]+=5
        walk_animation = True
        direçao = "direita"
    if centre[0]<= 10:
        centre[0] = 10
    if centre[0]>= 700:
        centre[0] = 700

    if monstre_direita_ativo:
        monstre_direita_x += 3
        if monstre_direita_x > 800:
            monstre_direita_x = -96

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
    
    if walk_animation:
        anim_time_walk = anim_time_walk + dt
        anim_time_walk_sec = anim_time_walk/1000
        if anim_time_walk_sec > 0.1:
            curr_frame_walk = curr_frame_walk + 1
            if curr_frame_walk > 5:
                curr_frame_walk = 0
                walk_animation = False
            anim_time_walk = 0

    screen.fill((255,255,255))
    screen.blit(Laype_img, (500, 300))
    screen.blit(monstre_spritesheet, (0, 0), (96*curr_frame, 0, 96, 96))
    screen.blit(Attack1, (200, 200), (96*curr_frame_att, 0, 96, 96))
    if direçao == "esquerda":
        screen.blit(Walk, centre, (96*curr_frame_walk, 0, 96,96))
    else:
        screen.blit(Walk_espelho,centre,(96*(5- curr_frame_walk), 0, 96, 96))
    if monstre_direita_ativo:
        screen.blit(monstre_direita, (monstre_direita_x, 100),(96*(3 -curr_frame),0, 96,96))
    else:
        screen.blit(monstre_direita, (monstre_direita_x, 100),(96*3,0, 96, 96))

    pygame.display.update()