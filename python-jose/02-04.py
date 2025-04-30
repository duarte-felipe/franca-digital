#saudadeeeeeeeeeeeeeeeeeeeeeeeeeee
import math
'''b = 7
senha = "3105" 

while True:
    try:
       
        a = int(input("Digite um numero até 10, se voce acertar, ele te dirá a senha: "))
        
        if a > 10:
            print("Voce passou dos números certos.")
        elif a == b:
            print(f"Voce acertou! A senha é: {senha}")
            break  
        else:
            print("Voce errou, tente novamente.")
    
    except ValueError:
        print("Por favor, insira um número válido.")

print("Proxima etapa...")
print("Dessa vez voce vai desbloquear um cofre.")'''







#liçao 1 
num2 = float(input("DIgite o primeiro numero: "))
num3 = float(input("Digite o segundo numero: "))

#variavel pra media 
media= (num2+num3) /2

print(f"A média dos seus dois numero é: {media}")



#liçao 2
num = int(input("Digite um número: "))
suc = num + 1
ant = num - 1

print(f"O sucessor de {num} é {suc}.")
print(f"O antecessor de {num} é {ant}.")



#liçao 3 
def calculo(largura, altura):
    area = (largura*altura)
    return area 
altura = float(input("Digite a altura: "))
largura= float(input("Digite a largura: "))
print("A altura do calculo foi {altura}, a largura do calculo foi {largura} e o resultaado de sua area e de: {}".format(altura*largura))


#licao4
num = float(input("Digite um número para calcular a raiz quadrada: "))
sqrt = math.sqrt(num)
#exibir o resultado
print(f"A raiz quadrada de {num} é {sqrt}")


#licao 5 

#variavel pras notas e nome do aluno
nome= input("Digite o nome do aluno: ")
nota1 = float(input("DIgite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
 
media= (nota1+nota2) /2

#print e conclusao do ex parcialmente 
print(f"A media do aluno/a {nome} e de {media}")

#aproveitamento do aluno e agora sim conclusao total do ex
if media >= 7.0:
    print("Ele/a teve um bom aproveitamento! ")
else:
    print("Ele/a nao teve um bom apoveitamento! ")





