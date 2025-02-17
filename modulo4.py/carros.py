""" programa para calcular e mostrar o numero de carros por marca sem repetir"""
import numpy as np 

carros = np.array(["bmw","tesla,","peugeot","ford,","tesla","mercedes","bmw","volvo"])
marcas = np.zeros(len(carros),"U20")

n = 0
for carro in carros:
    if carro in marcas:
        continue
    marcas[n] = carro
    n = n +1 
    contar = 0 
    for carro2 in carros:
        if carro == carro2:
            contar = contar + 1 
        print(f"A {carro} tem {contar} carros")
