import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from parse import * 

print("Wpisz macierz sąsiedztwa, po wpisaniu macierzy naciśnij enter 2 razy:")
input_string = multiline_input()
matrix = parse_matrix(input_string)

for row in matrix:
    print(row)
print("\n")

G = nx.from_numpy_array(np.array(matrix)) #Bez numpy nie działa

nx.draw(G, with_labels=True, font_weight='bold')
plt.show()

while True:
    option = input("""Do jakiej postaci chcesz przekonwertować graf? 
(1 - macierz sąsiedztwa, 2 - lista sąsiedztwa, 3 - macierz incydencji, 4 - exit\n""")
    
    match option:
        case "1":
            print("Macierz sąsiedztwa:")
            print(matrix)
        case "2":
            print("Lista sąsiedztwa:")
            print(nx.to_dict_of_lists(G))
        case "3":
            print("Macierz incydencji:")
            print(nx.incidence_matrix(G).todense())
        case "4":
            break
        case _:
            print("Niepoprawna opcja")
            continue
    print("\n")