import pygame, sys
from pygame.locals import QUIT
from random import randint

# Funcoes Gerais
def eixos (screen):
    screen_h = screen.get_height()
    pygame.draw.line(screen, ("white"), (75, screen_h - 80), (575, screen_h - 80), 2)
    pygame.draw.line(screen, ("white"), (75, screen_h - 80), (75, 20), 2)

    police = pygame.font.Font(None, 25)

    for i in range(num_cat):
        x = 100 + i * 50
        pygame.draw.line(screen, ("white"), (x, screen_h - 85), (x, screen_h - 75), 2)
        text = police.render(f"{num_min + i * tam_cat:.1f}", True, ("white"))
        screen.blit(text, (x - 5, screen_h - 70))
    for i in range(21):
        y = screen_h - 80 - i * 20
        pygame.draw.line(screen, ("white"), (70, y), (80, y), 2)
        text1 = police.render(str(i), True, ("white"))
        screen.blit(text1, (50, y - 5))

num_cat = 5

def random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))
cores = [random_color() for i in range(num_cat)]

#aqui o programa cria uma caixa para excrever os numeros ecolhidos pelo utilisator
texte =""
#esa variavel permite saber se o programa mostra a caixa para os numeros ou o histograma
pantalha_histograma = False
def desenhar_caixa(screen):
    screen.blit(police.render("Digite os números separados por espaços :", True, "white"), (50, 200))
    pygame.draw.rect(screen, "white", (50, 260, 700, 50), 3)
    screen.blit(police.render(texte, True, "white"), (60, 265))

#esa parte permite verificar se as informaoes entradas sao numeros
def digit_numeros(numeros):
    if len(numeros) == 0:
        return False
    for a in numeros:
        if not a.isnumeric():
            return False
    return True


def contabiliza_totais(nums, lista_total):
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

def draw1(screen):
    screen_h = screen.get_height()
    for i in range(len(lista_total)):
        x = 100 + i * 50
        h = 20 * lista_total[i]
        pygame.draw.rect(screen, cores[i], (x, screen_h - h - 80, 25, h))



pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Os melhores histogramas!')

police = pygame.font.SysFont("Arial", 40)
#mostra ao utilisador que fazer
screen.blit(police.render("Digite números separados por espaços :", True, "White"), (200,400))
pygame.draw.rect(screen, "white", (200, 500, 600, 50), 3)

#usei a mesma estructura daquela usada para a atividade 8 (login/email)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                texte = texte[:-1]
            elif event.key == pygame.K_RETURN:
                #aqui separo os numeros
                nums = texte.split()
                #aqui e a introducao das variaveis
                if digit_numeros(nums):
                    nums = [int(x) for x in nums]
                    num_min = min(nums)
                    num_max = max(nums)
                    tam_cat = (num_max - num_min) / num_cat
                    lista_total = [0] * num_cat
                    contabiliza_totais(nums, lista_total)
                    pantalha_histograma = True
                else:
                    texte = ""
            else:
                texte += event.unicode
    #uma vez que o utilisator escolheu o seus numeros, podemos mostrar a pantlha do histograma
    if pantalha_histograma == True:
        eixos(screen)
        draw1(screen)
    else :
        desenhar_caixa(screen)
    pygame.display.update()