""" 
agenda:
    nome
    N_telefone
    email
menu principal:
1.Adicionar
2.Listar todos
3.Procurar
4.Apagar
5.Treminar
 """
import numpy as np
Max_contactos= 100
nomes= np.empty(Max_contactos,dtype="U50")
emails = np.empty(Max_contactos,dtype="U50")
telefones = np.empty(Max_contactos,dtype="U9")
nr_contactos = 0

#criar funções para cada escolha do utilizador
#função para adicionar contactos
def Adicionar(nomes,emails,telefones,nr_contactos):
    nomes[nr_contactos]= input("nome:")
    emails[nr_contactos] = input("email:")
    telefones[nr_contactos] = input("telefone:")
    nr_contactos += 1  
    return nr_contactos
#função para listar todos os contactos
def listar_todos(nomes,emails,telefones,nr_contactos):
    print("#"*60)
    print("#listar contactos##",end="")
    print(""*38,end="")
    print("##")
    print("#"*60)
    for i in range(nr_contactos):
        print(f"#{nomes[i]}\t {emails[i]}\t {telefones[i]}\t #")
#função para procurar determinado contacto
def procurar(nomes,emails,telefones,nr_contactos):
    nome_procurar = input("qual o nome do contacto:")
    for i in range(nr_contactos):
        if nome_procurar in nomes[i]:
            print(F"#{nomes[i]}\t {emails[i]}\t {telefones[i]}\t#")   
#função para apagar um contacto 
def apagar(nomes,emails,telefones,nr_contactos):
    print("#"*60)
    print("#listar contactos##",end="")
    print(""*38,end="")
    print("##")
    print("#"*60)
    nome_procurar = input("qual o nome do contacto:")
    for i in range(nr_contactos):
        if nome_procurar in nomes[i]:
            print(F"#{nomes[i]}\t {emails[i]}\t {telefones[i]}\t#")
            opção =input("tem certeza que pretende eliminar este contacto? (s/n)")
            if  opção in "sS":
                for k in range(i,nr_contactos):
                    break
                nomes[k] = nomes[k+1]
                emails[k] = emails[k+1]
                telefones[k] = telefones[k+1] 
            nr_contactos = 1   
    return nr_contactos
#função para terminar o programa 
def terminar():
    pass
#função para editar os contactos
def editar(nomes,emails,telefones):
    """função pesquisa um contacto pelo nome e permite alterar os dados"""
    #pedir o array ao utilizador
    nome = input("qual o nome do contacto a editar:")
    #percorrer os arrays dos nomes
    for i in range(nr_contactos):
        #encontar o nome permite alterar os dados 
        if  nome in nomes[i]:
            print(f"Dados do contacto: {nomes[i]} - {emails[i]} - {telefones[i]}")
            op = input("pretende eidtar estes dados? (s\n)")
            if op.lower()!="s":
                continue
            #editar os dados 
            novo_nome = input("introduza o novo nome ou deixa em branco par não alterar:")
            novo_email =input("introduza o novo email ou deixe em branco pra não alterar:")
            novo_telefone = input("introduza o nove telefone ou deixe em branco para não alterar:")
            if novo_nome.strip()!="":
                nomes[i] = novo_nome.strip()
            if novo_email.strip()!="":
                emails[i] = novo_email.strip()
            if novo_telefone.strip()!="":
                telefones[i] = novo_telefone.strip()
#função para o menu
def menu():
    nr_contactos = 0
    opção = 0
    while opção != 5:
        print("1.adicionar\n2.listar\n3.procurar\n4.apagar\n5.terminar")
        opção = int(input("opção:"))
        if opção == 1:
           nr_contactos = Adicionar(nomes,telefones,emails,nr_contactos)
        elif opção == 2:
            listar_todos()
        elif opção == 3:
            procurar(nomes,emails,telefones,nr_contactos)
        elif opção == 4:
            apagar()
        elif opção == 5:
            break
        else:
            print("opção não existe")

if __name__=="__main__":
    menu()