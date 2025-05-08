import os
os.system("cls")
#ESTRUTURAS CONDICIONAIS IF ELSE (ELIF)
#SWITCH CASE -> (match case) escolha caso (a partir da versão 3.10)
#match valor:
#case valor:


# linguagem = 100

# match linguagem:

#     case "python":
#         print("é fácil")
#     case "java":
#         print("muito código, python faz com linhas menores")    
#     case "c#":
#         print("massa")
#     case "js":
#         print("sou do back")    
#     case "html":
#         print("não dorme")
#     case 10: 
#         print("entrou aqui!") 
#     case _:
#         print("outro caso")       


# dia = int(input("digite um número de 1 a 7:"))

# match dia:

#     case 1:
#         print("segunda")
#     case 2:
#         print("terça")
#     case 3:
#         print("quarta")
#     case 4:
#         print("quinta")
#     case 5:
#         print("sexta")
#     case 6:
#         print("sábado")
#     case 7:
#         print("domingo")


# print("*"*10, "MUNDO DO CELULAR", "*"*10)
# print("""
# 1- IPHONE 15 - R$5000,00     
# 2- XIAOMI REDMI 13 PRO PLUS 512GB - R$2500,00     
# 3- SAMSUNG S25 265 GB - R$6999,99      
# FRETE: SP -> R$10,00
#        MG -> R$15,00
#        RS -> R$20,00
# """)
# produto = int(input("digite o número do produto:"))
# estado = input("digite a sigla do estado:").upper()
# print("*"*40)

# frete = ""
# celular = ""

# match produto:
#     case 1:
#         celular = 5000.00 
#     case 2:
#         celular = 2500.00 
#     case 3:
#         celular = 6999.99 

# match estado:
#     case "SP":
#         frete = 10 
#     case "MG":
#         frete = 15                  
#     case "RS":
#         frete = 20


# print(f"PREÇO: R${celular}")
# print(f"FRETE: R${frete}")
# print(f"TOTAL: R${celular+frete}")


#atividade pedra papel tesoura
# import random

# valor = 0
#randint(valorinicial,valorfinal)
# valor = random.randint(0,100) #gera de 1 ate 99 aleatoriamente

# match valor:

#     case _ if valor <50 : 
#         print("menor que 50")
#     case _ if valor ==50:
#         print("= 50")
#     case _ if valor > 50:
#         print("maior que 50")

# import random
# maquina = random.randint(1,3) 
print("JOGO PEDRA PAPEL TESOURA")

papel = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

pedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


tesoura = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

jogador = input("digite pedra ou papel ou tesoura: ").lower()

import random
maquina = random.randint(1,3) 
match maquina:
    case _ if maquina == 1:
        print(f"Máquina: pedra {pedra}")
    case _ if maquina == 2:
        print(f"Máquina: papel {papel}")
    case _ if maquina == 3:
        print(f"Máquina: tesoura {tesoura}")    

match jogador: 
    case _ if jogador == "pedra":
        print(f"Você: pedra {pedra}")
    case _ if jogador == "papel":
        print(f"Você: papel {papel}")   
    case _ if jogador == "tesoura":
        print(f"Você: tesoura {tesoura}")  

match jogador:
    case _ if jogador == "pedra" and maquina == 1: 
        print("EMPATE!")
    case _ if jogador == "pedra" and maquina == 3:
        print("GANHOU!")
    case _ if jogador == "pedra" and maquina == 2:
        print("PERDEU!")
    case _ if jogador == "papel" and maquina == 2: 
        print("EMPATE!")
    case _ if jogador == "papel" and maquina == 3:
        print("PERDEU!")
    case _ if jogador == "papel" and maquina == 1:
        print("GANHOU!")    
    case _ if jogador == "tesoura" and maquina == 3: 
        print("EMPATE!")
    case _ if jogador == "tesoura" and maquina == 2:
        print("GANHOU!")
    case _ if jogador == "tesoura" and maquina == 1:
        print("PERDEU!")    