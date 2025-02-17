"""
slicing -permite ter acesso a subconjuntos de uma sequencia ou coleção
    sintaxe : sequencia[inicio:fim:passo]
    inicio- a posição do primeiro a incluir 
    fim- é a posição onde termina o slice (NAO É INCLUIDO)
    passo- intervalo entre os elementos a incluir no slice 
"""


nome ="Juaquim Silva"
nome_5_letras = nome[0:5:1]#copia as letras das posições 0 a 4
print(nome_5_letras)
nome_5_letras = nome[:5:1]#copia as primeiras 5 letras
print(nome_5_letras)
nome_ultimas_letras = nome[7:]#copiar as letras na posição 7 ate ao fim 
print(nome_ultimas_letras)
nome_ultimas_letras = nome[7:110]#copiar as letras na posição 7 ate ao fim 
print(nome_ultimas_letras)
nome_invertido = nome[::-1]#inverter a string 
print(nome_invertido)
nome_2_2_letras = nome[::2]#
print(nome_2_2_letras)
print(nome[-1])#ultima letra da string 
ultimo_nome_invertido = nome[:-7:-1]
print(ultimo_nome_invertido)

import numpy as np 
nomes=np.array(["joaquim","maria","antónio","augusto","cesar"])
#mostrar todos os nomes pela ordem inversa
nomes_todos= nomes[0:]
print(nomes_todos)
#mostrar os dois ultimos nomes
ultimos_dois_nomes = nomes[3:]
print(ultimos_dois_nomes)
print(nomes[len(nomes)-2:])
#mostrar o 1º,3º,5º
print(nome[::2])