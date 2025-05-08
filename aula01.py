#aula 01 -> String (texto), Int (número inteiro), Float (número quebrado) - são tipos de dados

#print -> exibe mensagem no terminal
print( " HELLO WORLD! " )
print( " LAURA " )

#diferença entre texto e numero (atenção nas "")
print( 10 + 10 ) #realiza a soma = 10+10 = 20
print( "10" + "10" ) #concatena = junta 10 com 10 = 1010

#operações matematicas
#soma +
#subtração - 
#multiplicação *
#divisão /

#exemplos
print (2+2)
print(10-5)
print(10*2)
print(20/2)

#parametros no print
#print(a,b,c,d,e,...) até no máximo 128 parametros (vírgulas)
print("escola senai")
print("escola","senai")
#para que usar
print("10 + 10 =", 10+10)

#atividade 1
print("Laura Rodrigues de Souza, 16, 504.966.688-03")
print("Laura Rodrigues de Souza", "16", "504.966.688-03")

#formatações Sep e End
#sep -> operador de separação (troca o caractere padrão na virgula pelo setado dentro do sep)
#end -> operador final (coloca o caractere no final do print)
print("*"*5, "SEJA BEM VINDO", "olá"*5) #multiplicar caracteres
print("aula" , "de" , "python" , sep="@", end="!")
print("no senai")
#o end também pega a linha de baixo e coloca na linha de cima (nesse caso, a linha 36 junta com a 37)

#\n -> quebra linha
print("outro \nexemplo")

#limpar o terminal (deixa na linha 1, pra quando rodar dnv o terminal já limpar e ir direto pro novo)
import os 
os.system ("cls")

#atividade 1:
print("curso", "de", "python", sep="_", end="%"*2)
print ("\n*no senai rio claro")
print ("", "logica", "de", "programação", sep="_-_-_")
#atividade 2:
print("\npython", "versao3", sep="@"*3, end="[]" )
print("\nlogica", "de", "programação", sep="#"*3 )
print("","uso", "do", "print", sep="&", end="()")

