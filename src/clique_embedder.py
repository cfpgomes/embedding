from dwave.system import DWaveSampler
from dwave.embedding.pegasus import find_clique_embedding
import json

# Step 1: Get parameters N from data
with open('data/outN20q1B10P100.json') as f:
    data = json.load(f)

    N = int(data['N'])               # Universe size

    # Step 2: Find clique embedding
    embedding = find_clique_embedding(
        N, target_graph=DWaveSampler().to_networkx_graph())
    print(embedding)

    # Step 3: Store embedding to data.
    with open("data/embedding_cliqueN{}.json".format(N), "w") as ff:
        json.dump(embedding, ff)
