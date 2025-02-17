import numpy as np

#definir um array para strings 
"""
i = inteiros 
f = reais 
b = boleanos
s =unicode string
m = datetime
"""
nomes = np.empty(10,dtype="U20")

for i in range(len(nomes)):
    nomes[i] =input("Introduza o nome:")
print(nomes)