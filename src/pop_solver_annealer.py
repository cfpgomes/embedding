import json
import pandas as pd
import numpy as np
import os

# To formulate QUBO
from collections import defaultdict

# To run QUBO
from dwave.system import DWaveSampler, FixedEmbeddingComposite
import dwave.inspector

# To print variables:


def print_var(variable_name, variable):
    print(f'{variable_name}:\n{variable}')

# Five steps:
# 1. Get parameters N, q, B, P, tickers, sigma, and mu from data
# 2. Formulate QUBO
# 3. Solve it.


# Results are stored on a specific folder
folder_name = 'scenario1_N64_annealer'
# Check if folder exists and creates if not
if not os.path.exists('results/' + folder_name):
    os.makedirs('results/' + folder_name)

# Step 1: Get parameters N, q, B, P, tickers, sigma, and mu from data
f = open('data/out_diversified_N64_p1mo_i1d.json')
data = json.load(f)

N = data['N']               # Universe size
tickers = data['tickers']   # Tickers
mu = pd.Series(data['mu'])
sigma = pd.DataFrame.from_dict(data['sigma'], orient='index')

print_var('mu', mu)
print_var('sigma', sigma)

B = int(N * 0.5)
print_var('B', B)

q_values = [1.1, 1.3, 1.5]
print_var('q_values', q_values)

min_sigma = 0
for i in range(N):
    for j in range(i+1, N):
        if sigma[tickers[i]][tickers[j]] < 0:
            min_sigma += sigma[tickers[i]][tickers[j]]

max_mu = 0
for i in range(N):
    if mu[tickers[i]] > 0:
        max_mu += mu[tickers[i]]

# Get sampler
sampler = DWaveSampler()
embedding_type = 'normal'

# Get embedding
f = open(f'data/embedding_{embedding_type}N{N}.json')
embedding = json.load(f)
print_var('embedding', embedding)

# Chain_strength is a guessed value. Good rule of thumb is to have the same order of magnitude as Q.
chain_strength = 200

composite = FixedEmbeddingComposite(sampler, embedding=embedding)

for q in q_values:
    # Step 2: Formulate QUBO
    Q = defaultdict(float)

    P = -q * min_sigma + max_mu

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

    print_var('Q', Q)

    # Step 3: Solve QUBO
    sampleset = composite.sample_qubo(Q, num_reads=1000)

    chain_strength = sampleset.info['embedding_context']['chain_strength']
    dwave.inspector.show(sampleset)
    sampleset.to_pandas_dataframe().sort_values(
        by=['energy']).to_csv(f'results/{folder_name}/out_{embedding_type}N{N}q{q:.2f}B{B}P{P:.3f}C{chain_strength}.csv', index=False)
