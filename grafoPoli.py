class Grafo:

    # GRAFO = [  [[2,preto],[3,amarelo]],  [[3,amarelo]],  [[1,azul],[2,preto],[3,amarelo]],  [[1,azul]]  ]
    def __init__(self, vertices):
        self.vertices = vertices #quantidade de vertices
        self.grafo = [[] for i in range(self.vertices)] #lista de adjacencia (inicialmente criamos uma lista de listas vazias)


    def adiciona_aresta(self, u, v, cor):
        #estamos considerando um grafo não direcionado
        #grafo[u-1] corresponde à posicao do vertice u na lista. Ex: se o verice u é o vertice 1, a posicao 0 da lista coresponde a esse vértice u, portanto grafo[u-1] receberá os grafos adjacentes a u
        self.grafo[u-1].append([v,cor]) #adiciona o vertice v como adjacente do vertice u
        self.grafo[v-1].append([u,cor]) #adiciona o vertice u como adjacente do vertice v

    def mostra_lista(self):
        for i in range(self.vertices):
            print(f'{i+1}  ->', end='  ') #end não quebra a linha
            for j in self.grafo[i]: #percorre a lista de adjacencia do grafo[i]
                print(f'{j} ->', end='  ')
            print('') #para pular para a proxima linha

g = Grafo(4)
g.adiciona_aresta(1,2, None)
g.adiciona_aresta(1,3, None)
g.adiciona_aresta(1,4, None)
g.adiciona_aresta(2,3, None)

g.mostra_lista()

