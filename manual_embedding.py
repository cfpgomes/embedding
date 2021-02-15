from dwave.system import DWaveSampler, FixedEmbeddingComposite
from dwave.embedding.chimera import find_clique_embedding
import dimod
import dwave.inspector
import matplotlib.pyplot as plt
import networkx as nx
import dwave_networkx as dnx

bqm = dimod.BQM({}, {('s0', 's1'): -1, ('s0', 's2'): -1,
                     ('s1', 's2'): 1}, 0, dimod.Vartype.SPIN)

embedding = find_clique_embedding(['s0', 's1', 's2'], 2)

print(embedding)


# D-Wave 2000Q
plt.ion()
G = dnx.chimera_graph(16, 16, 4)
dnx.draw_chimera(G)

#sampler = FixedEmbeddingComposite(DWaveSampler(solver={'qpu': True}), embedding=)

#sampleset = sampler.sample(bqm, num_reads=1000)

#dwave.inspector.show(sampleset)