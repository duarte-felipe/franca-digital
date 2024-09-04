
#primeiro codigo em python no franca digital!!!!!!!!!!!!!!!!!!!!!!!!!!!

#primeiro importo random para fazer o jogo funcioar sem bugs 
import random
from sys import exit
#abro uma funçao de advinhaçao e logo em seguida prints para "enfeitar" o jogo
def adivinhacao():
    print("Bem-vindo ao meu jogo de adivinhação!" )
    print("Escreva um número entre 1 a 100 e descubra qual o correto!!")

#uma variavel com random para funiconar so ate o numero 100
    num = random.randint(1, 100)
    trys = 0

#
    while True:
       # if(trys == 2):,

          #  exit

        try:
            palpite = int(input("Digite seu palpite: "))
            trys += 1

            if palpite < num:
                print("O número é maior que isso.")
            elif palpite > num:
                print("O número é menor que isso.")
            else:
                print(f"Parabéns voce adivinhou! O número é '{num}' e voce usou '{trys}' tentativas.")
                break
        except ValueError:
            print("Por favor, digite um número válido.")

if __name__ == "__main__":
    adivinhacao()
