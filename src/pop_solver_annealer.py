import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# To formulate QUBO
from collections import defaultdict

# To run QUBO
from dwave.system import DWaveSampler, FixedEmbeddingComposite
import dwave.inspector
import dwave_networkx as dnx

# Five steps:
# 1. Get parameters N, q, B, P, tickers, sigma, and mu from data
# 2. Formulate QUBO
# 3. Solve it.

# Step 1: Get parameters N, q, B, P, tickers, sigma, and mu from data
f = open('data/outN50q1B25P100.json')
data = json.load(f)

N = data['N']               # Universe size
#q = data['q']               # Risk appetite
B = data['B']               # Budget
#P = data['P']               # Penalization factor
tickers = data['tickers']   # Tickers
mu = pd.Series(data['mu'])
sigma = pd.DataFrame.from_dict(data['sigma'], orient='index')

#print('q B P: {} {} {}'.format(q, B, P))
print('mu vector:')
print(mu)
print('sigma matrix:')
print(sigma)

q = 1
P = 10

# Step 2: Formulate QUBO
Q = defaultdict(float)

# There are three terms in the objective function: Covariance, Return, and Budget

# Covariance term
for i in range(N):
    for j in range(i, N):
        Q[(str(i), str(j))] = float(q * sigma[tickers[i]][tickers[j]])

# Return term
for i in range(N):
    Q[(str(i), str(i))] += float(-mu[tickers[i]])

# Budget term is decomposed into four terms, per the formula ((sum^{n-1}_{i=0} x_i) - B)^2
for i in range(N):
    Q[(str(i), str(i))] += float(P)

for i in range(N):
    for j in range(i + 1, N):
        Q[(str(i), str(j))] += float(2*P)

for i in range(N):
    Q[(str(i), str(i))] += float(-2 * B * P)

print('QUBO Matrix')
print(Q)

# Step 3: Solve QUBO

# Get sampler
sampler = DWaveSampler()
embedding_type = 'clique'

# Get embedding
f = open(f'data/embedding_{embedding_type}N{N}.json')
embedding = json.load(f)
print(embedding)

# Draw the embedding
dnx.draw_pegasus_embedding(
    sampler.to_networkx_graph(), embedding, unused_color=None)
plt.savefig(f'images/embedding_{embedding_type}N{N}q{q:.2f}B{B}P{P:.3f}.png')

# Chain_strength is a guessed value. Good rule of thumb is to have the same order of magnitude as Q.
chain_strength = 100

composite = FixedEmbeddingComposite(sampler, embedding=embedding)
sampleset = composite.sample_qubo(
    Q, num_reads=1000, chain_strength=chain_strength)
dwave.inspector.show(sampleset)
sampleset.to_pandas_dataframe().sort_values(
        by=['energy']).to_csv(f'results/out_{embedding_type}N{N}q{q:.2f}B{B}P{P:.3f}C{chain_strength:.3f}.csv', index=False)
