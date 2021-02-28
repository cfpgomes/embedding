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

returns = []
risks = []
colors = []

x0 = 0
x1 = 0
for x2 in range(2):
    for x3 in range(2):
        for x4 in range(2):
            for x5 in range(2):
                for x6 in range(2):
                    for x7 in range(2):
                        for x8 in range(2):
                            for x9 in range(2):
                                for x10 in range(2):
                                    for x11 in range(2):
                                        for x12 in range(2):
                                            for x13 in range(2):
                                                for x14 in range(2):
                                                    for x15 in range(2):
                                                        for x16 in range(2):
                                                            for x17 in range(2):
                                                                for x18 in range(2):
                                                                    for x19 in range(2):
                                                                        best_solution = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19]
                                                                        if sum(best_solution) != B:
                                                                            continue

                                                                        portfolio_return = 0
                                                                        portfolio_risk = 0

                                                                        for i in range(N):
                                                                            portfolio_return += best_solution[i] * \
                                                                                mu[tickers[i]]
                                                                            portfolio_risk += best_solution[i] * sigma[tickers[i]
                                                                                                                    ][tickers[i]] * sigma[tickers[i]][tickers[i]]

                                                                        portfolio_return /= N

                                                                        for i in range(N):
                                                                            for j in range(i+1, N):
                                                                                portfolio_risk += 2 * best_solution[i] * \
                                                                                    best_solution[j] * \
                                                                                        sigma[tickers[i]
                                                                                            ][tickers[j]]

                                                                        returns.append(
                                                                            portfolio_return)
                                                                        risks.append(
                                                                            portfolio_risk)
                                                                        colors.append(
                                                                            '#0000ff')  # blue

                                                                        print(f'{x1}{x2}{x3}{x4}{x5}{x6}{x7}{x8}{x9}{x10}{x11}{x12}{x13}{x14}{x15}{x16}{x17}{x18}{x19}')

x0 = 0
x1 = 1
for x2 in range(2):
    for x3 in range(2):
        for x4 in range(2):
            for x5 in range(2):
                for x6 in range(2):
                    for x7 in range(2):
                        for x8 in range(2):
                            for x9 in range(2):
                                for x10 in range(2):
                                    for x11 in range(2):
                                        for x12 in range(2):
                                            for x13 in range(2):
                                                for x14 in range(2):
                                                    for x15 in range(2):
                                                        for x16 in range(2):
                                                            for x17 in range(2):
                                                                for x18 in range(2):
                                                                    for x19 in range(2):
                                                                        best_solution = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19]
                                                                        if sum(best_solution) != B:
                                                                            continue

                                                                        portfolio_return = 0
                                                                        portfolio_risk = 0

                                                                        for i in range(N):
                                                                            portfolio_return += best_solution[i] * \
                                                                                mu[tickers[i]]
                                                                            portfolio_risk += best_solution[i] * sigma[tickers[i]
                                                                                                                    ][tickers[i]] * sigma[tickers[i]][tickers[i]]

                                                                        portfolio_return /= N

                                                                        for i in range(N):
                                                                            for j in range(i+1, N):
                                                                                portfolio_risk += 2 * best_solution[i] * \
                                                                                    best_solution[j] * \
                                                                                        sigma[tickers[i]
                                                                                            ][tickers[j]]

                                                                        returns.append(
                                                                            portfolio_return)
                                                                        risks.append(
                                                                            portfolio_risk)
                                                                        colors.append(
                                                                            '#0000ff')  # blue

                                                                        print(f'{x1}{x2}{x3}{x4}{x5}{x6}{x7}{x8}{x9}{x10}{x11}{x12}{x13}{x14}{x15}{x16}{x17}{x18}{x19}')

x0 = 1
x1 = 0
for x2 in range(2):
    for x3 in range(2):
        for x4 in range(2):
            for x5 in range(2):
                for x6 in range(2):
                    for x7 in range(2):
                        for x8 in range(2):
                            for x9 in range(2):
                                for x10 in range(2):
                                    for x11 in range(2):
                                        for x12 in range(2):
                                            for x13 in range(2):
                                                for x14 in range(2):
                                                    for x15 in range(2):
                                                        for x16 in range(2):
                                                            for x17 in range(2):
                                                                for x18 in range(2):
                                                                    for x19 in range(2):
                                                                        best_solution = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19]
                                                                        if sum(best_solution) != B:
                                                                            continue

                                                                        portfolio_return = 0
                                                                        portfolio_risk = 0

                                                                        for i in range(N):
                                                                            portfolio_return += best_solution[i] * \
                                                                                mu[tickers[i]]
                                                                            portfolio_risk += best_solution[i] * sigma[tickers[i]
                                                                                                                    ][tickers[i]] * sigma[tickers[i]][tickers[i]]

                                                                        portfolio_return /= N

                                                                        for i in range(N):
                                                                            for j in range(i+1, N):
                                                                                portfolio_risk += 2 * best_solution[i] * \
                                                                                    best_solution[j] * \
                                                                                        sigma[tickers[i]
                                                                                            ][tickers[j]]

                                                                        returns.append(
                                                                            portfolio_return)
                                                                        risks.append(
                                                                            portfolio_risk)
                                                                        colors.append(
                                                                            '#0000ff')  # blue

                                                                        print(f'{x1}{x2}{x3}{x4}{x5}{x6}{x7}{x8}{x9}{x10}{x11}{x12}{x13}{x14}{x15}{x16}{x17}{x18}{x19}')

x0 = 1
x1 = 1
for x2 in range(2):
    for x3 in range(2):
        for x4 in range(2):
            for x5 in range(2):
                for x6 in range(2):
                    for x7 in range(2):
                        for x8 in range(2):
                            for x9 in range(2):
                                for x10 in range(2):
                                    for x11 in range(2):
                                        for x12 in range(2):
                                            for x13 in range(2):
                                                for x14 in range(2):
                                                    for x15 in range(2):
                                                        for x16 in range(2):
                                                            for x17 in range(2):
                                                                for x18 in range(2):
                                                                    for x19 in range(2):
                                                                        best_solution = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19]
                                                                        if sum(best_solution) != B:
                                                                            continue

                                                                        portfolio_return = 0
                                                                        portfolio_risk = 0

                                                                        for i in range(N):
                                                                            portfolio_return += best_solution[i] * \
                                                                                mu[tickers[i]]
                                                                            portfolio_risk += best_solution[i] * sigma[tickers[i]
                                                                                                                    ][tickers[i]] * sigma[tickers[i]][tickers[i]]

                                                                        portfolio_return /= N

                                                                        for i in range(N):
                                                                            for j in range(i+1, N):
                                                                                portfolio_risk += 2 * best_solution[i] * \
                                                                                    best_solution[j] * \
                                                                                        sigma[tickers[i]
                                                                                            ][tickers[j]]

                                                                        returns.append(
                                                                            portfolio_return)
                                                                        risks.append(
                                                                            portfolio_risk)
                                                                        colors.append(
                                                                            '#0000ff')  # blue

                                                                        print(f'{x1}{x2}{x3}{x4}{x5}{x6}{x7}{x8}{x9}{x10}{x11}{x12}{x13}{x14}{x15}{x16}{x17}{x18}{x19}')

fig, ax=plt.subplots()

ax.scatter(risks, returns, c=colors, marker='o')

ax.set(xlabel='Risk', ylabel='Return',
       title='Risk vs Return')
ax.grid()

plt.xlim([0, 0.4])
plt.ylim([0, 0.04])

fig.savefig('images/markowitzN{}B{}P{}.png'.format(N, B, P))
plt.show()
