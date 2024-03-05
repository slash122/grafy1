import numpy as np

def incidence_to_adjacency(incedence_matrix):
    tmp = np.dot(incedence_matrix, incedence_matrix.T)
    for i in range(tmp.shape[0]):
        tmp[i][i] = 0
    return tmp
    
    