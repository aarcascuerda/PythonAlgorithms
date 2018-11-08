import createnetwork
import matplotlib.pyplot as plt
import networkx as nx

spls = []
cls = []
xprob = []

for a in range(100):
    if a != 0:
        probability = 10**(-4*(1-a/float(100)))
    elif a == 0:
        probability = 0
    G = [createnetwork.small_world(250, k=4, prob=probability)
         for b in range(10)]
    clustering = 0.0
    shortestpathlength = 0.0
    for i in range(10):
        clustering += nx.algorithms.cluster.average_clustering(G[i])/float(10)
        shortestpathlength += nx.algorithms.shortest_paths.generic.average_shortest_path_length(
            G[i])/float(10)
    spls.append(shortestpathlength)
    cls.append(clustering)
    xprob.append(probability)

spls = [spls[x]/spls[0] for x in range(len(spls))]
cls = [cls[x]/cls[0] for x in range(len(cls))]

plt.figure()
plt.semilogx(xprob, cls, "ro")
plt.semilogx(xprob, spls, "bo")
plt.savefig("testing.png")
