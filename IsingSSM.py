import numpy as np

from randomdistributions import dynamicalmethods


def square_lattice(L):
    Neigh = []
    for i in range(L):
        for j in range(L):
            i_up, i_down = i+1, i-1
            j_right, j_left = j+1, j-1
            if i == L-1:
                i_up = 0
            elif i == 0:
                i_down = L-1
            if j == (L-1):
                j_right = 0
            elif j == 0:
                j_left = L-1
            Neigh.append(L*i_up+j)
            Neigh.append(L*i_down+j)
            Neigh.append(L*i+j_right)
            Neigh.append(L*i+j_left)
    return Neigh


def probability(K, s1, s2):
    return np.exp(-2*K*s1*s2)
