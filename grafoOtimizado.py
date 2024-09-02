import random


class Grafo:
  def __init__(self, vertices):
    self.vertices = vertices
    self.grafo = [[] for _ in range(self.vertices)]

  def adiciona_aresta(self, u, v):
    self.grafo[u-1].append(v)
    self.grafo[v-1].append(u)

  def imprime_grafo(self):
    for i in range(self.vertices):
        print(f'{i+1}:', end='  ')        
        for j in self.grafo[i]:
            print(f'{j} ->', end='  ')
        print('')

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

  # Função para calcular o grau de cada vértice
  def calcular_graus(self):
    graus = []
    for i in range(self.vertices):
        graus.append((i, len(self.grafo[i])))  # (vértice, grau)
    return graus

  # Implementação do Merge Sort para ordenar os vértices por grau
  def merge_sort(self, arr):
    if len(arr) > 1:
      meio = len(arr) // 2
      esquerda = arr[:meio]
      direita = arr[meio:]

      # Chama o Merge Sort recursivamente nas metades
      self.merge_sort(esquerda)
      self.merge_sort(direita)

      # Mescla as duas metades ordenadas
      i = j = k = 0

      while i < len(esquerda) and j < len(direita):
          # Ordena em ordem decrescente de grau
          if esquerda[i][1] > direita[j][1]:
              arr[k] = esquerda[i]
              i += 1
          else:
              arr[k] = direita[j]
              j += 1
          k += 1

      # Copia os elementos restantes
      while i < len(esquerda):
          arr[k] = esquerda[i]
          i += 1
          k += 1

      while j < len(direita):
          arr[k] = direita[j]
          j += 1
          k += 1

  def coloração_de_grafos_otimizado(self):
    # Calcula o grau de cada vértice
    graus = self.calcular_graus()

    # Ordena os vértices por grau (ordem decrescente)
    self.merge_sort(graus)

    # Inicializa todas as cores como -1 (sem cor)
    cor = [-1] * self.vertices

    # Atribui a primeira cor ao primeiro vértice na lista ordenada
    cor[graus[0][0]] = 0

    # Array para verificar a disponibilidade de cores
    cores_utilizadas = [False] * self.vertices

    # Atribui cores aos vértices restantes na ordem dos graus
    for v, _ in graus:
        # Marque as cores dos vizinhos como indisponíveis
        for vizinho in self.grafo[v]:
            if cor[vizinho-1] != -1:  # Verifica se o vértice já está colorido
                cores_utilizadas[cor[vizinho-1]] = True

        # Encontre a primeira cor disponível
        primeira_cor_disponivel = 0
        while primeira_cor_disponivel < self.vertices and cores_utilizadas[primeira_cor_disponivel]:
            primeira_cor_disponivel += 1

        # Atribui a menor cor disponível ao vértice v
        cor[v] = primeira_cor_disponivel

        # Redefine a lista de cores disponíveis para a próxima iteração
        cores_utilizadas = [False] * self.vertices

    # Retorna o array de cores para verificar a coloração
    return cor

