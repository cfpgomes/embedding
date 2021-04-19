from dwave.system import DWaveSampler
from dwave.embedding.pegasus import find_clique_embedding
import matplotlib.pyplot as plt
import dwave_networkx as dnx
import json

# Step 1: Get parameters N from data
with open('data/out_diversified_N8_p1mo_i1d.json') as f:
    data = json.load(f)

    N = int(data['N'])               # Universe size

    # Step 2: Find clique embedding
    sampler = DWaveSampler()

    embedding = find_clique_embedding(
        N, target_graph=sampler.to_networkx_graph())
    print(embedding)

    # Draw the embedding
    dnx.draw_pegasus_embedding(
        sampler.to_networkx_graph(), embedding, unused_color=None)
    plt.savefig(f'images/embedding_cliqueN{N}.png')

    # Step 3: Store embedding to data.
    with open(f'data/embedding_cliqueN{N}.json', 'w') as ff:
        json.dump(embedding, ff)
