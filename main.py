# Nome(s) Discente(s): Maria Luísa Mendonça Oliveira, Poliana Cristina de Sousa
# Matrícula(s): 0049545, 0056154
# Data: agosto de 2024


# Declaro que sou o único autor e responsável por este programa. Todas as partes do programa, exceto as que 
# foram fornecidas pelo professor foram desenvolvidas por mim. Declaro também que
# sou responsável por todas  as eventuais cópias deste programa e que não distribui nem facilitei a #distribuição de cópias.

import time
import random
from guloso import Grafo
#from grafoOtimizado import Grafo

#numero_vertices = 5
numero_vertices = random.randint(1, 10)
grafo_aleatorio = Grafo.gerar_grafo_aleatorio(numero_vertices)
grafo_aleatorio.imprime_grafo()
x = grafo_aleatorio.coloracao_gulosa()

print(f'Cores: {x}')

'''
numero_vertices = 5
tempo_inicio = time.time()
while True:
    if time.time() - tempo_inicio > 6:
        print("Passaram 10 minutos")
        print(f'Maior instância: {numero_vertices}')
        break
    if time.time() - tempo_inicio == 1800:
        print("Passaram 30 minutos")
    if time.time() - tempo_inicio == 3600:
        print("Passaram 60 minutos")
    if time.time() - tempo_inicio == 7200:
        print("Passaram 120 minutos")
    if time.time() - tempo_inicio == 10800:
        print("Passaram 180 minutos")
        break

    grafo_aleatorio = Grafo.gerar_grafo_aleatorio(numero_vertices)
    x = grafo_aleatorio.coloração_de_grafos()
    print(f'Quantidade de cores: {x}')
    numero_vertices+= 1
'''
