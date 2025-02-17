from dicionario import configurar,adicionar,listar,pesquisar,apagar

def menu():
    dicionario={}
    if em_teste:
        configurar(dicionario)
    op = 0
    while op != 5:
        print("1.Adicionar termos\n2.Listar todos os termos\n3.pesquisar um termo\n4.apagar um termo\n5.sair")
        op =int(input("opção:"))
        if op == "1":
            adicionar({"palavra":"chave"})

        elif op == "2":
            listar(dicionario)
        elif op == "3":
            pesquisar(dicionario)
        elif op == "4":
            apagar(dicionario)
        elif op == "5":
            print("Obrigada por utilizar o nosso programa")
        else:
            print("opção inválida")

if __name__=="__main__":
    menu()