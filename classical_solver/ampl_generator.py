import json
import pandas as pd
import shutil

# Step 1: Get parameters N, q, B, P, tickers, sigma, and mu from data
f = open('outN20q1B10P100.json')
data = json.load(f)

N = data['N']               # Universe size
q = data['q']               # Risk appetite
B = data['B']               # Budget
P = data['P']               # Penalization factor
tickers = data['tickers']   # Tickers
print(tickers)
mu = pd.Series(data['mu'])
sigma = pd.DataFrame.from_dict(data['sigma'], orient='index')

# Step 2: Create ampl file from both linearized and IPL_linearized templates
shutil.copy2('classical_solver\IPL_linearized_template.ampl','IPL_linearized_N{}q{}B{}P{}.ampl'.format(N,q,B,P))
shutil.copy2('classical_solver\linearized_template.ampl','linearized_N{}q{}B{}P{}.ampl'.format(N,q,B,P))

with open('IPL_linearized_N{}q{}B{}P{}.ampl'.format(N,q,B,P), 'a') as f:
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

with open('linearized_N{}q{}B{}P{}.ampl'.format(N,q,B,P), 'a') as f:
    f.write('\n#data:\ndata;\n\n')
    f.write('param n := {};\n'.format(N))
    f.write('param q := {};\n'.format(q))
    f.write('param B := {};\n'.format(B))
    f.write('param P := {};\n'.format(P))

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