'''print("Esse é o cadastro padrao do nosso sistema, por favor conclua-o")

agua = float(input("Qual a profundidade da sua piscina? "))
baby = input("Voce esta com uma criança em casa? ") 


   # if agua >= 1.0:
    if baby == "sim":
        print("Voce corre risco, iremos ativar o alarme. ")
    elif "nao":
        print("Voce nao corre risco. Deseja ativar seu alarme mesmo assim?")
'''

#importei sys para ficar mais facil a pausa do programa
import sys
print("Esse é o cadastro padrão do nosso sistema, por favor conclua-o") #print de começo para começar o cadastro do cliente

agua = float(input("Qual a profundidade da sua piscina?: "))
baby = input("Você está com uma criança em casa? (sim/não): ").strip().lower() #.strip e .lower para nao ter confusao no python
#variaveis para saber a profundidade e se tem crianças em casa

def afogamento(agua, baby): #funçao para o codigo ficar mais resumido e funcional
    if agua >= 1.0 and baby == "sim":
        print("Você corre risco, iremos ativar o alarme.") #se a piscina for maior ou igual a 1 metro ativara o sistema automaticamente
        sys.exit() #gosto do .exit particularmente para situaçoes como essa
    elif agua >= 1.0 and baby == "nao":
        print("Você não corre risco. Deseja ativar seu alarme mesmo assim?: ") #esse elif ficou um pouco sem funçao KKKKKK
    else:
        print("A profundidade é segura.")
    
    alarme = input("Voce nao corre riscos com crianças, deseja ativa-lo mesmo assim?(sim/nao): ").strip().lower()
 #fiz uma nova variavel caso a pessoa queira ativar por outro motivo o alarme
    if alarme == "sim": 
        print("O alarme foi ativado.")
        sys.exit()
    elif alarme == "nao":
        print("Ele nao sera ativado.") 

# Chamada da função
afogamento(agua, baby)
