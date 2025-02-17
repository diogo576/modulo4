import numpy as np
notas= np.array([12,10,11,14])
aluno1={"nome":"Juaquim","turma":"10t","email":"juaquim@gmail.com","notas":notas}

#listar as notas do aluno 1
for nota in aluno1["notas"]:
    print(nota)

for posicao in range(len(aluno1["notas"])):
    print(aluno1["notas"][posicao])