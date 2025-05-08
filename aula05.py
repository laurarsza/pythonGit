import os
os.system("cls")

#IF ENCADEADO -> TESTA TODAS AS CONDIÇÕES MESMO SE UMA FOR VERDADEIRA
#ELIF -> TESTA TODAS AS CONDIÇÕES ATÉ UMA SER VERDADEIRA

# x = 15 

# if x <=20 :
#     print("entrou no if 14")
# if x <=15 :
#     print("entrou no if 15")
# if x <=16:
#     print("entrou no if 16")


# if x <=20:
#     print("entrou no if 14")
# elif x<=15:
#     print("entrou no if 15")
# elif x <=16:
#     print("entrou no if 16")


# ESCREVA UM PROGRAMA EM PYTHON NA QUAL O USUARIO DIGITA A IDADE
#  SE MENOR QUE 12 -> CRIANÇA
#  SE MENOR QUE 18 -> ADOLESCENTE
#  SE MENOR QUE 60 -> ADULTO
#  SE NAO -> IDOSO


# NO CASO SE USAR IF ELE VAI TESTAR TODAS AS CONDIÇÕES
# idade = int(input("digite sua idade: "))

# if idade < 12:
#     print("criança")
# if idade < 18:
#     print("adolescente")
# if idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")


# SE USAR ELIF ELE VAI TESTAR UMA E SAIR DA ESTRUTURA
# if idade < 12:
#     print("criança")
# elif idade < 18:
#     print("adolescente")
# elif idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")
    
# #atividade 1: 
#.replace ("valor1","valor2") -> substitui o valor 1 pelo valor 2
# nota1 = float(input("digite a 1 nota: ").replace(",","."))
# nota2 = float(input("digite a 2 nota: ").replace(",","."))
# media = (nota1+nota2)/2
# print(f"sua média é {media:.2f}")
# #:.2f -> formata para 2 casas decimais (apenas no fstring)
# if media < 5:
#     print("reprovado")
# elif media >=  5 and media <= 7:
#     print("em recuperação")
# else:
#     print("aprovado")    
      
# #atividade IMC:
# peso = float(input("digite seu peso: ".replace(",",".")))  
# altura = float(input("digite sua altura: ".replace(",","."))) 
# imc = round(peso / (altura*altura),2)
# print(f"seu IMC é: {imc}")
# if imc < 17:
#     print("muito abaixo do peso")
# elif imc >= 17 and imc <= 18.49:
#     print("abaixo do peso") 
# elif imc >= 18.50 and imc <= 24.99:
#     print("peso normal")    
# elif imc >= 25 and imc <= 29.99:
#     print("acima do peso")    
# elif imc >= 30 and imc <= 34.99:
#     print("obesidade 1")   
# elif imc >=35 and imc <= 39.99:
#     print ("obesidade 2")
# else:
#     print("obesidade 3 (mórbida)")         

#raw string -> 

print("*"*10, "REAJUSTE AUTOCAR", "*"*10)
print("TABELAS DE REAJUSTE DE SALÁRIO:")
print("Salários até R$ 2799,99 : aumento de 20%")
print("Salários entre R$ 2800,00 e R$ 6999,99 : aumento de 15%")
print("Salários entre R$ 7000,00 e R$ 14999,99 : aumento de 10%")
print("Salários entre R$ 15000,00 em diante : aumento de 5%")

salario = float(input("\nDigite seu salário: R$"))
print("¨"*20)
print(f"SALARIO SEM REAJUSTE: R${salario}")
if salario <= 2799.99:
    print("PERCENTUAL DA SUA FAIXA: 20%")
elif salario >= 2800.00 and salario <= 6999.99:
    print("PERCENTUAL DA SUA FAIXA: 15%")    
elif salario >= 7000.00 and salario <= 14999.99:
    print("PERCENTUAL DA SUA FAIXA: 10%")
else:
    print("PERCENTUAL DA SUA FAIXA: 5%")    

if salario <= 2799.99:
    print(f"AUMENTO DE: R${salario*0.20}")
elif salario >= 2800.00 and salario <= 6999.99:
    print(f"AUMENTO DE: R${salario*0.15}")    
elif salario >= 7000.00 and salario <= 14999.99:
    print(f"AUMENTO DE: R${salario*0.10}")
else:
    print(f"AUMENTO DE: R${salario*0.05}")

if salario <= 2799.99:
    print(f"NOVO SALÁRIO: R${(salario*0.20) + salario}")
elif salario >= 2800.00 and salario <= 6999.99:
    print(f"NOVO SALÁRIO: R${(salario*0.15) + salario}")   
elif salario >= 7000.00 and salario <= 14999.99:
    print(f"NOVO SALÁRIO: R${(salario*0.10) + salario}")
else:
    print(f"NOVO SALÁRIO: R${(salario*0.05) + salario}")