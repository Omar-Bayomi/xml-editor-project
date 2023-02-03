import pandas as pd
import networkx as nx
import numpy as np
import scipy
from pyvis.network import Network
import community as community_louvain
import matplotlib.pyplot as plt
import uuid


def directed_visuals(users):
    # Calculate all possible user combinations
    source = []
    target = []
    for user in users:
        for follower in users[user].followers:
            source.append(users[user].id)
            target.append(follower.id)

    df = pd.DataFrame(np.array([source, target]).T, columns=['Source', 'Target'])
    # df=pd.DataFrame(np.array([["A","B",50],["B","A",15],["C","A",30],["D","A",23],["D","E",53],["F","B",20],["A","G",16],["H","A",12],["E","A",22],["I","J",30],["F","I",10000],["J","E",1]]),columns=["Source","Target","Value"])
    graph = nx.from_pandas_edgelist(df, source="Source", target="Target", edge_attr=None, create_using=nx.DiGraph())
    plt.figure(figsize=(10, 10))
    pos = nx.kamada_kawai_layout(graph)
    node_degree = dict(graph.degree)
    nx.draw(graph, with_labels=True, node_color="skyblue", edge_cmap=plt.cm.Blues, pos=pos,
            node_size=[v * 100 for v in node_degree.values()])
    FileName = uuid.uuid4().hex
    plt.savefig(FileName + ".png")
    network = Network(width="1000px", height="700px", bgcolor="#222222", font_color="white",directed=True)
    network.from_nx(graph)
    network.show(FileName + ".html")
    return FileName + ".png"


