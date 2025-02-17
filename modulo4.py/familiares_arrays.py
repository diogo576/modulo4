"""programa para ler dois nomes completos e indicar se são familiares.
Dois nomes são familiares se o ultimo nome for igual.
Dois nomes são familiares se um dos dois ultimos nomes forem iguais por qualquer ordem(ultimo=penultimo,
ultimo=ultimo,penultimo=penultimo)"""

def familiares(A,B)-> bool:
    nomesA = A.split(" ")#lista com os nomes 
    nomesB= B.split(" ")#lista com os nomes 
    #verificar se os ultimos nomes são iguais
    if nomesA[len(nomesA)-1] == nomesB[len(nomesB)-1]:
        return True  
    #verificar se os dois ultimos nomes são iguais
    for i in nomeA[1:]:
        for k in nomeB[1:]:
            if i == k:
                return True
    return False 
    
nomeA = input("introduza um nome completo: ")
nomeB = input("introduza um nome completo: ")
print(familiares(nomeA,nomeB))

