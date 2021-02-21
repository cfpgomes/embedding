import json
import pandas as pd

# To formulate QUBO
from collections import defaultdict

# To run QUBO
from dwave.system import DWaveSampler, EmbeddingComposite
from dwave.embedding.pegasus import find_clique_embedding
import dwave.inspector

# Five steps:
# 1. Get parameters N, q, B, P, tickers, sigma, and mu from data
# 2. Formulate QUBO
# 3. Solve it.

# Step 1: Get parameters N, q, B, P, tickers, sigma, and mu from data
f = open('outN20q1B10P100.json')
data = json.load(f)

N = data['N']               # Universe size
q = data['q']               # Risk appetite
B = data['B']               # Budget
P = data['P']               # Penalization factor
tickers = data['tickers']   # Tickers
mu = pd.Series(data['mu'])
sigma = pd.DataFrame.from_dict(data['sigma'], orient='index')

# mu = [0.8, 0.4, 0.3, 0.4, 0.5, 0.6, 0.1, 0.2, 0.7, 0.1,
#       0.8, 0.4, 0.2, 0.9, 0.1, 0.4, 0.5, 0.9, 0.6, 0.4]

# sigma = [[2, 0, 8, 1, 0, 6, 3, 2, 2, 0, 9, 0, 3, 5, 7, 7, 4, 3, 8, 3],
#          [0, 6, 7, 0, 7, 4, 4, 0, 8, 7, 3, 4, 2, 5, 0, 0, 7, 8, 2, 2],
#          [8, 7, 3, 9, 3, 2, 6, 3, 0, 0, 7, 5, 4, 8, 1, 0, 5, 0, 7, 6],
#          [1, 0, 9, 9, 9, 9, 6, 3, 8, 7, 2, 8, 1, 0, 2, 6, 6, 6, 6, 9],
#          [0, 7, 3, 9, 7, 4, 6, 6, 2, 7, 5, 4, 5, 2, 9, 8, 8, 0, 5, 0],
#          [6, 4, 2, 9, 4, 0, 7, 3, 2, 7, 8, 1, 0, 4, 3, 3, 1, 5, 3, 6],
#          [3, 4, 6, 6, 6, 7, 3, 7, 5, 3, 2, 9, 3, 6, 2, 2, 7, 5, 8, 8],
#          [2, 0, 3, 3, 6, 3, 7, 3, 4, 8, 3, 9, 8, 0, 1, 5, 7, 3, 2, 1],
#          [2, 8, 0, 8, 2, 2, 5, 4, 9, 0, 9, 6, 9, 7, 1, 4, 9, 6, 2, 9],
#          [0, 7, 0, 7, 7, 7, 3, 8, 0, 0, 7, 2, 1, 3, 6, 6, 5, 9, 3, 0],
#          [9, 3, 7, 2, 5, 8, 2, 3, 9, 7, 4, 2, 4, 9, 1, 4, 4, 2, 6, 0],
#          [0, 4, 5, 8, 4, 1, 9, 9, 6, 2, 2, 4, 4, 1, 6, 4, 7, 6, 0, 6],
#          [3, 2, 4, 1, 5, 0, 3, 8, 9, 1, 4, 4, 3, 2, 3, 7, 9, 4, 7, 0],
#          [5, 5, 8, 0, 2, 4, 6, 0, 7, 3, 9, 1, 2, 1, 9, 2, 7, 4, 4, 9],
#          [7, 0, 1, 2, 9, 3, 2, 1, 1, 6, 1, 6, 3, 9, 4, 4, 4, 3, 1, 1],
#          [7, 0, 0, 6, 8, 3, 2, 5, 4, 6, 4, 4, 7, 2, 4, 6, 9, 0, 4, 9],
#          [4, 7, 5, 6, 8, 1, 7, 7, 9, 5, 4, 7, 9, 7, 4, 9, 0, 9, 8, 9],
#          [3, 8, 0, 6, 0, 5, 5, 3, 6, 9, 2, 6, 4, 4, 3, 0, 9, 6, 0, 9],
#          [8, 2, 7, 6, 5, 3, 8, 2, 2, 3, 6, 0, 7, 4, 1, 4, 8, 0, 3, 9],
#          [3, 2, 6, 9, 0, 6, 8, 1, 9, 0, 0, 6, 0, 9, 1, 9, 9, 9, 9, 3]]

print('q B P: {} {} {}'.format(q, B, P))
print('mu vector:')
print(mu)
print('sigma matrix:')
print(sigma)

# Step 2: Formulate QUBO
Q = defaultdict(float)

# There are three terms in the objective function: Covariance, Return, and Budget

# Covariance term
for i in range(N):
    for j in range(i, N):
        Q[(tickers[i], tickers[j])] = float(q * sigma[tickers[i]][tickers[j]])

# Return term
for i in range(N):
    Q[(tickers[i], tickers[i])] += float(-mu[tickers[i]])

# Budget term is decomposed into four terms, per the formula ((sum^{n-1}_{i=0} x_i) - B)^2
for i in range(N):
    Q[(tickers[i], tickers[i])] += float(P)

for i in range(N):
    for j in range(i + 1, N):
        Q[(tickers[i], tickers[j])] += float(2*P)

for i in range(N):
    Q[(tickers[i], tickers[i])] += float(-2 * B * P)

print('QUBO Matrix')
print(Q)

# Step 3: Solve QUBO
sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample_qubo(Q, num_reads=100)

dwave.inspector.show(sampleset)
sampleset.to_pandas_dataframe().sort_values(
    by=['energy']).to_csv('outP' + str(P) + '.csv', index=False)
