#Importação de módulo
import os # comandos do terminal
import forca
import adivinhacao
import adivinhacao
os.system("cls")
print("*************************************************")
print("****************Escolha seu jogo!****************")
print("*************************************************")

print("       (1) Forca          (2) Adivinhação")

jogo = int(input("Qual jogo?"))

if(jogo == 1):
    forca.jogar()
elif(jogo == 2):
    adivinhacao.jogar()
else:
    print("Opção inválida")


print("")
print("*************************************************")
print("******************Fim do Jogo!*******************")
print("*************************************************")