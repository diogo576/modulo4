""" 
programa para registar as matriculas e o tempo (segundos) de utilização de um estacionamento
o programa deve ler uma linha com as matriculas separadas por ,e os tempos em segundos separados por,
p.ex:.
    00-00-oo,ab-cd-33, 33-44-zy(strings)
    120,535,10333              (inteiros)
no maximo o programa deve permitir 10 matriculas/tempos 
"""
import numpy as np
MX_LUGARES = 0
matriculas = np.zeros(MX_LUGARES,dtype="U8")
tempos= np.zeros(MX_LUGARES)
#ler os dados 
def LerDados(matriculas,tempos):
    todas_matriculas=input("Introduza as matriculas separadas por , (virgulas)")
    todos_tempos = input("Introduza os tempos de estacionamento separados por,(virgulas)")
    #separar os dados e inserir nos arrays 
    matriculas_separadas = todas_matriculas.split(",")
    tempos_separados =todos_tempos.split(",")
    if len(matriculas_separadas)!= len(tempos_separados):
        print("o nº de matriculas deve ser igual ao nº tempo")
        return
    #verificar se o array tem espaço para todos os elementos 
    if len(matriculas_separadas) > MX_LUGARES:
        print("Introduziu matriculas a mais,so pode inserir",MX_LUGARES)
    for i in range(len(matriculas_separadas)):
        #guardar a matricula 
        matriculas[i] = matriculas_separadas[i].strip()
        #guardar tempos 
        tempos[i] = tempos_separados[i].strip()
#calcular e mostrar a matricula do carro que esteve mais tempo no estacionamento 
def maiortempoestacionamento(matriculas,tempos):
    p_maior = 0
    for p in range(MX_LUGARES):
        if matriculas[p] == "":
            break
        if tempos[p] > tempos[p_maior]:
            p_maior = p 
    print(f"o tempo maior de estacionamento foi de {tempos[p_maior]} e corresponde à matricula{matriculas[p_maior]}")
#calcular a media dos tempos de estacionamento
def mediaTempo(tempos):
    soma = 0
    preenchidos = 0
    for p in range(len(tempos)):
        if tempos[p] == 0:
            break
        soma = soma + tempos [p]
    media = soma / preenchidos
    return media 
# mostrar as matriculas dos carros que estiveram mais tempo no estacionamento do que a media  
def listaSuperiorMedia(matriculas,tempos):
    media =mediaTempo(tempos)
    for p in range(MX_LUGARES):
        if tempos [p] == 0:
            break
        if tempos[p] > media:
            print(f"{matriculas[p]} este {tempos[p]} que é superior à média")
#verificar se existe algum carro que esteve no estacionamento mais do que uma vez
def verificarMatricula(matricula):
    for m in matriculas:
        contar = 0
        if m == "":
            break
        for m2 in matriculas:
            if m == m2:
                contar = contar +1 
        if contar > 1:
            print(f"A matricula {m} esteve estacionada {contar} vezes")
LerDados(matriculas,tempos)
verificarMatricula(matriculas)
#permitir a pesquisa de uma matricula  
#inserida pelo utilizador e mostrar os tempos dessa matricula caso existam 
#mostrar a lista das matriculas ordenadas pelos tempos de estacionamento (maior para o menor )
#mostrar os tempos de estacionamento convertidos em minutos:segundos 