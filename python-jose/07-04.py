#bom dia 

'''voce = input("Me diga, VOCE È GAY? ")    #para começar o dia bem :)

if voce == "nao":
    print("VOCE ESTA MENTINDOO.")
else:
    print("UE...?????") '''


#licao1
def verificar_positivo(numero):
    if numero > 0:
        print("O número é positivo.")
    else:
        print("O número não é positivo.")
numero = int(input("Digite um número: "))
verificar_positivo(numero)

#licao2
def verificar_par_impar(numero):
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
numero = int(input("Digite um número: "))
verificar_par_impar(numero)

#licao3
def ordem_decrescente(valor1, valor2):
    if valor1 > valor2:
        print(f"{valor1} > {valor2}")
    elif valor2 > valor1:
        print(f"{valor2} > {valor1}")
    else:
        print("Os valores são iguais!")
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
ordem_decrescente(valor1, valor2)



#tabuada
num1= int(input("Digite um numero: "))
tabuada=[num1*1,num1*2,num1*3,num1*4,num1*5,num1*6,num1*7,num1*8,num1*9,num1*10]
for num1 in tabuada:
    print(num1)
