import pygame, sys, os
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((896, 640)) #14 x10 tiles de 64 pixels
clock = pygame.time.Clock()
tile_size = 60
tile_size_joguinho = 64
pasta_do_script = os.path.dirname(os.path.abspath(__file__))
tileset = pygame.image.load(os.path.join(pasta_do_script, "tileset_neige_5x5.png"))
can_walk = True

#Personagem da Atividade 11
Walk = pygame.image.load(os.path.join(pasta_do_script, "Walk.png"))
Walk_espelho = pygame.transform.flip(Walk, True, False)
curr_frame_walk = 0
anim_time_walk = 0
direçao = "direita"

#ajustamento do desenho do personagem (usei a AI para entender como adaptar coreitamente ao mapa)
largura_jogador = 44
altura_jogador = 42
monstro_y = 54 
monstro_x_esquerda = 36 
monstro_x_direita = 16

pos_x = 80
pos_y = 320 - altura_jogador
velocidade = 0.25
mostrar_colliders = False

tiles = {
    "E": (0, 0),
    "G": (1, 0),
    "D": (2, 0),
    "I": (3, 0),
    "H": (4, 0),
    "L": (0, 1),
    "T": (1, 1),
    "R": (2, 1),
    "A": (3, 1),
    "P": (4, 1),
    "Q": (0, 2),
    "U": (1, 2), 
    "W": (2, 2),
    "N": (3, 2), 
    "Y": (4, 2),
    "S": (0, 3),
    "C": (1, 3),
    "B": (2, 3),
    "K": (3, 3), 
    "F": (4, 3),
    "V": (0, 4), 
    "O": (1, 4), 
    "M": (2, 4), 
    "Z": (3, 4), 
    "J": (4, 4),
}

mapa_joguinho = [
  "XXXXXXXXXXXXXX",
  "XXXXXXXXXXXXXX",
  "XXXXXKXXXXXXCX",
  "XXIXEGDIYEGGGG",
  "VXXXQUWXYQUUTT",
  "GDOXXHXXYFHHLT",
  "TTDZXXXXYBSSLT",
  "TTTDNNNEGGGGTT",
  "TTTRAAALTTTTTT",
  "TTTRPPPLTTTTTT",
]

# Tiles duros: sol, gelo, arvores e caixa
tiles_duros = "EGDLTRQUWIVOB"
colliders = []
for i in range(len(mapa_joguinho)):
    for j in range(len(mapa_joguinho[i])):
        letra = mapa_joguinho[i][j]
        x = j * tile_size_joguinho
        y = i * tile_size_joguinho
        if letra in tiles_duros:
            colliders.append(pygame.Rect(x, y, tile_size_joguinho, tile_size_joguinho))
        elif letra == "N":
            colliders.append(pygame.Rect(x, y, tile_size_joguinho, 20))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(60)
    dt= clock.get_time()
    keys = pygame.key.get_pressed()

    andando = False

    # Movimento horizontal
    old_pos_x = pos_x
    if keys[pygame.K_RIGHT]:
        pos_x = pos_x + velocidade*dt
        direçao = "direita"
        andando = True
    elif keys[pygame.K_LEFT]:
        pos_x = pos_x - velocidade*dt
        direçao = "esquerda"
        andando = True
    if pos_x < 0:
        pos_x = 0
    if pos_x > screen.get_width()- largura_jogador:
        pos_x = screen.get_width() -largura_jogador
    collider_jogador = pygame.Rect(pos_x, pos_y, largura_jogador, altura_jogador)
    for collider in colliders:
        if collider_jogador.colliderect(collider):
            pos_x = old_pos_x

    # Movimento vertical
    old_pos_y = pos_y
    if keys[pygame.K_UP]:
        pos_y= pos_y-velocidade*dt
        andando =True
    elif keys[pygame.K_DOWN]:
        pos_y =pos_y +velocidade*dt
        andando = True
    if pos_y < 0:
        pos_y= 0
    collider_jogador= pygame.Rect(pos_x, pos_y, largura_jogador, altura_jogador)
    for collider in colliders:
        if collider_jogador.colliderect(collider):
            pos_y =old_pos_y

    #Animacao de andar da atividade 11
    if andando:
        anim_time_walk = anim_time_walk + dt
        if anim_time_walk/1000 > 0.1:
            curr_frame_walk = curr_frame_walk + 1
            if curr_frame_walk > 5:
                curr_frame_walk = 0
            anim_time_walk = 0
    else:
        curr_frame_walk = 0
        anim_time_walk = 0

    screen.fill((152,209,250))

    for i in range(len(mapa_joguinho)):
        for j in range(len(mapa_joguinho[i])):
            letra = mapa_joguinho[i][j]
            if letra in tiles:
                coluna, linha = tiles[letra]
                screen.blit(tileset, (j * tile_size_joguinho, i * tile_size_joguinho), (coluna * tile_size_joguinho, linha * tile_size_joguinho, tile_size_joguinho, tile_size_joguinho))

    if direçao == "esquerda":
        screen.blit(Walk, (pos_x - monstro_x_esquerda, pos_y - monstro_y), (96*curr_frame_walk, 0, 96, 96))
    else:
        screen.blit(Walk_espelho, (pos_x - monstro_x_direita, pos_y - monstro_y), (96*(5 - curr_frame_walk), 0, 96, 96))
    if mostrar_colliders:
        pygame.draw.rect(screen, (0,0,255), collider_jogador,2)
        for collider in colliders:
            pygame.draw.rect(screen,(0, 0, 255), collider,1)
    pygame.display.update()
