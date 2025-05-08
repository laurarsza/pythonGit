import os
os.system("cls")

#aula 03 -> continuação input com int e float
#exemplo 1
numero = 10
numero2 = input("digite um numero: ")
print("o tipo do numero é", type(numero2)) #type retorna o tipo da variavel (string, int ou float)
soma = numero + numero2
print(f"soma de {numero} + {numero2} = ", soma)
#não dá certo porque o "numero" é int e o "numero2" vem em string

#correção do exemplo acima
#int() -> converte para inteiro
#float() -> converte para numero quebrado
#SEMPRE que for preciso armazenar um numero, temos que converter o número para int ou float
numero = 10
numero2 = input("digite um numero: ")
print("o tipo do numero é", type(numero2)) #type retorna o tipo da variavel (string, int ou float)
soma = numero + int(numero2)
print(f"soma de {numero} + {numero2} = ", soma)

#exemplo 2
num1 = input("digite um numero: ")
soma = float(num1) + 15
print("a soma de",num1 , "+", "15", "=", soma)

#exemplo 3
#maneira mais simples: converter o input em float ou int diretamente
n1 = float(input("digite um numero: "))
n2 = float(input("digite outro numero: "))
soma = (n1)+(n2)
print(f"a soma de {n1} + {n2} =", soma)

#atividade 1:
n1 = float(input("digite um número: "))
n2 = float(input("digite outro número: "))
multiplicacao = (n1)*(n2)
print(f"a multiplicação de {n1} e {n2} =", multiplicacao)

#atividade 2:
numero = float(input("digite um número: "))
antecessor = (numero)-1
sucessor = (numero)+1
print(f"o antecessor de {numero} é: {antecessor}")
print(f"o sucessor de {numero} é: {sucessor}")

#atividade 3:
nascimento = int(input("digite seu ano de nascimento: "))
idade = 2025 - (nascimento)
print(f"sua idade é {idade} anos")

#ATIVIDADE: Escreva um programa em python que leia 2 itens de um supermercado,
#você deve armazenar o nome e o valor do item, no final aplique 10% de desconto
#no primeiro item e 25% de desconto no segundo item. Calcule o valor total de
#compra e mostre o nome e o valor com desconto de cada item.

print("¨"*20, "SUPERMERCADO", "¨"*20)
nome1 = input("digite o nome do primeiro produto: ")
valor1 = float(input("digite o valor desse produto R$: "))
nome2 = input("digite o nome do segundo produto: ")
valor2 = float(input("digite o valor desse produto R$: "))
desconto1 = 0.10*valor1
desconto2 = 0.25*valor2
valorfinal1 = round(valor1-desconto1, 2)
valorfinal2 = round(valor2-desconto2, 2)
print("¨"*20, "CAIXA", "¨"*20)
print(f"{nome1} custa R$ {valor1} com desconto de 10% =" , valorfinal1)
print(f"{nome2} custa R$ {valor2} com desconto de 25% =" , valorfinal2)
print("="*10, "TOTAL", "="*10)      
print(f"VALOR TOTAL R$ {valorfinal1+valorfinal2}")
#round(valor, quantas casas decimais) -> faz o arredondamento dos valores
