import stocks_retriever
import pandas as pd

# To formulate QUBO
from collections import defaultdict

# To run QUBO
from dwave.system import DWaveSampler, EmbeddingComposite
import dwave.inspector

# Five steps:
# 1. Download data
# 2. Get parameters sigma and mu
# 3. Set q and B
# 4. Formulate QUBO
# 5. Solve it.

# Step 1: Download data

## Get tickers
table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
tickers = list(table[0]['Symbol'])[:150] ## Alphabetically first 150 indexes are used. TODO: Change method of choosing stocks.

N = len(tickers)
period = '1y'
interval = '1d'
print('Tickers used')
print(N)
print(list(tickers))

## Retrieve data about the tickers
data = stocks_retriever.get_data(tickers, period, interval)
print('Market data')
print(data)

# Step 2: Get parameters sigma and mu
sigma, mu = stocks_retriever.get_sigma_and_mu_from_tickers(data)

print('mu vector')
print(mu)
print('sigma matrix')
print(sigma)

# Step 3: Set q and B
q = 1
B = 50

# Step 4: Formulate QUBO
Q = defaultdict(int)

# There are three terms in the objective function: Covariance, Return, and Budget

# Covariance term
for i in range(N):
    for j in range(i, N):
        Q[(i, j)] += q * sigma[tickers[i]][tickers[j]]

# Return term
for i in range(N):
    Q[(i, i)] += -mu[tickers[i]]

# Budget term is decomposed into four terms, per the formula ((sum^{n-1}_{i=0} x_i) - B)^2
for i in range(N):
    Q[(i, i)] += (2 * B) - 1

for i in range(N):
    for j in range(i + 1, N):
        Q[(i, j)] += -2

#print('QUBO Matrix')
#print(Q)

# Execute QUBO
sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample_qubo(Q, num_reads=100)

dwave.inspector.show(sampleset)
print(sampleset)
