#Importação de módulo
import random
import os # comandos do terminal

def jogar():
    os.system("cls")
    print("*************************************************")
    print("********Bem vindo ao jogo de adivinhação!********")
    print("*************************************************")

    #atribuindo o número secreto
    numero_secreto= random.randrange(1,101)
    #a função random.random() gera valores pseudo aleatórios entre 0 e 1
    #random.randrange(1,101) : números aleatórios entre 1 e 100
    total_de_tentativas = 0
    pontos = 1000

    # print para verificar o número
    #print(numero_secreto)

    #atribuindo a quantidade de tentativas de acordo com o nível escolhido pelo usuário
    #print("*************************************************")
    print("************* Níveis de Dificuldade *************")
    print("  (1) Fácil        (2) Médio        (3) Difícil")
    print("*************************************************")

    nivel = int(input("Defina o nível de dificuldade: "))

    if(nivel   == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    elif(nivel == 3):
        total_de_tentativas = 5
    else:
        print("Valor inválido!")

    #laço de tentativas
    for rodada in range(1,total_de_tentativas+1):
        #print("\nTentativa ", rodada, " de ", total_de_tentativas, ".\n", sep='')
        #interpolação de string

        print("\nTentativa {} de {}".format(rodada, total_de_tentativas))
        # Input do usuário com o chute
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou ", chute)

        if(chute< 1 or chute > 100 ):
            print("Você deve digitar um número entre 1 e 100!")
            continue # sai da iteração

        #condições
        acertou = chute == numero_secreto
        maior   = chute >  numero_secreto
        menor   = chute <  numero_secreto

        #verificando e informando para o usuário se ele acertou ou errou
        # no caso do erro, é informado se o número chutado é menor ou maior que o número secreto
        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break # sai do laço
        elif(maior):
            print("Você errou!")
            print("O seu chute foi maior que o número secreto")
        else:
            print("Você errou.")
            print("O seu chute foi menor que o número secreto")
        pontos_perdidos = abs(numero_secreto - chute) #valor absoluta da diferença entre o número secreto e o chute
        pontos -=pontos_perdidos
        if(rodada == total_de_tentativas):
            print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))
        print("Você tem mais", total_de_tentativas - rodada, "tentativa(s)")
if(__name__ == "__main__"):
    jogar()