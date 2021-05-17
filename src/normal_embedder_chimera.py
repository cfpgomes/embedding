from dwave.system import DWaveSampler
from minorminer import find_embedding
import networkx as nx
import dwave_networkx as dnx
import matplotlib.pyplot as plt
import json

# Step 1: Get parameters N from data
with open('data/out_industry_diversified_N64_p1mo_i1d.json') as f:
    data = json.load(f)

    N = int(data['N'])  # Universe size

    # Step 2: Find normal embedding
    sampler = DWaveSampler()
    
    embedding = find_embedding(nx.complete_graph(
        N).edges(), sampler.edgelist)
    print(embedding)

    # Step 3: Store embedding to data.
    with open(f'data/embedding_chimera_normalN{N}.json', 'w') as ff:
        json.dump(embedding, ff)
