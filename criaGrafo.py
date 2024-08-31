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
