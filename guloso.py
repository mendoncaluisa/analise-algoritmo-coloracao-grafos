# Nome(s) Discente(s): Maria Luísa Mendonça Oliveira, Poliana Cristina de Sousa
# Matrícula(s): 0049545, 0056154
# Data: agosto de 2024


# Declaro que sou o único autor e responsável por este programa. Todas as partes do programa, exceto as que
# foram fornecidas pelo professor foram desenvolvidas por mim. Declaro também que
# sou responsável por todas  as eventuais cópias deste programa e que não distribui nem facilitei a #distribuição de cópias.


import random
import time


class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for _ in range(self.vertices)] #inicializa a lista de vertices com as listas de adjacencia de cada vertice (inicialmente vazias)

    def adiciona_aresta(self, u, v):
        # estamos considerando um grafo não direcionado
        # grafo[u-1] corresponde à posicao do vertice u na lista. Ex: se o verice u é o vertice 1, a posicao 0 da lista coresponde a esse vértice u, portanto grafo[u-1] receberá os grafos adjacentes a u
        self.grafo[u - 1].append(v)  # adiciona o vertice v como adjacente do vertice u
        self.grafo[v - 1].append(u)  # adiciona o vertice u como adjacente do vertice v

    def imprime_grafo(self):
        for i in range(self.vertices):
            print(f'{i + 1}  ->', end='  ')  # end não quebra a linha
            for j in self.grafo[i]:  # percorre a lista de adjacencia do grafo[i]
                print(f'{j} ->', end='  ')
            print('')  # para pular para a proxima linha

    @staticmethod
    def gerar_grafo_aleatorio(numero_vertices):
        grafo = Grafo(numero_vertices)
        if numero_vertices < 2:
            return grafo

        # Começando com o primeiro vértice (1) e adicionando mais vértices
        for novo_vertice in range(2, numero_vertices + 1):
            # Escolhe um ou mais vértices aleatórios já existentes para conectar ao novo vértice
            vertices_existentes = range(1, novo_vertice)
            numero_arestas = random.randint(1, len(vertices_existentes))  # Número aleatório de arestas

            vizinhos = random.sample(vertices_existentes, numero_arestas)
            for vizinho in vizinhos:
                grafo.adiciona_aresta(novo_vertice, vizinho)

        return grafo

    def coloracao_gulosa(self):
        # Inicializa todas as cores como -1 (sem cor)

        cor = [-1] * self.vertices

        # Atribui a primeira cor ao primeiro vértice
        cor[0] = 0

        # Array para verificar a disponibilidade de cores (Se for False, não está usando a cor)
        cores_utilizadas = [False] * self.vertices

        # Atribui cores aos vértices restantes
        for u in range(0, self.vertices):
            # Marque as cores dos vizinhos como indisponíveis
            for vizinho in self.grafo[u]:
                if cor[vizinho - 1] != -1:  # Verifica se vértice ja esta colorido
                    cores_utilizadas[cor[vizinho - 1]] = True

            # Encontre a primeira cor disponível
            primeira_cor_disponivel = 0
            # se cores_utilizadas[primeira_cor_disponivel] for False, o vertice nessa posicao nao esta usando a cor e ela não sera incrementada. Ele manterá a cor e poderá usar ela
            while primeira_cor_disponivel < self.vertices and cores_utilizadas[primeira_cor_disponivel]:
                primeira_cor_disponivel += 1

            # Atribui a menor cor disponível ao vértice u
            cor[u] = primeira_cor_disponivel

            # Redefine a lista de cores disponíveis para a próxima iteração
            cores_utilizadas = [False] * self.vertices

        # Retorna o array de cores para verificar a coloração
        return cor


