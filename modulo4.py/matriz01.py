import numpy as np 
""" introdução as arrays de duas dimensões tambem chamdos de matrizes """

matriz = np.array([1,2,3],[3,5,0])
print(matriz)
#primeiro elemento da matriz
print(matriz[0,0])
#ultimo elemento da matriz
print(matriz[1,2])
print(f"função len com matriz{len(matriz)}")
#ciclo para percorrer todos os elmentos da matriz 
#for l in range(2):
#    for c in range(3):
#        print(matriz[l,c])

#n* de colunas
print("nº de linhas da matriz:",matriz.shape[1])
#nº de linhas 
print("nº de linhas da matriz:",matriz.shape[0])