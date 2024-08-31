# Nome(s) Discente(s): Maria Luísa Mendonça Oliveira, Poliana Cristina de Sousa
# Matrícula(s): 0049545, 
# Data: agosto de 2024


# Declaro que sou o único autor e responsável por este programa. Todas as partes do programa, exceto as que 
# foram fornecidas pelo professor foram desenvolvidas por mim. Declaro também que
# sou responsável por todas  as eventuais cópias deste programa e que não distribui nem facilitei a #distribuição de cópias.

######/Leia e depois apague  os comentários abaixo #############

# Escreva um comentário no início do arquivo fonte para indicar O QUE o código faz
# Coloque comentários no seu código de modo a explicar o que está sendo feito
# Se utilizar ou basear seu código em alguma fonte externa, explicite este fato.

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

