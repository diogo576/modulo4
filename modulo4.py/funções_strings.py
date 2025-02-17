texto = "ola mundo"
tamanho = len(texto)
print(tamanho)

texto = texto.upper()#devolve a string em maiusculas
print(texto)
texto = texto.lower()#devolve a string em minusculas
print(texto)
texto = texto.capitalize()#devolve a string com a primeira em M
print(texto)

texto.strip()#devolve astring sem espaços em branco no inicio e no final
print(texto)
texto = texto.replace(" ","-")#devolve a string substituindo o primeiro parametro pelo segundo(" "por"-"")
print(texto)
print(texto.isdigit())#devolve verdadeiro se todas as letras sem digitos(numeros)
frase ="ola mundo, o computador é uma torradeira"
palavras = frase.split(" ")#devolve uma lista com partes da string por carater indicado
print(palavras)
print(len(palavras))
print(palavras[1])
posicao = frase.index("m")#devolve a posição da string mas se não existir dá erro
print(posicao)
posicao = frase.find("m")#devolve a posição da sting se não encontar devolve -1
if posicao == -1:
    print("não encontrei")
else:
    print("encontrei na posição",posicao)

#código ascii de uma letra
codigo = ord("a")
print(codigo)
#devolve a letra correspondente  ao codido ASCII
letra = chr(97)

