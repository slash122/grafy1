import re #regular expressions


# Zwraca string z wieloma wprowadzanymi liniami 
def multiline_input():
    result = ""
    while True:
        line = input()
        if line.strip() == "":
            break 
        result += line + "\n"
    return result


# Dla macierzy sąsiedztwa lub incydencji
def parse_matrix(matrix_string: str):
    matrix = []

    for row in matrix_string.splitlines():
        parsed_row = []
        
        for value in re.split(r",| ", row): #Zostawia "" więc trzeba to wykluczyć niżej
            if value == "":
                continue
            if not value.isdigit() or (value != "0" and value != "1"):
                raise ValueError("Wrong value in matrix!")
            parsed_row.append(int(value))  
        
        matrix.append(parsed_row)
    
    return matrix


# Nie działa
def parse_adjacency_list(list_string: str): 
    adjacency_list = {}
    
    for line in list_string.split(r"\n|;"):
        if not line.isdigit():
            raise ValueError("Non-integer value in list")
        
        vertex, *adjacent_vertices = map(int, line.split(r",| "))
        adjacency_list[vertex] = adjacent_vertices
    
    return adjacency_list




