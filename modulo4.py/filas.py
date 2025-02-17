""" o SR.Silva tem um restaurante muito popular e precisa de ajuda a gerir a fila de espera dos clientes

Pretende_se criar um programa para registar os nomes dos clientes em espera e de cada vez 
retirar o primeiro a chegar à fila
menu: 1.Entrada 2.Saída 3.Consultar Fila 4.Terminar
"""
import numpy as np
MAXIMO = 10
def Entrada(fila):
    """adicionar um nome ao final da fila de espera"""
    #procurar o ultimo lugar da fila
    for posicao in range(MAXIMO):
        if fila[posicao]=="":
            encontrou = True
            break
        #avisar se a fila está cheia
        if encontrou == False:
                print("fila cheia.Volte mais tarde.")
                return 
        #ler o nome 
        nome=input("introduza o nome do cliente:")       
    #inserir no final
    fila[posicao]= nome 
    print(f"A sua posição na fila de espera é {posicao+1}:")
def Saida(fila):
    #verificar se a fila está vazia
    if fila[0] =="":
        print(" nao tem ninguem na lista de espera.")
        return 
    #retirar o primeiro nome da fila de espera 
    print(f"o cliente com o nome{fila[0]} pode entrar.")
    #avansar os restantes nomes da fila uma posição
    for i in range(MAXIMO-1):
        fila[i] = fila[i+1]
    fila[MAXIMO-1]="" #para limpar a ultima posição do array 

def Consultar(fila):
    """listar os nomes na fila de espera"""
    #verificar se a fila está vazia
    if fila[0] =="":
        print(" nao tem ninguem na lista de espera.")
        return 
    #listar os nomes das pessoas em espera
    fila_cheia = True
    for posicao in range(MAXIMO):
        if posicao =="":
            fila_cheia = False
            break
        print(f"{posicao+1} - {fila[posicao]}")
    #verificar se a fila está cheia
    if fila_cheia == True:
        print("fila de espera cheia.volte mais tarde")

def main():
    fila = np.empty(MAXIMO,dtype="U20")
    #limpar array
    for i in range[MAXIMO]:
        fila[i]=""
    op = 0
    while op != 4:
        op=input("1.Entrada\n2.Saída\n3.Consultar Fila\n4.Terminar")
        if op == "1":
            Entrada(fila)
        elif op == "2":
            Saida(fila)
        elif op == "3":
            Consultar(fila)
        elif op == "4":
            break
        else:
            print("opção inválida")


if __name__=="__main__":
    main()