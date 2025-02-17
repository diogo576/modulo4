""" 
dicionario                                               palavra - chave
1.adicionar definição                                    definição - valor
2.listar todas as definições
3.pesquisar definição
4.apagar
5.terminar
programa que implementa as funvionalidades de um dicionário de termos técnicos
(termos e definição)
MENU de opções (1.Adicionar termos;2.Listar todos os termos;3.pesquisar um termo;4.apagar um termo;5.sair)
opcional: Listar todos os termos ordenados alfabeticamente 
No Futuro: Guardar os dados num ficheiro(M07)
"""
def adicionar(dicionario):
    #ler o termo
    termo =input("Qual é a palavra a adicinar ao dicionario?")
    #verificar se ja existe
    if termo in dicionario:
        #se existir perguntar se pretende atualizar 
        op =input("esse termo ja existe no dicionario. pretende alterar?")
        if op == "n":
            return
    #ler a definição
    dicionario =input("qual a definição da palavra indicada?")
    #adicionar ou atualizar o dicionario
    print("termo adicionado/atualizado com sucesso")

def listar(dicionario):
    op= input("pretende visualizar por ordem alfabetica?")
    if op !="s":
        for chave, valor in dicionario.items():
            print(F"{chave}-> {valor}")
    else:
        #ordenar as chaves
        chaves = dicionario.keys()
        chaves =sorted(chaves)
        #percorrer as chaves ordenadas e mostrar o valor correspondente 
        for chave in chaves:
            print(f"{chave}->dicionario{chave}")


    
def pesquisar(dicionario):
    #ler o termo a pesquisar
    chave_pesquisar = input("Introduza a palavra,ou parte da palavra,a pesquisar")
    # #percorrer o dicionario 
    for chave, valor in dicionario.items():
        #se o termo existir no inicio da chave mostrar o valor 
        if chave_pesquisar == chave[:len(chave_pesquisar)]: #slicing para só comparar o inicio da chave
            print(f"{chave} -> {valor}")

def apagar(dicionario):
    #ler o termo a apagar
    chave_apagar = input("Introduza a palavra,ou parte da palavra,a apagar")
    # #percorrer o dicionario 
    for chave, valor in dicionario.items():
        #se o termo existir no inicio da chave mostrar o valor 
        if chave_apagar == chave[:len(chave_apagar)]: #slicing para só comparar o inicio da chave
            print(f"{chave} -> {valor}")
            op = input("Pretende remover esta palavra do dicionário?")
            if op =='s':
                del dicionario[chave]
                return  #uma vez que o dicionario foi alterado náo podemos continuar o ciclo

def configurar(dicionario):
    dicionario["pêra"] ="fruta"
    dicionario["pc"]="computador pessoal"
    dicionario["bicicleta"]="meio de transporte"
#se o programa está em desenvolvimento deve ser true 
#se está terminado (em produção)
em_teste = True