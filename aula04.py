#aula 04 -> ESTRUTURA CONDICIONAL IF ELSE (se senao) -> True or False (Verdadeiro ou Falso)
#OPERADORES CONDICIONAIS:  > >= < <= != == and or
# > (maior)
# >= ( maior OU igual)
# < (menor)
# <= (menor OU igual)
# == (igual) 
# != (diferente)
# and (e) -> Se apenas uma ou mais condiçoes for FALSA ele retorna FALSE 
# or (ou) -> Se apenas uma ou mais condições for VERDADE ele retorna TRUE

#if condicao :
# print("verdade")
#else: 
#print("falso")

# A IDENTAÇÃO (ESPAÇO) deve ser utilizado o TAB

# import os
# os.system("cls")

# x=10  
# if x > 1000:
#     print("verdade")
# else:
#     print("falso")

# nome = "teste"
# if "testee" != nome:
#     print(1)
# else:
#     print(2)

#atividade 1:
# idade = int(input("informe sua idade: "))
# if idade >= 18:
#     print("USUÁRIO AUTENTICADO")
# else:
#     print("USUÁRIO INVALIDO, MENOR DE IDADE")


#atividade 2:
# idade = float(input("informe sua idade: "))
# if idade >= 18 and idade < 120:
#     print("USUÁRIO AUTENTICADO")
# else: 
#     if idade >= 0 and idade <= 18:        
#         print("USUÁRIO INVALIDO, MENOR DE IDADE")
#     else:
#         print("USUÁRIO INVALIDO, MAIOR DE 120")


#atividade 3:
# print("*"*10, "CADASTRO", "*"*10 )
# email = input("digite seu email: ")
# senha = int(input("digite sua senha: "))
# if email == "python@senai.com" and senha == 12345678:
#     print("USUÁRIO AUTENTICADO")
# else:
#     print("USUÁRIO OU SENHA INVALIDOS")

#atividade 4:
# print("*"*10, "LOJA DE MAÇÃS", "*"*10)
# print("R$: 0.30: menos de uma duzia")
# print("R$: 0.25: pelo menos doze")

# quantia = int(input("\ndigite a quantidade de maças que deseja levar: "))
# if quantia <12:
#     print(f"{quantia} maças: R$0.30 unidade, TOTAL = R$ {quantia*0.30}")
# else: 
#     print(f"{quantia} maças: R$0.25 unidade, TOTAL = R$ {quantia*0.25}")

# #atividade 1: 
# letra = input("digite uma letra: ")
# if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
#     print("você digitou uma vogal!")
# else:    
#     print("você digitou uma consoante!")

# #atividade 1 de outra maneira (sem precisar colocar as LETRAS MAIUSCULAS no if):
# #upper() -> CONVERTER TUDO PARA MAISCULO
# #lower() -> converter tudo para minusculo
#letra = input("digite uma letra: ").lower()
# if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
#     print("você digitou uma vogal!")
# else:    
#     print("você digitou uma consoante!")

# #NOVO OPERADOR na atividade 1:
# #and, or e IN
#letra = input("digite uma letra: ")
# if letra in "aeiouAEIOU":                                # -> IN (se) a letra estiver dentro da sequência "aeiouAEIOU"...
#     print("você digitou uma vogal!")
# else:    
#     print("você digitou uma consoante!")

# #atividade 2:
# n1 = float(input("digite um número: "))
# n2 = float(input("digite outro número: "))
# if n1 > n2:
#     print(f"\nmaior número: {n1}")
#     print(f"menor número: {n2}")
# else:
#     print(f"\nmaior número: {n2}")   
#     print(f"menor número: {n1}")