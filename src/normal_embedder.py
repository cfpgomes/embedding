from dwave.system import DWaveSampler
from minorminer import find_embedding
import networkx as nx
import json

# Step 1: Get parameters N from data
with open('data/outN20q1B10P100.json') as f:
    data = json.load(f)

    N = int(data['N'])  # Universe size

    # Step 2: Find normal embedding
    embedding = find_embedding(nx.complete_graph(
        N).edges(), DWaveSampler().edgelist)
    print(embedding)

    # Step 3: Store embedding to data.
    with open("data/embedding_normalN{}.json".format(N), "w") as ff:
        json.dump(embedding, ff)
