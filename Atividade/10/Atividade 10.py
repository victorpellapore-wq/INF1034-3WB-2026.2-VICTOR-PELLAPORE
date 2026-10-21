import pygame, sys
from pygame.locals import QUIT
from random import randint

# primera lista de números aleatórios
nums = [
    randint(0, 100) for a in range(50)
]
num_cat = 10
num_min = min(nums)
num_max = max(nums)
tam_cat = (num_max - num_min) / num_cat
lista_total = [0] * num_cat


def contabiliza_totais(nums, lista_total):
    # Para cada número na minha lista
    for i in range(len(nums)):
        if nums[i] == num_max:
            lista_total[-1] += 1
            continue

        for i_cat in range(num_cat):
            lim_inf = num_min + i_cat * tam_cat
            lim_sup = lim_inf + tam_cat

            if lim_inf <= nums[i] < lim_sup:
                lista_total[i_cat] += 1
                break
    return lista_total


print(contabiliza_totais(nums, lista_total))


def draw1(screen):
    screen_h = screen.get_height()
    for i in range(len(lista_total)):
        x = 100 + i * 50
        h = 20 * lista_total[i]
        pygame.draw.rect(screen, (255, 0, 0), (x, screen_h - h - 80, 25, h))


def eixos (screen):
    screen_h = screen.get_height()
    pygame.draw.line(screen, ("white"), (75, screen_h - 80), (575, screen_h - 80), 2)
    pygame.draw.line(screen, ("white"), (75, screen_h - 80), (75, 20), 2)

    police = pygame.font.SysFont("Arial", 15)

    for i in range(num_cat):
        x = 100 + i * 50
        pygame.draw.line(screen, ("white"), (x, screen_h - 85), (x, screen_h - 75), 2)
        text = police.render(str(i + 1), True, ("white"))
        screen.blit(text, (x - 5, screen_h - 70))
    for i in range(1, num_cat + 1):
        y = screen_h - 80 - i * 20
        pygame.draw.line(screen, ("white"), (70, y), (80, y), 2)
        text1 = police.render(str(i), True, ("white"))
        screen.blit(text1, (50, y - 5))




pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Hello World!')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    eixos(screen)
    draw1(screen)
    pygame.display.update()