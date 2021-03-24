import json
import pandas as pd
import numpy as np
import shutil

# Step 1: Get parameters N, q, B, P, tickers, sigma, and mu from data
f = open('data/outN50q1B25P100.json')
data = json.load(f)

N = data['N']               # Universe size
B = data['B']               # Budget
tickers = data['tickers']   # Tickers
print(tickers)
mu = pd.Series(data['mu'])
sigma = pd.DataFrame.from_dict(data['sigma'], orient='index')

min_sigma = 0
for i in range(N):
    for j in range(i+1, N):
        if sigma[tickers[i]][tickers[j]] < 0:
            min_sigma += sigma[tickers[i]][tickers[j]]

max_mu = 0
for i in range(N):
    if mu[i] > 0:
        max_mu += mu[tickers[i]]

print('q maximo calculado:')
print(int(-max_mu/min_sigma)+1)

for q in range(0, 12):
    P = -q * min_sigma + max_mu
    print('P calculado:')
    print(P)
    print('q usado:')
    print(q)
    # Step 2: Create ampl file from both linearized and IPL_linearized templates
    shutil.copy2('src/ampl/IPL_linearized_template.ampl',
                'src/ampl/testingQ/IPL_linearized_N{}q{:.2f}B{}P{}.ampl'.format(N, q, B, P))

    with open('src/ampl/testingQ/IPL_linearized_N{}q{:.2f}B{}P{}.ampl'.format(N, q, B, P), 'a') as f:
        solution_file_name = 'results/testingQ/IPL_linearized_N{}q{:.2f}B{}P{}_solution.json'.format(
            N, q, B, P)

        f.write('printf: "{{ ""solution"": [%d", x[1] > "{}";\n'.format(
            solution_file_name))
        f.write('printf{{i in 2..n}}: ",%d", x[i] >> "{}";\n'.format(
            solution_file_name))
        f.write('printf: "]}}" >> "{}";\n'.format(solution_file_name))

        f.write('\n#data:\ndata;\n\n')
        f.write('param n := {};\n'.format(N))
        f.write('param q := {};\n'.format(q))
        f.write('param B := {};\n'.format(B))

        f.write('param mu :=')
        for i in range(N):
            f.write('\n{} {}'.format(i+1, mu[tickers[i]]))
        f.write(';\n')

        f.write('param sigma :')
        for i in range(N):
            f.write(' {}'.format(i+1))
        f.write(' :=')

        for i in range(N):
            f.write('\n{}'.format(i+1))
            for j in range(N):
                f.write(' {}'.format(sigma[tickers[i]][tickers[j]]))

        f.write(';\nend;\n')
