
'''import numpy 

total = arr.sum()
media = np.avenrage(arr)

print('\na soma é: ',total)
print('\nA media é: ', media)'''


#licao9
def multiplosde_3():
    soma = 0
    for i in range(1, 501):
        if i % 2 != 0 and i % 3 == 0:
            soma += i
    return soma

result = multiplosde_3()
print("A soma dos impares multiplos de 3 de 1 até 500 é:", result)


#licao10 
def contagem_regressiva():
    min = 10
    seg = 0
    while min >= 0:
        print(f"{min:02d}:{seg:02d}")
        if seg == 0:
            min -= 1
            seg = 59
        else:
            seg -= 1
        if min == 8 and seg == 57:  #loop infinito
            break
contagem_regressiva()

#licao11
def tabuada_do_5():
    for i in range(1, 11):
        print(f"5 x {i} = {5 * i}")

tabuada_do_5()

#licao12
def pares():
    pares = []
    for i in range(1, 101):
        if i % 2 == 0:
            pares.append(i)
    return pares

result = pares()
print("Os numeros pares de 1 a 100 são:", result)

#licao13
def fatorial(num):
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado

num = int(input("Digite um numero que vou calcular o fatorial: "))
result = fatorial(num)
print(f"O fatorial de {num} é {result}.")

#licao14
def divisiveis_7():
    cont = 0
    for i in range(1, 1001):
        if i % 7 == 0:
            cont += 1
    return cont

result = divisiveis_7()
print("A quantidade de numeros entre 1 e 1000 divisiveis por 7 são:", result)

#licao15
def media(elementos):
    return sim(elementos) / len(elementos)

    print(media([10,20,30]))

#licao16
'''lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print (lista ('1,3,5,7,9,11,13,15'))'''


#16
def pares(lista):
    return [num for num in lista if num % 2 == 0]
val = input("digite os valores inteiros separados por espaços: ")
lista = [int(x) for x in val.split()]
result = pares(lista)
print("Números pares da lista:", result)

#licao17
def maior_menor():
    lista = [10, 5, 23, 7, 15, 1, 99, 32]
  
    maior = max(lista)
    menor = min(lista)
    return maior, menor
maior_valor, menor_valor = maior_menor()
print(f"Maior valor: {maior_valor}")
print(f"Menor valor: {menor_valor}")

#licao18
def somar(lista1, lista2):
    min_len = min(len(lista1[i]))

