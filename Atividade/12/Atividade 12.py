import pygame, sys, os
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((896, 640)) #14 x10 tiles de 64 px
pygame.display.set_caption('Hello World!')
clock = pygame.time.Clock()
tile_size = 60
tile_size_joguinho = 64
pasta_do_script = os.path.dirname(os.path.abspath(__file__))
tileset = pygame.image.load(os.path.join(pasta_do_script, "tileset_neige_5x5.png"))
collider_caixa = pygame.Rect(0, 0, 0, 0)
can_walk = True

pos_x = 0
pos_y = 0

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
  "VXXXQUWXYQUUUU",
  "GDOXXHXXYFHHJM",
  "TTDZXXXXYBSSJM",
  "TTTDNNNEGGGGGG",
  "TTTRAAALTTTTTT",
  "TTTRPPPLTTTTTT",
]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(60)
    dt = clock.get_time()

    old_pos_x = pos_x
    old_pos_y = pos_y

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        pos_x = pos_x + 0.1*dt
    elif keys[pygame.K_LEFT]:
        pos_x = pos_x - 0.1*dt
    elif keys[pygame.K_UP]:
        pos_y = pos_y - 0.1*dt
    elif keys[pygame.K_DOWN]:
        pos_y = pos_y + 0.1*dt

    screen.fill((152,209,250))

    collider_jogador = pygame.Rect(pos_x, pos_y, 64, 64)

    if collider_jogador.colliderect(collider_caixa):
        pos_x = old_pos_x
        pos_y = old_pos_y

    pygame.draw.rect(screen, (255, 0, 0), (pos_x, pos_y, 64, 64))
    pygame.draw.rect(screen, (0, 0, 255), collider_jogador, 2)
    
    for i in range(len(mapa_joguinho)): # Para cada linha
        for j in range(len(mapa_joguinho[i])): # Para cada coluna (letra)
            letra = mapa_joguinho[i][j]
            if letra in tiles:
                coluna, linha = tiles[letra]
                screen.blit(tileset, (j * tile_size_joguinho, i * tile_size_joguinho), (coluna * tile_size_joguinho, linha * tile_size_joguinho, tile_size_joguinho, tile_size_joguinho))
            if letra == "B":
                collider_caixa = pygame.Rect(j * tile_size_joguinho, i * tile_size_joguinho, 64, 64)
                pygame.draw.rect(screen, (0, 0, 255), collider_caixa, 2)
    

    pygame.display.update()