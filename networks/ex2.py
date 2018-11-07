import createnetwork
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

spls=[]
cls=[]

for a in range(100):
    probability=10**(-4*(1-a/float(100)))
    G=[createnetwork.small_world(250,k=4,prob=probability) for b in range(10)]
    clustering=sum(nx.algorithms.cluster.average_clustering(G))/float(10)
    shortestpathlength=nx.algorithms.shortest_paths.generic.average_shortest_path_length(G)/float(10)
    spls.append(shortestpathlength)
    cls.append(clustering)

spls=[spls[x]/spls[0] for x in range(len(spls))]
cls=[cls[x]/cls[0] for x in range(len(cls))]

i=[x/float(100) for x in range(100)]
plt.figure()
plt.semilogx(i,cls,"ro")
plt.semilogx(i,spls,"bo")
plt.savefig("testing.png")


