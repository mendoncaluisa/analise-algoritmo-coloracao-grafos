# Nome(s) Discente(s): Maria Luísa Mendonça Oliveira, Poliana Cristina de Sousa
# Matrícula(s): 0049545,
# Data: agosto de 2024


# Declaro que sou o único autor e responsável por este programa. Todas as partes do programa, exceto as que 
# foram fornecidas pelo professor foram desenvolvidas por mim. Declaro também que
# sou responsável por todas  as eventuais cópias deste programa e que não distribui nem facilitei a #distribuição de cópias.

import random
import networkx as nx
import matplotlib.pyplot as plt

def gera_grafo_aleatorio(vertices):
    # Cria um grafo vazio
    G = nx.Graph()
    
    # Adiciona os vértices ao grafo
    G.add_nodes_from(range(vertices))
    
    # Adiciona arestas aleatórias
    for i in range(vertices):
        for j in range(i + 1, vertices):
            if random.choice([True, False]):
                G.add_edge(i, j)
    
    return G

# Desenha o grafo gerado
# nx.draw(grafo, with_labels=True)
# plt.show()
