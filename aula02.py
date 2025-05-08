import os
os.system("cls")
#aula 02 -> variaveis, tipos e Input - são variaveis (objeto que armazena um valor)

#tipos de dados:
#String - texto
#Int - inteiro
#Float - quebrado (flutuante)

#declaração de variaveis
#mostrando o valor da variavel no print
escola = "senai"
print(escola)

#concatenando com o +
print("o nome da minha escola é " + escola)
#separando por parametro ,
print("o nome da minha escola é" , escola)
#f string
print(f"o nome da minha escola é {escola}")

#podemos fazer as operações matemáticas com variaveis int
número = 100
print(número)
print("somando com 10 = " ,número+10)
print("subtraindo 5 = ", número-5)
print("dividindo por 2 = ", número/2)
print("multiplicando por 10 = ", número*10)


#atividade 1
nome = "Laura Rodrigues de Souza"
idade = "16"
CPF = "504.966.688-03"
print("NOME: " ,nome )
print("CPF: " + CPF)
print (f"idade: {idade} anos")

#input () -> perguntar algo a ser armazenado (pra armazenar SEMPRE será preciso uma variavel antes do input)
#print () -> mostra texto na tela
texto = input("digite algo: ")
print("você digitou ..." ,texto)


print("*"*15 , "CADASTRO" , "*"*15 )
nome = input("digite seu nome: ")
cpf = input("digite seu cpf: ")
rg = input("digite eu rg: ")

print("*"*15 , "DADOS CADASTRADOS" , "*"*15 )
print("nome: " ,nome)
print("cpf: " ,cpf)
print("rg:  " ,rg)