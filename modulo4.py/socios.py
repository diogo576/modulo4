import numpy as np
socios_A = np.array(["joaquim","maria","joao"])
socios_B = np.array(["maria","antónio","carla"])

#listar os socios que pertence aos dois clubes
contar = 0
for nome_a in socios_A:
    for nome_b in socios_B:
        if nome_a == nome_b:
            print(f"o sócio com o nome {nome_a} pertence aos dois clubes")

#versão 2
for nome_a in socios_A:
    if nome_a in socios_B:
        print(f"o sócio com o nome {nome_a} pertence aos dois clubes")