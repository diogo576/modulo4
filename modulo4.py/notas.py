#programa para ler as notas de 10 alunos, caucular e mostrar
#  as medias das notas e por fim mostrar as notas que são superiores á media

import numpy as np

#constante com o valor do nº de alunos
NR_ALUNOS = 10

#definir o array para as notas 
notas = np.zeros(NR_ALUNOS)

#ler as notas
for n in range(NR_ALUNOS):
   notas[n] = int(input(f"nota do aluno nº{n+1}:"))
#print(notas)

#calcular Média 
soma = 0 
for n in range (NR_ALUNOS):
   soma = soma + notas[n]

media = soma / NR_ALUNOS
print(f"a media das notas dos alunos foi de{media}")

#listar as notas que são superiores à media
for n in range(NR_ALUNOS):
   if notas > media:
      print(f"a nota{notas[n]} do aluno nº{n+1} é superior à media")