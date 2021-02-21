from dwave.system import DWaveSampler, FixedEmbeddingComposite
from dwave.embedding.pegasus import find_clique_embedding
import dimod
import dwave.inspector
import networkx as nx
import dwave_networkx as dnx

bqm = dimod.BQM({}, {('s0', 's1'): -1, ('s0', 's2'): -1,
                     ('s1', 's2'): 1}, 0, dimod.Vartype.SPIN)

embedding = find_clique_embedding(['s0', 's1', 's2'], 2)

print(embedding)


# D-Wave 2000Q

sampler = FixedEmbeddingComposite(DWaveSampler(solver={'qpu': True}), embedding=embedding)

sampleset = sampler.sample(bqm, num_reads=1000)

#dwave.inspector.show(sampleset)