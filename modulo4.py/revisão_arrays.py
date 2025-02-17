""" um programa para registar os nomes dos clientes que entraram numa loja num determinado dia 
e o valor das compras de cada 
o programa deve mostrar o nome do cliente que fez a compra mais cara"""

import numpy as np

#defenir os arrays:para nomes e para as cientes
MAX_clientes = 10

nomes=np.empty(MAX_clientes,dtype="U50")
compras=np.empty(MAX_clientes,dtype="f")
#função para ler os daods 
#array passado por referencia
def Ler_dados(nomes_clientes,compras_clientes):
    #perguntar quantos clientes entraram
    n_clientes=int(input("quantos clientes entraram na loja:"))
    for i in range(n_clientes):
        #ler o nome 
        nomes_clientes[i]=input("nome:")
        #ler o valor das compras
        compras_clientes[i]=input("valor das compras:")
#função para mostrar o nome do cliente com a compra mais cara
def MelhorCliente(nomes_clientes,compras_clientes):
    posição = 0
    maior_compra =compras_clientes[0]
    #percorrer o array
    for i in range(MAX_clientes):
        if maior_compra < compras_clientes[i]:
            #guardar o maior valor e a posição
            maior_compra = compras_clientes[i]
            posição = i
    print(f"o melhor cliente foi {nomes_clientes[posição]}que gastou{compras_clientes[posição]}")

Ler_dados(nomes,compras)
MelhorCliente(nomes,compras)