"""programa para ler um nome e mostrar o nome no formato: ultimo,primeiro,segundo"""

def AlteraNome(nome)->str:
    #separar os nomes
    nome= nome.slipt(" ")
    #verificar os nomes 
    if len(nome)== 1:
        return nome
    #criar uma string com o ultimo nome e , 
    nome_alterado = nome[len(nome)-1]+","
    #juntar na string os restantes nomes
    for n in nome[:len(nome)-1]:
        nome_alterado = nome_alterado + n + " "
    return nome_alterado.strip()
def main():
   nome = input("introduza o seu nome completo:")
   nome_alterado =AlteraNome()
   print(nome_alterado)
 
if __name__=="__main__":
    main()