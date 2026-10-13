import pygame

def valida_email(email):
    return email[-8:] == "@puc.com"

def possui_maiuscula(senha):
    for carac in senha:
        if 'A' <= carac <= 'Z':
            return True
    return False

def possui_minuscula(senha):
    for carac in senha:
        if 'a' <= carac <= 'z':
            return True
    return False

def possui_numero(senha):
    for carac in senha:
        if carac.isnumeric():
            return True
    return False

def valida_senha(senha):
    if len(senha) < 8:
        return False
    if not possui_maiuscula(senha):
        return False
    if not possui_minuscula(senha):
        return False
    if not possui_numero(senha):
        return False
    
    return True

def criptografa(senha):
    senha_cripto = ""
    for carac in senha:
        if carac.islower():
            pos_alpha = ord(carac) - ord('a')
            pos_alpha = (pos_alpha + 3) % 26
            pos_ascii = pos_alpha + ord('a')
            senha_cripto += chr(pos_ascii)
        elif carac.isupper():
            pos_alpha = ord(carac) - ord('A')
            pos_alpha = (pos_alpha + 3) % 26
            pos_ascii = pos_alpha + ord('A')
            senha_cripto += chr(pos_ascii)
        elif carac.isdigit():
            senha_cripto += carac
        else:
            senha_cripto += carac
    return senha_cripto

running = True

#while running:
   # print("\n" + "=" * 40)
   # email = input("Digite seu email: ")
   # while valida_email(email)==False  :
  #      print("O seu e-mail não é válido. Digite novamente!")
  #      email = input("Digite seu email: ")
  #  print("Parabéns, o seu e-mail é válido!")
  #  senha = input("Digite sua senha: ")
   # while valida_senha(senha) == False :
   #     print("A sua senha não é válida. Digite novamente!")
  #      senha = input("Digite sua senha: ")
   # print("Parabéns, a sua senha é válida!")
   # print("\n" + "=" * 40)
  #  print("A criptografia de César da sua senha é", criptografa(senha))


## Configurar e utilizar o pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Login")

running = True

input_string = ""
input_string1 = ""
input_string2 = ""
champ_actif = "input_string1"
valid_email = False
pressed_enter = False
fonte = pygame.font.Font(size=50)
fonte_validation = pygame.font.Font(size=25)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if champ_actif == "input_string1":
                    input_string1 = input_string1[:-1]
                else:
                    input_string2 = input_string2[:-1]
            elif event.key == pygame.K_RETURN:
                if champ_actif == "input_string1":
                    valid_email = valida_email(input_string1)
                    if valid_email:
                        champ_actif = "input_string2"
                        pressed_enter = False
                    else:
                        pressed_enter = True
                else:
                    valid_senha = valida_senha(input_string2)
                    pressed_enter = True
            else:
                if champ_actif == "input_string1":
                    input_string1 += event.unicode
                else:
                    input_string2 += event.unicode

    screen.fill("white")
    pygame.draw.rect(screen, "black", (400, 300, 500, 50), 3)
    pygame.draw.rect(screen, "black", (400, 425, 500, 50), 3)
    input_text1 = fonte.render(input_string1, True, "#000000")
    input_text2 = fonte.render(input_string2, True, "#000000")
    
    title_font = pygame.font.Font(None, 48)
    font = pygame.font.Font(None, 32)
    titre = title_font.render("Login", True, "black")
    screen.blit(titre, (600, 150))

    screen.blit(font.render("Email:", True, "black"), (400, 275))
    screen.blit(font.render("Senha:", True, "black"), (400, 400))

    screen.blit(input_text1, (420, 305))
    senha_oculta = "*" * len(input_string2)
    screen.blit(font.render(senha_oculta, True, "black"), (420, 440))

    if pressed_enter:
        if valid_email:
            valid_text = fonte_validation.render("Parabéns, o seu e-mail é válido!", True, "green")
            screen.blit(valid_text, (400, 360))
            if valid_senha:
                    valid_text = fonte_validation.render("Parabéns, a sua senha é válida!", True, "green")
                    screen.blit(valid_text, (400, 485))
                    if valid_email and valid_senha:
                        senha_cripto = criptografa(input_string2)
                        valid_text = fonte_validation.render(f"A criptografia de César da sua senha é: {senha_cripto}", True, "blue")
                        screen.blit(valid_text, (400, 520))
            else:
                valid_text = fonte_validation.render("A sua senha não é válida. Digite novamente!", True, "red")
                screen.blit(valid_text, (400, 485))

        else:
            valid_text = fonte_validation.render("O seu e-mail não é válido. Digite novamente!", True, "red")
            screen.blit(valid_text, (400, 360))
        
    pygame.display.update()
    