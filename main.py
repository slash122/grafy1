import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from parse import *
from graph import * 

print("Wpisz macierz sąsiedztwa, po wpisaniu macierzy naciśnij enter 2 razy:")

input_type = input("Jak chcesz wprowadzić graf? (1 - macierz sąsiedztwa, 2 - lista sąsiedztwa, 3 - macierz incydencji)\n")
input_string = multiline_input()

# Wejście:
# Macierz incydencji:
# a11 a12 ... a1n
# ... ... ... ...
# an1 an2 ... ann
#
# Lista sąsiedztwa (v1 - idx wierzchołka, a1, a2, ... an - idx wierzchołków sąsiednich):
# v1 a1 a2 ... an
# ...
# vn a1 a2 ... an
# 
# Macierz incydencji (wiersze - wierzchołki, kolumny - krawędzie, 1 - wierzchołek jest końcem krawędzi, 0 - nie jest końcem krawędzi):
# l11 l12 ... l1m
# ... ... ... ...
# ln1 ln2 ... lnm


G: nx.Graph
match input_type:
    case "1":
        matrix = parse_matrix(input_string)
        G = nx.from_numpy_array(np.array(matrix))
    case "2":
        adj_list = parse_adjacency_list(input_string)
        G = nx.from_dict_of_lists(adj_list)
    case "3":
        matrix = parse_matrix(input_string)
        np_matrix = incidence_to_adjacency(np.array(matrix))
        for row in np_matrix:
            print(row)
        G = nx.from_numpy_array(np.array(np_matrix))
    case _:
        print("Niepoprawna opcja")
        exit()

# Rysowanie grafu za pomocą matplotlib
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()

while True:
    option = input("""Do jakiej postaci chcesz przekonwertować graf? 
(1 - macierz sąsiedztwa, 2 - lista sąsiedztwa, 3 - macierz incydencji, 4 - exit\n""")
    match option:
        case "1":
            print("Macierz sąsiedztwa:")
            print(nx.to_numpy_array(G))
        case "2":
            print("Lista sąsiedztwa:")
            print(nx.to_dict_of_lists(G))
        case "3":
            print("Macierz incydencji:")
            print(nx.incidence_matrix(G).todense()) 
        case "4":
            exit()
        case _:
            print("Niepoprawna opcja")
            continue
    print("\n")