from dwave.system import DWaveSampler
import minorminer.layout as mml
import networkx as nx
import dwave_networkx as dnx
import matplotlib.pyplot as plt
import json

# Step 1: Get parameters N from data
with open('data/out_diversified_N16_p1mo_i1d.json') as f:
    data = json.load(f)

    N = int(data['N'])  # Universe size

    # Step 2: Find layout embedding
    sampler = DWaveSampler()
    
    embedding = mml.find_embedding(nx.complete_graph(
        N), sampler.to_networkx_graph())
    print(embedding)

    # Draw the embedding
    dnx.draw_pegasus_embedding(
        sampler.to_networkx_graph(), embedding, unused_color=None)
    plt.savefig(f'images/embedding_layoutN{N}.png')

    # Step 3: Store embedding to data.
    with open(f'data/embedding_layoutN{N}.json', 'w') as ff:
        json.dump(embedding, ff)
