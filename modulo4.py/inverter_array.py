#programa para inverter um array de nomes com 5 elementos

import numpy as np
N_ELEMENTOS =5
nomes =np.empty(N_ELEMENTOS,dtype="U20")

for i in range(N_ELEMENTOS):
    nomes[i] = input(f"Introduza o nome:")

#criar o array par os elementos com posições invertidas
nomes_invertido =np.empty(N_ELEMENTOS,dtype="U20")
#preencher o array invertendo as posições
k =N_ELEMENTOS - 1
for i in range(N_ELEMENTOS):
    nomes_invertido[k] =nomes[i]
    k = k- 1
#mostrar os dois arrays
print(nomes,nomes_invertido) 