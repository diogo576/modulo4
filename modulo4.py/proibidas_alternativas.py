""" programa para percorrer um array e modificar a string """
import numpy as np 

proibidas = np.array(["mau","pobre","infeliz","pessimo","feio","desumilde"])
alternativas = np.array(["bom","rico","feliz","ótimo","bonito","humilde"])

frase = input("introduza a frase")

#verificar se algumas das palavras proibidas está presente na frase e substituir pela frase alternativa correspondente
for i in range(len(proibidas)):
    if proibidas[i] in frase:
        frase = frase.replace(proibidas[i],alternativas[i])

print(frase) 
    
