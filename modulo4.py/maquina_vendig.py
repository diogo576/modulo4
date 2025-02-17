""" programa para simular o moedeiro de uma maquina de vending 
o programa  deve ler o preço a pagar e o valor entregue depois devolver o troco , caos exista, 
moeda a moeda de acordo com o stock disponivel 
"""
import numpy as np 

moedas = np.array([0.01,0.02,0.05,0.1,0.2,0.5,1,2])
stock =np.array([2,2,2,2,2,2,2,2])

# preço do produto 
valor_pagar =float(input("qual o valor a pagar:"))
#quantia entregue pelo cliente
valor_entregue = float(input("qual o valor entregue:"))
#calcular o troco
troco = valor_entregue - valor_pagar
if troco == 0:
    print("volte sempre")
else:
    moedas_a_devolver = ""
    #procurar as moedas que prefazem a quantia do troco
    #todo: tesar o chatgpt para ver se consegue
    while troco != 0:
        for n in range(len(moedas)-1,-1,-1):
            #se existe a moeda e se o valor a devolver é maior a moeda
            if moedas[n]<troco and moedas[n]>0:
                moedas_a_devolver = moedas_a_devolver + str(moedas[n])
