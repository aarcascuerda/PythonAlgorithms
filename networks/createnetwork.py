import networkx as nx
import random as ran
import math


def pref_atatchment(N, m=1):
    '''Creates a network using preferential attachment algorithm.

    It can takes the number of output nodes and the number of starting nodes.
    '''
    G = nx.Graph()
    for i in range(m):
        G.add_edge(i, i+1)

    for n in range(m+1, N):
        Edges = G.size()
        Pc = 0.0
        x = ran.random()
        for j in range(n):
            Pc += G.degree[j]/(2*Edges)
            if x < Pc:
                G.add_edge(n, j)
                print(n, j)
                break
    return G


def small_world(N, k=2, prob=0):
    '''Method to create a Watts-Strogatz Network.

    It returns and object with a network of "N" nodes, "k" rightmost neighbors and "prob" the probability of rewiring. The network is created following the Watts-Strogatz Network.
    '''
    G = nx.Graph()
    for t in range(2):
        for i in range(N):
            for j in range(i+1, i+1+int(k/2)):
                if j < N:
                    if t == 0:
                        G.add_edge(i, j)
                    # has_edge is the same as j in G[i] but without exceptions
                    elif t == 1 and ran.random() <= prob and G.has_edge(i, j) == True:
                        while True:
                            choose = int(ran.random()*(N-1))
                            if (i+choose) < N and G.has_edge(i, i+1+choose) == False:
                                G.remove_edge(i, j)
                                G.add_edge(i, i+1+choose)
                                print(i, j, i+choose+1, "N<")
                                break
                            elif (i+choose) >= N and G.has_edge(i, i+1+choose-N) == False:
                                G.remove_edge(i, j)
                                G.add_edge(i, i+1+choose-N)
                                print(i, j, i+choose+1-N, "N")
                                break
                elif j >= N:
                    if t == 0:
                        G.add_edge(i, j-N)
                    elif t == 1 and ran.random() <= prob and G.has_edge(i, j-N) == True:
                        while True:
                            choose = int(ran.random()*(N-1))
                            if (i+choose) < N and G.has_edge(i, i+1+choose) == False:
                                G.remove_edge(i, j-N)
                                G.add_edge(i, i+1+choose)
                                print(i, j-N, i+choose+1, "N<")
                                break
                            elif (i+choose) >= N and G.has_edge(i, i+1+choose-N) == False:
                                G.remove_edge(i, j-N)
                                G.add_edge(i, i+1+choose-N)
                                print(i, j-N, i+choose+1-N, "N")
                                break
    return G
