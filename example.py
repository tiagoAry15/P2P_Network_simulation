import networkx as nx
import matplotlib.pyplot as plt

# Criação do grafo
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])

# Algoritmo de busca (exemplo: busca em largura)
search_algorithm = nx.bfs_edges

# Visualização passo a passo
pos = nx.spring_layout(G)
fig, ax = plt.subplots()

for edge in search_algorithm(G, 1):
    ax.clear()

    # Desenha o grafo
    nx.draw_networkx(G, pos, with_labels=True, ax=ax)

    # Destaca a aresta atual
    nx.draw_networkx_edges(G, pos, edgelist=[edge], width=2.0, edge_color='red', ax=ax)

    plt.pause(1)  # Pausa por 1 segundo para visualização

plt.show()

