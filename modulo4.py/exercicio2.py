import numpy as np 
array=np.array([10,11,12])


def soma(array):
    soma_valores = 0 
    for v in array:
        soma_valores = soma_valores + v
    return soma_valores

print(soma(array))
