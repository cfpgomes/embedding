import json
import pandas as pd

# To formulate QUBO
from collections import defaultdict

# To run QUBO
from dwave.system import DWaveSampler, FixedEmbeddingComposite

# Five steps:
# 1. Get parameters N, q, B, P, tickers, sigma, and mu from data
# 2. Formulate QUBO
# 3. Solve it.

# Step 1: Get parameters N, q, B, P, tickers, sigma, and mu from data
f = open(f'data/out_industry_diversified_N64_p1mo_i1d.json')
data = json.load(f)

N = data['N']               # Universe size
tickers = data['tickers']   # Tickers
mu = pd.Series(data['mu'])
sigma = pd.DataFrame.from_dict(data['sigma'], orient='index')

B = 32

q_values = [0, 0.2, 0.4, 0.6, 1.1, 1.3, 1.5, 2, 5, 6, 7, 8, 10, 100, 500]

min_sigma = 0
for i in range(N):
    for j in range(i+1, N):
        if sigma[tickers[i]][tickers[j]] < 0:
            min_sigma += sigma[tickers[i]][tickers[j]]

max_mu = 0
for i in range(N):
    if mu[tickers[i]] > 0:
        max_mu += mu[tickers[i]]

# Get embedding
f = open('data/embedding_normalN64.json')
embedding = json.load(f)
embedding = {int(k): [int(i) for i in v] for k, v in embedding.items()}

composite = FixedEmbeddingComposite(DWaveSampler(), embedding=embedding)

for q in q_values:
    # Step 2: Formulate QUBO
    Q = defaultdict(float)

    P = -q * min_sigma + max_mu

    # There are three terms in the objective function: Covariance, Return, and Budget

    # Covariance term
    for i in range(N):
        for j in range(i, N):
            Q[(i, j)] = float(q * sigma[tickers[i]][tickers[j]])

    # Return term
    for i in range(N):
        Q[(i, i)] += float(-mu[tickers[i]])

    # Budget term is decomposed into four terms, per the formula ((sum^{n-1}_{i=0} x_i) - B)^2
    for i in range(N):
        Q[(i, i)] += float(P)

    for i in range(N):
        for j in range(i + 1, N):
            Q[(i, j)] += float(2*P)

    for i in range(N):
        Q[(i, i)] += float(-2 * B * P)

    # Step 3: Solve QUBO
    sampleset = composite.sample_qubo(Q, num_reads=1000)

    sampleset.to_pandas_dataframe().sort_values(
        by=['energy']).to_csv('results/out.csv', index=False)
