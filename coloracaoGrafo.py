def coloracao_gulosa(grafo):
    # Inicializa o dicionário para armazenar a cor de cada nó
    coloracao = {}
    
    # Percorre todos os nós no grafo
    for no in grafo.nodes():
        # Obtem as cores dos vizinhos do nó atual
        vizinhos_cores = {coloracao.get(vizinho) for vizinho in grafo.neighbors(no) if vizinho in coloracao}
        
        # Encontra a primeira cor disponível
        cor_disponivel = 0
        while cor_disponivel in vizinhos_cores:
            cor_disponivel += 1
        
        # Atribui a cor disponível ao nó atual
        coloracao[no] = cor_disponivel
    
    return coloracao

