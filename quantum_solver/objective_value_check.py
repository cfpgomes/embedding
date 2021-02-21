import numpy as np
import json
import pandas as pd

# Step 1: Get parameters N, q, B, P, tickers, sigma, and mu from data
f = open('outN20q1B10P100.json')
data = json.load(f)

N = data['N']               # Universe size
q = data['q']               # Risk appetite
B = data['B']               # Budget
P = data['P']               # Penalization factor
tickers = data['tickers']   # Tickers
mu = pd.Series(data['mu']).to_numpy()
sigma = pd.DataFrame.from_dict(data['sigma'], orient='index').to_numpy()

solution = np.array([1,1,0,1,0,0,1,1,0,0,1,1,0,0,0,1,1,0,1,0])
#solution = np.array([1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,0,1,0])

print(q*np.transpose(solution).dot(sigma).dot(solution))

print(-np.transpose(mu).dot(solution))

print(P * np.square(np.ones((1,20)).dot(solution) - B))

print(q*np.transpose(solution).dot(sigma).dot(solution) - np.transpose(mu).dot(solution) + P * np.square(np.ones((1,20)).dot(solution) - B))