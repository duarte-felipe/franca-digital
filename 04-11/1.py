#escreva um algoritimo q a partir de um mes fornecido (1 a 12) mostre o nome do mes.

print("vmaos começar a aula!")


def nome_do_mes(mes):
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

def main():
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
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()


#3 crie uma calculadora

print("Diga um numero e a forma q o quer soma-lo")
def calculadora():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        return

    operacao = input("Escolha a operação (+, -, *, /): ")

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

calculadora()

'''Construa um algoritmo que seja capaz de concluir qual dentre os seguintes animais foi escolhido,
 através de perguntas e respostas. Animais possíveis: Leão, cavalo, homem, macaco, morcego, baleia, avestruz,
pinguin, pato, iguia, tartaruga, crocodilo e cobra.
Exemplo: É mamifero? Sim.
É quadrúpede? Sim.
É carnívoro? Não.
É herbívoro? Sim.
Então o animal escolhido foi o cavalo.'''

print("Vamos começar a brincadeira... ")
def trabalho_animal():
    # Pergunta 1: O animal é um mamífero?
    print("Primeira pergunta.")
    mamifero = input("O animal é um mamífero? (Sim/Não): ").strip().lower() #fiz strip e lower em quase td pra nao ter erro

    if mamifero == "sim":
        # Pergunta 2: O animal é quadrúpede?
        print("Seguuuunda pergunta")
        quadrupede = input("O animal é quadrúpede? (Sim/Não): ").strip().lower()

        if quadrupede == "sim":
            # Pergunta 3: O animal é carnívoro?
            print("terceira pergunta  :)")
            carnivoro = input("O animal é carnívoro? (Sim/Não): ").strip().lower()

            if carnivoro == "sim":
                # se o animal é mamífero, quadrúpede e carnívoro, é um Leão
                print("O animal escolhido foi o Leão.")
            else:
                # se o animal é mamífero, quadrúpede e herbívoro, é um Cavalo
                print("O animal escolhido foi o Cavalo.")
                #aqui ja matou bastantes
        else:
            # Pergunta 4: O animal voa?

            voa = input("O seu animal voa??? (Sim/Não): ").strip().lower()

            if voa == "sim":
                # se o animal é mamífero e não é quadrúpede, mas voa, é um Morcego
                print("Descobriiii, o animal escolhido foi o Morcego.")
            else:
                # Pergunta para diferenciar Homem e Macaco KKKKKKK
                ereto = input("O animal anda ereto? (Sim/Não): ").strip().lower()
                if ereto == "sim":
                    print("O animal escolhido foi o Homem.")
                else:
                    print("O animal escolhido foi o Macaco.")
    else:
        # Pergunta 5: O animal é um réptil?
        reptil = input("O animal é um réptil? (Sim/Não): ").strip().lower()

        if reptil == "sim":
            # Pergunta 6: O animal é aquático?
            aquatico = input("O animal é aquático? (Sim/Não): ").strip().lower()

            if aquatico == "sim":
                # Pergunta para diferenciar Baleia e Crocodilo
                mamifero_aquatico = input("O animal é mamífero? (Sim/Não): ").strip().lower()
                if mamifero_aquatico == "sim":
                    print("O animal escolhido foi a Baleia.")
                else:
                    print("O animal escolhido foi o Crocodilo.")
            else:
                # Pergunta para diferenciar Cobra e Tartaruga
                casco = input("O animal tem casco? (Sim/Não): ").strip().lower()
                if casco == "sim":
                    print("O animal escolhido foi a Tartaruga.")
                else:
                    print("O animal escolhido foi a Cobra.")
        else:
            # Pergunta 7: O animal voa?
            voa = input("O animal voa? (Sim/Não): ").strip().lower()

            if voa == "sim":
                # Pergunta 8: O animal vive em ambientes aquáticos?
                aquatico = input("O animal vive em ambientes aquáticos? (Sim/Não): ").strip().lower()
                if aquatico == "sim":
                    print("O animal escolhido foi o Pinguim.")
                else:
                    print("O animal escolhido foi o Avestruz.")
            else:
                # Pergunta para diferenciar Pato e Iguiá
                aquatico = input("O animal é aquático? (Sim/Não): ").strip().lower()
                if aquatico == "sim":
                    print("O animal escolhido foi o Pato.")
                else:
                    print("O animal escolhido foi o Iguiá.")

# chamou a função para iniciar o jogo
identificar_animal()
