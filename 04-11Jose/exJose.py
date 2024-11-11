#escreva um algoritimo q a partir de um mes fornecido (1 a 12) mostre o nome do mes.

print("vamos começar a aula!")


def nome_do_mes(mes): #funcao para todos meses
    meses = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
    }
    
    return meses.get(mes, "Mês inválido")

# Solicita ao usuário um mês
mes_input = int(input("Digite um número de 1 a 12 que te falarei que mes esse numero representa: "))
print(nome_do_mes(mes_input))


#Crie um menu com o comando 'escolha' para executar uma das 4 opçoes ou sair do programa

print("exercicio 2")

def main(): #funcao true para todas opcoes
    while True:
        print("\nMenu:")
        print("1. Opção 1")
        print("2. Opção 2")
        print("3. Opção 3")
        print("4. Opção 4")
        print("5. Sair")

        escolha = input("Escolha uma opção (1-5): ")

        if escolha == '1':
            print("Você escolheu a Opção 1.")
        elif escolha == '2':
            print("Você escolheu a Opção 2.")
        elif escolha == '3':
            print("Você escolheu a Opção 3.")
        elif escolha == '4':
            print("Você escolheu a Opção 4.")
        elif escolha == '5':
            print("Saindo do programa.")
            break #eu poderia ter usado um 
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()


#3 crie uma calculadora

print("Exercicio 3")
print("Diga um numero e a forma q o quer soma-lo")
def calculadora():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, digite um número válido.") #em caso de erro
        return

    operacao = input("Escolha a operação (+, -, *, /): ") #escolher a operaçao desejada

   #if e else em todas as operaçoes
    if operacao == '+': 
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Divisão por zero não é permitida.")
            return
    else:
        print("Operação inválida.")
        return

    print("O resultado é:", resultado)

calculadora() #chamada de funçao


#exercicios for in, while

num = 5 #numeros do contador 
#quantas vezes sera repetido
cont = 1

while cont <= 10: #enquanto o contador for = ou menor que 10 ele vai continuar contando
    resultado = num * cont #variavel para a conta
    print(f"{num} x {cont} = {resultado}")
    cont += 1 #sempre vai adc +1

    num = int(input("Digite um número para ver sua tabuada: ")) #input padrao

for cont in range(1, 11):
    resultado = num * cont
    print(f"{num} x {cont} = {resultado}")