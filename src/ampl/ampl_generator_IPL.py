import json
import pandas as pd
import numpy as np
import shutil
import os

# Results are stored on a specific folder
folder_name = 'scenario1_N8_classical'
# Check if folder exists and creates if not
if not os.path.exists('results/' + folder_name):
    os.makedirs('results/' + folder_name)
# Check if folder exists and creates if not
if not os.path.exists('src/ampl/' + folder_name):
    os.makedirs('src/ampl/' + folder_name)

# Step 1: Get parameters N, q, B, P, tickers, sigma, and mu from data
f = open('data/out_diversified_N8_p1mo_i1d.json')
data = json.load(f)

N = data['N']               # Universe size
B = int(N * 0.5)            # Budget
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

q_values = list(np.linspace(10.44, 10.56, num=9, endpoint=False))

for q in q_values:
    print('q usado:')
    print(q)
    # Step 2: Create ampl file from both linearized and IPL_linearized templates
    shutil.copy2('src/ampl/IPL_linearized_template.ampl',
                 f'src/ampl/{folder_name}/IPL_linearized_N{N}q{q:.2f}B{B}.ampl')

    with open(f'src/ampl/{folder_name}/IPL_linearized_N{N}q{q:.2f}B{B}.ampl', 'a') as f:
        solution_file_name = f'results/{folder_name}/IPL_linearized_N{N}q{q:.2f}B{B}_solution.json'

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
