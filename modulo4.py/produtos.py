"""
preferencias entre dicionarios e dicionarios com arrays 
"""

marca1 ={"nome":"nike","tipo":"calçado","país":"americano"}
marca2 = {"nome":"adidas","tipo":"roupa e calçado","país":"alemão"}
marca3 ={"nome":"mimosa","tipo":"leite","país":"portugal"}

produto1={"nome":"sapatilhas","preço":"85,45","marca":marca2}

#mostrar de que país pertence a marca
print(produto1["marca"]["país"])
marca2["país"]= "japão"
print(produto1)
produto2={"nome":"casaco","preço":100,"marca":marca2}
marca2={}#cria um dicionario novo mas a informação dos produtos 1 e 2 continua a ser referenciada
print(produto1) 
print(produto2)
