import networkx as nx
import random as ran


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
                if j >= N:
                    j = j-N
                if t == 0:
                    G.add_edge(i, j)
                elif t == 1 and ran.random() <= prob and G.has_edge(i, j) == True:
                    while True:
                        choose = int(ran.random()*(N-1))
                        if (i+1+choose) >= N:
                            choose = choose - N
                        if G.has_edge(i, i+1+choose) == False:
                            G.remove_edge(i, j)
                            G.add_edge(i, i+1+choose)
#                           print(i, j, i+choose+1)
                            break
    return G
