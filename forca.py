# -*- coding: utf-8 -*-
#Importação de módulo
import os # comandos do terminal
import random # módulo de números pseudo aleatórios
import unicodedata  #retirar acentos das palavras

#########################################################################################################
def jogar(): # criando uma função para o jogo criado
    os.system("cls")
    msg_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    boneco(0)
    enforcou = False
    acertou = False
    erros = 0

    # enquanto não acabou as chances e não acertou a palavra
    #while(true)
    while(not enforcou and not acertou):
        chute = pede_chute()
        palavra_secreta_sem_acento = remove_non_ascii_normalized(palavra_secreta)

        if(chute in palavra_secreta_sem_acento):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta,palavra_secreta_sem_acento )
        else:
            erros+=1
            boneco(erros)
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("ganhou")
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
#########################################################################################################
def boneco(qtdErros):
    #os.system("cls")
    if   (qtdErros == 0):
        print("\n           _________  \n          |         | \n          |           \n          |           \n          |           \n          |           \n          |           \n          |           \n          |           \n _________|_________  \n|                   | \n\n")
    elif (qtdErros == 1):
        print("\n           _________  \n          |         | \n          |         O \n          |           \n          |           \n          |           \n          |           \n          |           \n          |           \n _________|_________  \n|                   | \n\n")
    elif (qtdErros == 2):
        print("\n           _________  \n          |         | \n          |         O \n          |         | \n          |         | \n          |           \n          |           \n          |           \n          |           \n _________|_________  \n|                   | \n\n")
    elif (qtdErros == 3):
        print("\n           _________  \n          |         | \n          |         O \n          |        /| \n          |         | \n          |           \n          |           \n          |           \n          |           \n _________|_________  \n|                   | \n\n")
    elif (qtdErros == 4):
        print("\n           _________   \n          |         |  \n          |         O  \n          |        /|\ \n          |         |  \n          |            \n          |            \n          |            \n          |            \n _________|_________   \n|                   |  \n\n")
    elif (qtdErros == 5):
        print("\n           _________   \n          |         |  \n          |         O  \n          |        /|\ \n          |         |  \n          |        /   \n          |            \n          |            \n          |            \n _________|_________   \n|                   |  \n\n")
    elif (qtdErros == 6):
        print("\n           _________   \n          |         |  \n          |         O  \n          |        /|\ \n          |         |  \n          |        / \ \n          |            \n          |            \n          |            \n _________|_________   \n|                   |  \n  G A M E   O V E R\n")

def msg_abertura():
    print("*************************************************")
    print("***********Bem vindo ao jogo da Forca!***********")
    print("*************************************************")

def carrega_palavra_secreta():
    palavra = []  # inicializando a lista
    with open("palavras.txt",encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavra.append(linha)
    numero = random.randrange(0, len(palavra))
    palavra_secreta = palavra[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra? ")
    chute = remove_non_ascii_normalized(chute.strip().upper())
    return chute

def marca_chute_correto( chute, letras_acertadas, palavra_secreta,palavra_secreta_sem_acento ):
    index = 0
    for letra in palavra_secreta_sem_acento:
        if (chute == letra):
            # letras_acertadas[index] = letra
            letras_acertadas[index] = palavra_secreta[index]
        index += 1

#função de retirada de luizomf/remove_accents.py (github)
#https://gist.github.com/luizomf/54b58615cd674db44153470c369a8284.js
def remove_non_ascii_normalized(string: str) -> str:
    normalized = unicodedata.normalize('NFD', string)
    return normalized.encode('ascii', 'ignore').decode('utf8').casefold()

def imprime_mensagem_vencedor():
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

def imprime_mensagem_perdedor(palavra_secreta):
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))


#para jogar o jogo sem precisar do menu
# e não executar só pela importação no menu
if(__name__ == "__main__"):
    jogar()
