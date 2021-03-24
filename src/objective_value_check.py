import numpy as np
import json
import pandas as pd

# Step 1: Get parameters N, q, B, P, tickers, sigma, and mu from data
f = open('data/outN50q1B25P100.json')
data = json.load(f)

N = data['N']               # Universe size
q = data['q']               # Risk appetite
B = data['B']               # Budget
P = data['P']               # Penalization factor
tickers = data['tickers']   # Tickers
mu = pd.Series(data['mu']).to_numpy()
sigma = pd.DataFrame.from_dict(data['sigma'], orient='index').to_numpy()

# IPL Solver
ipl_solution = np.zeros(50)
ipl_solution[3-1] = 1
ipl_solution[6-1] = 1
ipl_solution[8-1] = 1
ipl_solution[11-1] = 1
ipl_solution[12-1] = 1
ipl_solution[13-1] = 1
ipl_solution[15-1] = 1
ipl_solution[16-1] = 1
ipl_solution[17-1] = 1
ipl_solution[19-1] = 1
ipl_solution[20-1] = 1
ipl_solution[24-1] = 1
ipl_solution[26-1] = 1
ipl_solution[27-1] = 1
ipl_solution[28-1] = 1
ipl_solution[30-1] = 1
ipl_solution[33-1] = 1
ipl_solution[35-1] = 1
ipl_solution[36-1] = 1
ipl_solution[41-1] = 1
ipl_solution[43-1] = 1
ipl_solution[46-1] = 1
ipl_solution[47-1] = 1
ipl_solution[49-1] = 1
ipl_solution[50-1] = 1

# Dwave
solution = np.zeros(50)
solution[3-1]= 1
solution[6-1]= 1
solution[8-1]= 1
solution[11-1]=1 
solution[12-1]=1
solution[13-1]=1 
solution[15-1]=1 
solution[16-1]=1
solution[17-1]=1 
solution[19-1]=1 
solution[20-1]=1 
solution[24-1]=1 
solution[26-1]=1 
solution[28-1]=1 
solution[30-1]=1 
solution[33-1]=1 
solution[35-1]=1
solution[36-1]=1 
solution[41-1]=1 
solution[43-1]=1 
solution[45-1]=1 
solution[46-1]=1 
solution[47-1]=1 
solution[49-1]=1 
solution[50-1]=1 

print("1111:")
print(q*np.transpose(ipl_solution).dot(sigma).dot(ipl_solution) - np.transpose(mu).dot(ipl_solution) + P * np.square(np.ones((1,N)).dot(ipl_solution) - B))

print("6:")
print(q*np.transpose(solution).dot(sigma).dot(solution) - np.transpose(mu).dot(solution) + P * np.square(np.ones((1,N)).dot(solution) - B))

print('P calculado:')

min_sigma = 0
max_sigma = 0
for i in range(N):
    for j in range(i+1, N):
        if sigma[i][j] < 0:
            min_sigma += sigma[i][j]
        else:
            max_sigma += sigma[i][j]

max_mu = 0
min_mu = 0
for i in range(N):
    if mu[i] > 0:
        max_mu += mu[i]
    else:
        min_mu += mu[i]

print(-q * min_sigma + max_mu)



print('q maximo calculado:')
print(max_mu/min_sigma)