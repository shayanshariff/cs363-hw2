import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from networkx.algorithms.approximation import average_clustering
from thinkstats2 import Pmf
import thinkplot 


#Apart from the repetition(n, p) function, the rest are either all directly taken or slightly adapted from Allen Downey's Think Complexity 2e

#first configuration
n = 1000
p = 0.2


#second configuration
#n = 500
#p = 0.8

#third configuration
#n = 3000
#p = 0.4

def generate_graph(n, p):
    graph = nx.binomial_graph(n, p)
    return graph

def degrees(G):
    return [G.degree(u) for u in G]

def avg_degrees(G):
    return np.average([G.degree(u) for u in G])

def sample_path_lengths(G, nodes=None, trials=1):
    if nodes is None:
        nodes = list(G)
    else:
        nodes = list(nodes)

    pairs = np.random.choice(nodes, (trials, 2))
    lengths = [nx.shortest_path_length(G, *pair) for pair in pairs]
    return np.average(lengths)


def repetition(n, p):
    degr = 0
    clust = 0
    path = 0
    for i in range(30):
        g = generate_graph(n, p)
        degr += avg_degrees(g)
        clust += average_clustering(g)
        path += sample_path_lengths(g)
    degr = degr/30
    clust = clust/30
    path = path/30
    print(degr)
    print(clust)
    print(path)
    pmf_g = Pmf(degrees(g))
    thinkplot.Pdf(pmf_g, label='Degree')
    thinkplot.Show()

repetition(n, p)

