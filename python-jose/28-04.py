#licao 19
def nome(lista, nome):
    return nome in lista

nomes = input("Digite os nomes separados por espaço: ").split()
busca = input("Digite o nome a buscar: ")

resultado = nome(nomes, busca)
print("O nome existe na lista?", resultado)


#licao20
def quadrados(lista):
    return [x**2 for x in lista]


#licao21
def multiplos(lista):
    return sum(1 for x in lista if x % 3 == 0 and x % 5 == 0)


#licao22
def indices(lista, alvo):
    return [i for i, x in enumerate(lista) if x == alvo]


#licao23
def letras(texto):
    return [letra for letra in texto if not letra.isspace()]


#licao 24
def vogais(texto):
    vogais = 'aeiouAEIOU'
    cont = sum(1 for letra in texto if letra in vogais)
    return cont

print(vogais("DUARTEE"))

#licao 25
def nomes(lista_nomes):
    return [nome for nome in lista_nomes if len(nome) > 5]

print(nomes(["Marco", "Felipe", "Eduardo", "rodolfo"]))

#licao 26
def inverter(text):
    return text[::-1]

print(inverter_string("MARCO"))

#licao 27
def lista(palavras):
    return [palavra for palavra in palavras if palavra.lower().startswith('lista')]

print(lista(["maristela", "abobora", "america", "corona", "ferrari"]))

#licao 28
def media(num):
    if not num:
        return 0
    return sum(lista_numeros) / len(num)

print(media([10, 20, 30, 40]))

#licao 29
def elementos(lista1, lista2):
    return list(set(lista1) & set(lista2))

print(elementos([1, 2, 3, 4], [3, 4, 5, 6]))