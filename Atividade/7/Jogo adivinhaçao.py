import random

numero_secreto= random.randint(1, 1023)
tentativas=0
minimum=1
maximum=1023

print ("\n")
print ("Escolhe quem vai adivinhar !")
print("="*40)
print ("\n")
resposta = input("Quem adivinha ? (eu/voce) : ")

while True:
    if resposta == "eu" :
        proposiçao = int(input("Adivinha o numero : "))
        tentativas+= 1
        if numero_secreto > proposiçao:
            print(1)
        elif numero_secreto < proposiçao:
            print(-1)
        else:
            print(0)
            print("Numro de tentativas :", tentativas)
            break
    elif resposta == "voce":
        proposiçao = (minimum + maximum)// 2
        print("Eu proponho :", proposiçao)
        resposta_numero =int(input("1 = mais grande, -1 = mais pequeno, 0 = encontrado ! : "))
        tentativas+= 1
        if resposta_numero == 1:
            minimum = proposiçao+ 1
        elif resposta_numero == -1:
            maximum = proposiçao-1
        elif resposta_numero == 0:
            print("Encontrei !")
            print("Numero de tentativas :", tentativas)
            break