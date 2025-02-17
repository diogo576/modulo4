""" criar uma agenda que regista os nomes por ordem alfabetica
Guardar o nome e data de nascimento das pessoas ordenadas por ordem crescente do nome 
Menu: 1.Adicionar 2.Contacto 2.Listar contactos 3.Pesquisar 4.Terminar
"""
import numpy as np 

NR_MAXIMO = 10
def Adicionar(contactos,nome):
    #recebe um array e o nome de contacto a inserir por ordem alfabética
    #verificar se esta vazio o array
    if contactos[0] =="":
        contactos[0] = nome
        return
    #verificar se está cheio
    if contactos[NR_MAXIMO-1] !="":
        print("agenda de contactos está cheia")
        return 
    #procurar a posição do novo contacto 
    for posicao in range (NR_MAXIMO):
        if nome < contactos[posicao] or contactos[posicao]=="":
            break
    #avançar uma posicao os restantes contactos
    for i in range(NR_MAXIMO-1,posicao,-1):
        contactos[i] = contactos[i-1]
    #inserir o contacto
    contactos[posicao]= nome

def Listar(contactos):
    #listar os nomes e as datas de nascimento de todos os contactos
    for nome in contactos:
        if nome !="":
            partes = nome.split('-')
            print(f"nome: {partes[0]} data de nascimento: {partes[1]}")

def Pesquisar(contactos,nome):
    """ recebe o array e o nome a pesquisar"""
    #pesquisa binaria 
    primeiro = 0
    ultimo = len(contactos) + 1
    for t in contactos:
        if t =="":
            break
        ultimo = ultimo + 1
    while primeiro <= ultimo:
        meio = (primeiro + ultimo)// 2
        valor_meio = contactos[meio]
        if nome in valor_meio:
            print(valor_meio)
            return
        elif valor_meio < nome:
            primeiro == meio + 1
        else:
            ultimo == meio - 1
print("nome indicado não existe")

def main():
    contactos = np.zeros(NR_MAXIMO,dtype="U30")
    op = 0
    while op != 4:
        op=input("1.Adicionar\n2.Listar\n3.Pesquisar\n4.Terminar")
        if op == "1":
            nome =input("nome do contacto a pesquisar")
            data = input("data de nascimento")
            Adicionar(contactos,nome +"-"+ data)
        elif op == "2":
            Listar(contactos)
        elif op == "3":
            nome = input("nome a pesquisar:")
            Pesquisar(contactos,nome)
        elif op == "4":
            break
        else:
            print("opção inválida")


if __name__=="__main__":
    main()