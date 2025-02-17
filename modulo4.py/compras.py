#produtos comprados 
produtos=['bananas','maçã','laranja']
#preços unitários
precos =[2.5,3.5,4.5]
#quantidades compradas
quantidades =[2,3,3]
compras={}
#criar um dicionário que combina os dados das listas produtos, precos e quantidades
for p in range(len(produtos)):
   compras[produtos[p]]={'quantidade':quantidades[p],'preco':precos[p]}
print(compras)

#percentagem de desconto
descontos={'bananas':0,
           'maçã':15,
           'laranja':20}
#ler do utilizador as quantidades para o dicionário daas compras
for p in compras:
    compras[p]['quantidade'] = float(input(f"Qual a quantidade de {p}:"))
#adicionar um produto novo introduzido pelo utilizador 
nome= input("qual o produto:")
preco = input("qual o preço:")
quantidade = float(input("qual a quantidade:"))
desconto = float(input("qual a percenagem do desconto:"))
#adicionar o desconto ao dicionário de descontos 
descontos[nome]= desconto
#adicionar ao dicionário das compras o produto 
compras[nome] ={'preco':preco,'quantidade':quantidade}
total = 0
#calcular o valor total a apagar pelas compras tendo em conta as quantidades compradas 
# e percentagem de desconto de cada produto 
for p in compras:
   valor_pagar = compras[p]['preco'] * compras[p]['quantidade']
   valor_desconto = (descontos[p] /100) * valor_pagar
   valor_com_desconto = valor_pagar - valor_desconto
   total = total + valor_com_desconto
total = round(total,2)
print(F"valor a pagar pelas compras é de {total}")
   
   
   
