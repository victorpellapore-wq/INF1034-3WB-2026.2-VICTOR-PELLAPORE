from random import choice

PALAVRAS=["cachorro","gato","elefante","girafa","tigre", "leao","macaco","pinguim","tartaruga","coelho"]
FORCA=[
    """
       _______
      |/      |
      |      (_)
      |      /|\\
      |      / \\
      |
    __|__
    """,
    """
       _______
      |/      |
      |      (_)
      |      /|\\
      |      /
      |
    __|__
    """,
    """
       _______
      |/      |
      |      (_)
      |      /|\\
      |
      |
    __|__
    """,
    """
       _______
      |/      |
      |      (_)
      |      /|
      |
      |
    __|__
    """,
    """
       _______
      |/      |
      |      (_)
      |       |
      |
      |
    __|__
    """,
    """
       _______
      |/      |
      |      (_)
      |
      |
      |
    __|__
    """,
    """
       _______
      |/      |
      |
      |
      |
      |
    __|__
    """
]


def escolher_palavra():
    return choice(PALAVRAS)

def mostrar_palavra(palavra, letras_acertadas):
    resultado = ""
    for letra in palavra:
        if letra in letras_acertadas:
            resultado+=letra + " "
        else:
            resultado+= "_ "
    return resultado.strip()

def validar_entrada(entrada):
    return entrada.isalpha()

def jogar():
    palavra=escolher_palavra()
    vidas=6
    letras_acertadas=set()
    letras_tentadas =set()
    print("\n" + "="*40)
    print("          JOGO DA FORCA")
    print("="*40)
    print("Tema: ANIMAIS")
    print("Você possui 6 vidas.")
    print("Digite uma letra ou tente adivinhar a palavra inteira.")
    print("=" * 40)
    while vidas > 0:
        print(FORCA[6 - vidas])
        print(f"\nVidas restantes: {vidas}")
        print(f"Palavra: {mostrar_palavra(palavra, letras_acertadas)}")
        if letras_tentadas:
            print("Letras já tentadas:", " ".join(sorted(letras_tentadas)))
        entrada = input("\nDigite uma letra ou a palavra: ").strip()
        if not entrada:
            print("❌ Entrada vazia! Digite uma letra ou uma palavra.")
            continue
        if not validar_entrada(entrada):
            print("❌ Entrada inválida! Digite SOMENTE LETRAS.")
            continue
        if len(entrada) > 1:
            if entrada == palavra:
                print("\n🎉 PARABÉNS! Você acertou a palavra!")
                print(f"A palavra era: {palavra}")
                return
            else:
                vidas -= 1
                print("\n❌ Palavra incorreta!")
                print("Você perdeu 1 vida.")
        else:
            letra = entrada
            if letra in letras_tentadas:
                print("⚠️ Você já tentou essa letra!")
                continue
            letras_tentadas.add(letra)
            if letra in palavra:
                letras_acertadas.add(letra)
                print("✅ Boa! A letra está na palavra.")
            else:
                vidas -= 1
                print("❌ Essa letra não está na palavra.")
        if all(letra in letras_acertadas for letra in palavra):
            print("\n🎉 PARABÉNS! Você descobriu a palavra!")
            print(f"A palavra era: {palavra}")
            print("🏆 Você venceu! +100 XP")
            return
    print(FORCA[6])
    print("\n💀 GAME OVER!")
    print(f"A palavra era: {palavra}")
    print("Você perdeu todas as 6 vidas.")
    print("XP: 0")


def main():
    while True:
        jogar()
        print("\n" + "=" * 40)
        resposta = input("Deseja jogar novamente? (s/n): ").strip().lower()
        while resposta not in ("s", "n"):
            print("❌ Digite apenas 's' para sim ou 'n' para não.")
            resposta=input("Deseja jogar novamente? (s/n): ").strip().lower()
        if resposta == "n":
            print("\nObrigado por jogar! 👋")
            break

if __name__ == "__main__":
    main()