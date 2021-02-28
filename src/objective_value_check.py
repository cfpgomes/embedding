import numpy as np
import json
import pandas as pd

# Step 1: Get parameters N, q, B, P, tickers, sigma, and mu from data
f = open('data/outN20q1B10P100.json')
data = json.load(f)

N = data['N']               # Universe size
q = data['q']               # Risk appetite
B = data['B']               # Budget
P = data['P']               # Penalization factor
tickers = data['tickers']   # Tickers
mu = pd.Series(data['mu']).to_numpy()
sigma = pd.DataFrame.from_dict(data['sigma'], orient='index').to_numpy()

# IPL Solver
ipl_solution = np.array([1,1,0,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,1,1])

# Dwave
solution = np.array([0,1,0,1,0,1,1,1,0,0,1,1,0,0,0,1,1,0,1,0])

print("IPL:")
print(q*np.transpose(ipl_solution).dot(sigma).dot(ipl_solution) - np.transpose(mu).dot(ipl_solution) + P * np.square(np.ones((1,20)).dot(ipl_solution) - B))

print("Dwave:")
print(q*np.transpose(solution).dot(sigma).dot(solution) - np.transpose(mu).dot(solution) + P * np.square(np.ones((1,20)).dot(solution) - B))