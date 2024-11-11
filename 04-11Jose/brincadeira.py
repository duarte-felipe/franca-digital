'''Construa um algoritmo que seja capaz de concluir qual dentre os seguintes animais foi escolhido,
 através de perguntas e respostas. Animais possíveis: Leão, cavalo, homem, macaco, morcego, baleia, avestruz,
pinguin, pato, iguia, tartaruga, crocodilo e cobra.
Exemplo: É mamifero? Sim.
É quadrúpede? Sim.
É carnívoro? Não.
É herbívoro? Sim.
Então o animal escolhido foi o cavalo.'''

#chamando a funçao e começando a 'brincadeira'
print("Vamos começar a brincadeira... ")
def brincadeira_animal():
    while True:  # vou inicia um loop que permite múltiplas tentativas em vez de apenas uma (eu tinha feito assim KK)
        # Pergunta 1: O animal é um mamífero?
        mamifero = input("O animal é um mamífero? (Sim/Não): ").strip().lower()

        if mamifero == "sim":
            # Pergunta 2: O animal é quadrúpede?
            quadrupede = input("O animal é quadrúpede? (Sim/Não): ").strip().lower()

            if quadrupede == "sim":
                # Pergunta 3: O animal é carnívoro?
                carnivoro = input("O animal é carnívoro? (Sim/Não): ").strip().lower()

                if carnivoro == "sim":
                    print("O animal escolhido foi o Leão.")
                else:
                    print("O animal escolhido foi o Cavalo.")
            else:
                # Pergunta 4: O animal voa?
                voa = input("O animal voa? (Sim/Não): ").strip().lower()

                if voa == "sim":
                    print("O animal escolhido foi o Morcego.")
                else:
                    # Pergunta para diferenciar Homem e Macaco
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
                    # pergunta para diferenciar Baleia e Crocodilo
                    mamifero_aquatico = input("O animal é mamífero? (Sim/Não): ").strip().lower()
                    if mamifero_aquatico == "sim":
                        print("O animal escolhido foi a Baleia.")
                    else:
                        print("O animal escolhido foi o Crocodilo.")
                else:
                    # pergunta para diferenciar Cobra e Tartaruga
                    casco = input("O animal tem casco? (Sim/Não): ").strip().lower()
                    if casco == "sim":
                        print("O animal escolhido foi a Tartaruga.")
                    else:
                        print("O animal escolhido foi a Cobra.")
            else:
                # Pergunta 7: O animal é uma ave?
                ave = input("O animal é uma ave? (Sim/Não): ").strip().lower()

                if ave == "sim":
                    # Pergunta 8: O animal vive em ambientes aquáticos?
                    aquatico = input("O animal vive em ambientes aquáticos? (Sim/Não): ").strip().lower()
                    if aquatico == "sim":
                        print("O animal escolhido foi o Pinguim.")
                    else:
                        # Pergunta para diferenciar Avestruz e Pato
                        voa = input("O animal voa? (Sim/Não): ").strip().lower()
                        if voa == "sim":
                            print("O animal escolhido foi o Avestruz.")
                        else:
                            print("O animal escolhido foi o Pato.")
                else:
                    # Se não é mamífero, réptil ou ave, assume que é um Iguiá
                    print("O animal escolhido foi o Iguiá ou um leão.")

        # pergunto se o usuário deseja jogar novamente
        jogar_novamente = input("Você deseja jogar novamente? (Sim/Não): ").strip().lower()
        if jogar_novamente != "sim":
            print("Obrigado por jogar!")
            break  # sai do loop se a resposta não for "sim" :(

# chamando a função para iniciar o jogo
brincadeira_animal()
