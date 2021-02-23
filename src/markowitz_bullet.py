import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd
import os

# Step 1: Get parameters N, q, B, P, tickers, sigma, and mu from data
f = open('data/outN20q1B10P100.json')
data = json.load(f)

N = data['N']               # Universe size
q = data['q']               # Risk appetite
B = data['B']               # Budget
P = data['P']               # Penalization factor
tickers = data['tickers']   # Tickers
mu = pd.Series(data['mu'])
sigma = pd.DataFrame.from_dict(data['sigma'], orient='index')

returns_annealer = []
risks_annealer = []
labels_annealer = []
returns_classical = []
risks_classical = []
labels_classical = []
file_num = 0

for filename in os.listdir('results'):
    if '.csv' in filename:
        ff = open('results/' + filename)
        best_solution_line = ff.readlines()[1]

        best_solution = []
        for i in range(N):
            best_solution.append(int(best_solution_line[i*2]))

        start = filename.find('q')
        end = filename.find('B')

        print('File #{}: \tCSV \t{} \t{}'.format(
            file_num, filename[start:end], best_solution))

        portfolio_return = 0
        portfolio_risk = 0

        for i in range(N):
            portfolio_return += best_solution[i] * mu[tickers[i]]
            portfolio_risk += best_solution[i] * sigma[tickers[i]
                                                       ][tickers[i]] * sigma[tickers[i]][tickers[i]]

        portfolio_return /= N

        for i in range(N):
            for j in range(i+1, N):
                portfolio_risk += 2 * best_solution[i] * \
                    best_solution[j] * sigma[tickers[i]][tickers[j]]

        returns_annealer.append(portfolio_return)
        risks_annealer.append(portfolio_risk)
        labels_annealer.append(filename[start:end])
        file_num += 1

    elif '.json' in filename:
        ff = open('results/' + filename)
        best_solution = json.load(ff)["solution"]

        start = filename.find('q')
        end = filename.find('B')

        print('File #{}: \tJSON \t{} \t{}'.format(
            file_num, filename[start:end], best_solution))

        portfolio_return = 0
        portfolio_risk = 0

        for i in range(N):
            portfolio_return += best_solution[i] * mu[tickers[i]]
            portfolio_risk += best_solution[i] * sigma[tickers[i]
                                                       ][tickers[i]] * sigma[tickers[i]][tickers[i]]

        portfolio_return /= N

        for i in range(N):
            for j in range(i+1, N):
                portfolio_risk += 2 * best_solution[i] * \
                    best_solution[j] * sigma[tickers[i]][tickers[j]]

        returns_classical.append(portfolio_return)
        risks_classical.append(portfolio_risk)
        labels_classical.append(filename[start:end])
        file_num += 1

fig, ax = plt.subplots()

colors = []
for i in range(len(risks_annealer)):
    colors.append('#ff0000')
for i in range(len(risks_classical)):
    colors.append('#0000ff')

ax.scatter(risks_annealer + risks_classical, returns_annealer + returns_classical, c=colors, marker='o')

ax.set(xlabel='Risk (Variance)', ylabel='Return',
       title='Risk vs Return')
ax.grid()

for i, label in enumerate(labels_annealer+labels_classical):
    ax.annotate(label, ((risks_annealer + risks_classical)[i], (returns_annealer + returns_classical)[i]))

plt.xlim([0, 0.3])
plt.ylim([0, 0.03])

fig.savefig('images/markowitzN{}B{}P{}.png'.format(N, B, P))
plt.show()
