import random

def jogar():
    mensagem_abertura()
    palavra_secreta = pega_palavras()

    letras_acertadas = inicializa_palavras(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    

    while(not enforcou and not acertou):

        chute = input_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        ganhou()
    else:
        perdeu(palavra_secreta)
    print("Fim de jogo")







def mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def pega_palavras():
    arquivo = open("jogo/arquivo.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_palavras(palavra):
    return ["_" for letra in palavra]

def input_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1

def ganhou():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def perdeu(palavra_secreta):
    print("Você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("     _______________      ")
    print("    /               \     ")
    print("   /                 \    ")
    print("/\/                   \/\ ")
    print("\ |   XXXX     XXXX   | / ")
    print(" \|  XXXXXX   XXXXXX  |/  ")
    print("  |   XXXX     XXXX   |   ")
    print("  |                   |   ")
    print("  \__      XXX      __/   ")
    print("    |\     XXX     /|     ")
    print("    | |           | |     ")
    print("    | I I I I I I I |     ")
    print("    |  I I I I I I  |     ")
    print("     \_           _/      ")
    print("       \_________/        ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()