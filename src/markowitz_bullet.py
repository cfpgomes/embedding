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
colors = []
solutions = []
objectives = []
risks = []
labels = []
file_num = 0

for filename in os.listdir('results'):
    if 'cliquewithchain512_chimera.csv' in filename:
        ff = open('results/' + filename)

        start = filename.rfind('q')
        end = filename.rfind('B')

        print('File #{}: \tCSV \t{}'.format(
            file_num, filename))

        rets = []
        rsks = []

        for best_solution_line in ff.readlines()[1:]:
            best_solution = []
            for i in range(N):
                best_solution.append(int(best_solution_line[i*2]))

            num_occur = int(best_solution_line.split(',')[-1])

            # if sum(best_solution) != B:
            #     continue

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

            for i in range(num_occur):
                returns.append(portfolio_return)
                risks.append(portfolio_risk)
                solutions.append(best_solution)
                objectives.append(q*np.transpose(best_solution).dot(sigma).dot(best_solution) - np.transpose(mu).dot(best_solution) + P * np.square(np.ones((1,20)).dot(best_solution) - B))
                rets.append(portfolio_return)
                rsks.append(portfolio_risk)
                labels.append(filename[start:end])
                if sum(best_solution) != B:
                    colors.append('#000000') # black
                else: 
                    colors.append('#ff0000') # red
            #break # Remove comment to show best solution only

        print('Average Return: {}'.format(sum(rets) / len(rets)))
        print('Average Risk: {}'.format(sum(rsks) / len(rsks)))
        file_num += 1
    # elif '.json' in filename:
    #     ff = open('results/' + filename)
    #     best_solution = json.load(ff)["solution"]

    #     start = filename.find('q')
    #     end = filename.find('B')

    #     print('File #{}: \tJSON \t{} \t{}'.format(
    #         file_num, filename[start:end], best_solution))

    #     portfolio_return = 0
    #     portfolio_risk = 0

    #     for i in range(N):
    #         portfolio_return += best_solution[i] * mu[tickers[i]]
    #         portfolio_risk += best_solution[i] * sigma[tickers[i]
    #                                                    ][tickers[i]] * sigma[tickers[i]][tickers[i]]

    #     portfolio_return /= N

    #     for i in range(N):
    #         for j in range(i+1, N):
    #             portfolio_risk += 2 * best_solution[i] * \
    #                 best_solution[j] * sigma[tickers[i]][tickers[j]]

    #     returns.append(portfolio_return)
    #     risks.append(portfolio_risk)
    #     labels.append(filename[start:end])
    #     colors.append('#0000ff')
    #     file_num += 1

fig, ax = plt.subplots()

ax.scatter(risks, returns, c=colors, marker='o')

ax.set(xlabel='Risk', ylabel='Return',
       title='Risk vs Return')
ax.grid()

# for i, label in enumerate(labels):
#     ax.annotate(label, (risks[i], returns[i]))

plt.xlim([0, 0.4])
plt.ylim([0, 0.04])

fig.savefig('images/markowitzN{}B{}P{}.png'.format(N, B, P))
plt.show()

fig, ax = plt.subplots()



ax.scatter(list(range(len(objectives))), objectives, c=colors)
val, idx = min((val, idx) for (idx, val) in enumerate(objectives))
print(f'{val},{idx},{solutions[idx]}')

plt.ylim([-10, 1000])
plt.xlim([-10, 1010])
ax.set(xlabel='Index of solutions', ylabel='Objective Value',
       title='Value of solutions')
ax.grid()
plt.show()
