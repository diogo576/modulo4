#programa para preencher um array com 10 elementos em que cada 
#elemento é o dobro do valor do indice da sua posição 
import numpy as np
dobro = np.empty(10)
for i in range(10):
    dobro[i] = i * 2 

print(dobro)
