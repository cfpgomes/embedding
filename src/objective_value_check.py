import numpy as np
import json
import pandas as pd
from more_itertools import distinct_permutations


def get_volatility(sol, N, B, sigma):
    return np.transpose(sol).dot(sigma).dot(sol)


def get_expected_return(sol, N, B, mu):
    return np.transpose(mu).dot(sol)


# Step 1: Get parameters N, q, B, P, tickers, sigma, and mu from data
f = open('data/out_diversified_N64_p1mo_i1d.json')
data = json.load(f)

N = data['N']               # Universe size
q = 1
B = int(N*0.5)
tickers = data['tickers']   # Tickers
mu = pd.Series(data['mu']).to_numpy()
sigma = pd.DataFrame.from_dict(data['sigma'], orient='index').to_numpy()

solution = np.zeros(50)

min_sigma = 0
max_sigma = 0
for i in range(N):
    for j in range(i+1, N):
        if sigma[i][j] < 0:
            min_sigma += sigma[i][j]
        else:
            max_sigma += sigma[i][j]

max_mu = 0
for i in range(N):
    if mu[i] > 0:
        max_mu += mu[i]

P = -q * min_sigma + max_mu

expected_return = []
volatility = []

tmp = [1] * B + [0] * (64-B)
print(tmp)

for sol in distinct_permutations(tmp):
    expected_return.append(get_expected_return(sol, N, B, mu))
    volatility.append(get_volatility(sol, N, B, sigma))

with open('all_solutions_64.json', 'w') as ff:
    json.dump({
        'ret': expected_return,
        'vol': volatility
    }, ff)
