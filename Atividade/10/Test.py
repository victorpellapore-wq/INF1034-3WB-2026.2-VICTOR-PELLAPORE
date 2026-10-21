import pygame, sys
from pygame.locals import QUIT
from random import randint


num_cat = 4
texte = ""          # o que o usuário está digitando
modo = "digitar"    # "digitar" ou "histograma"


def contabiliza_totais(nums, lista_total):
    # Para cada número na minha lista
    for i in range(len(nums)):
        if nums[i] == num_max:
            lista_total[-1] += 1
            continue

        # Para cada faixa/categoria
        for i_cat in range(num_cat):
            # Obtém os limites inferior e superior
            lim_inf = num_min + i_cat * tam_cat
            lim_sup = lim_inf + tam_cat

            # Checa em qual faixa/categoria o número está com base nesses limites
            if lim_inf <= nums[i] < lim_sup:
                lista_total[i_cat] += 1
                break
    return lista_total


def nums_validate(numeros):
    try:
        nums = [int(x) for x in numeros.split()]
        return nums
    except ValueError:
        return []


def draw(screen):
    screen_h = screen.get_height()
    for i in range(len(lista_total)):
        x = 100 + i * 50
        h = 20 * lista_total[i]
        pygame.draw.rect(screen, (255, 0, 0), (x, screen_h - h - 80, 25, h))


def draw_caixa(screen):
    screen.blit(police.render("Digite números separados por espaços :", True, "white"), (50, 200))
    pygame.draw.rect(screen, "white", (50, 260, 700, 50), 3)
    screen.blit(police.render(texte, True, "white"), (60, 265))


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World!')
police = pygame.font.SysFont("Arial", 32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and modo == "digitar":
            if event.key == pygame.K_BACKSPACE:
                texte = texte[:-1]
            elif event.key == pygame.K_RETURN:
                nums = nums_validate(texte)
                if nums:  # lista válida -> calcula o histograma
                    num_min = min(nums)
                    num_max = max(nums)
                    tam_cat = (num_max - num_min) / num_cat
                    lista_total = contabiliza_totais(nums, [0] * num_cat)
                    print(lista_total)
                    modo = "histograma"
                else:     # entrada inválida -> apaga e recomeça
                    texte = ""
            else:
                texte += event.unicode

    screen.fill("black")  # apaga o quadro anterior
    if modo == "digitar":
        draw_caixa(screen)
    else:
        draw(screen)
    pygame.display.update()
