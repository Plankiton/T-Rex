from Translater import *

txt = """
algoritmo "joao"

var
j, k: inteiro

inicio

para i de 4 ate 8 faca
print ("joao")
fimpara

escolha j

caso 1
print("porra")
caso 2
print(" outra porra")
caso 67
print(" boiolage " )
caso 45
print(" joao ")
outro caso
print(" outra porra denovo")

fimescolha

fimalgoritmo
"""

print(translate(txt, 'portugol_to_python.yml'))
