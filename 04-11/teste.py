'''print("Vamos começar a brincadeira... ")
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
                    print("O animal escolhido foi o Iguiá.")'''
