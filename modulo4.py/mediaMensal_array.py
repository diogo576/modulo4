"""
programa para ler a temperatura média mensal de uma cidade ao longo do ano(12 meses).
o programa deve mostra a média, a menor, a maior, a moda e os meses em que a temperatura foi 
superior á média.
UTILIZE VALORES INTEIROS
"""
import numpy as np
NR_MESES =12

temperaturas = np.zeros(NR_MESES)
#leitura das temperaturas para o array
for mes in range(NR_MESES):
    temperaturas[mes] = int(input(f"Introduza a temperatura média do mês{mes+1}:"))
#maior e a menor temperatura
maior = temperaturas[0]
menor = temperaturas[0]
for mes in range(1,NR_MESES):
    if temperaturas[mes] > menor:
        maior = temperaturas[mes]
    if temperaturas[mes] <menor:
        menor = temperaturas[mes]
print(f"A temepratura mais elevada foi de {maior} e a menor temperatura foi de {menor}.")
#média
soma = 0 
for t in temperaturas:
    soma = soma + t
media =soma / NR_MESES 
print(f"a temperatura média anual foi de {media}")
#mostrar meses com temperaturas superior á média 
for mes in range(NR_MESES):
    if temperaturas[mes] > media:
        print(f"A temperatura do mês {mes+1} foi de {temperaturas[mes]} sendo superior á média.")
#moda
nr_vezes_moda = 0
moda = 0
for mes in range(NR_MESES):
    CONTAR =0
    for m_atual in range(NR_MESES):
        if temperaturas[mes] == temperaturas[m_atual]:
            CONTAR = CONTAR + 1
        if CONTAR > nr_vezes_moda:#se o contar é superior ao nr_vezes_moda este passa a ser a moda
            nr_vezes_moda = CONTAR #nr de vezes que a temperatura da posição mes aparece 
            moda = mes #a posição da temperatura contada
print(f"A moda é a temperatura{temperaturas[moda]} que ocrreu{nr_vezes_moda} vezes.")
