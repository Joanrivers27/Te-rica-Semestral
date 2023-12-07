# Importando las bibliotecas necesarias
import networkx as nx
import matplotlib.pyplot as plt

# Creando una figura para visualizar el grafo
fig = plt.figure(figsize=(12, 12))
ax = plt.subplot(111)

# Definiendo nodos (variables)
Ola = "Ola"
La_Pintada = "La_Pintada"
Nata = "Nata"
Anton = "Anton"
Aguadulce = "Aguadulce"
Penonome = "Penonome"

# Añadiendo nodos al grafo
G = nx.Graph()
G.add_node(Ola)
G.add_node(La_Pintada)
G.add_node(Nata)
G.add_node(Anton)
G.add_node(Aguadulce)
G.add_node(Penonome)

# Definiendo conexiones y pesos entre nodos
G.add_edge(Ola, La_Pintada, weight=18)
G.add_edge(Ola, Anton, weight=22)
G.add_edge(Nata, Aguadulce, weight=52)
G.add_edge(Aguadulce, Penonome, weight=38)
G.add_edge(La_Pintada, Nata, weight=36)
G.add_edge(La_Pintada, Penonome, weight=19)
G.add_edge(Anton, Penonome, weight=65)

# Configurando el diseño y la visualización del grafo
posiciones = nx.spring_layout(G)
nx.draw(G, posiciones, node_size=1300, node_color='red', font_size=10, font_weight='bold', with_labels=True)

# Atributos del grafo y etiquetas de las aristas (pesos)
pesos = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, posiciones, edge_labels=pesos)

# Solicitando las rutas de inicio y destino al usuario
punto_partida = input("Ingrese el punto de partida: ")
punto_destino = input("Ingrese el punto de destino: ")

# Aplicando el algoritmo de Dijkstra para encontrar la ruta más corta y su distancia
ruta_mas_corta = nx.shortest_path(G, punto_partida, punto_destino, weight='weight')
distancia_total = nx.shortest_path_length(G, punto_partida, punto_destino, weight='weight')

# Configurando el título del grafo con la información de la ruta más corta
titulo = f"La ruta más corta es: {ruta_mas_corta} y tiene una distancia de {distancia_total} km"
ax.set_title(titulo, fontsize=10)

# Guardando el grafo como PNG
plt.tight_layout()
plt.savefig("Grafo.png", format="PNG")

# Mostrando el grafo visualmente
plt.show()
