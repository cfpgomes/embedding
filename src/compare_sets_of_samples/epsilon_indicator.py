import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from datetime import datetime
import os
import json
import csv


def equals_budget(sol, N, B):
    return np.ones((1, N)).dot(sol) - B == 0


def get_expected_return(sol, N, B, mu):
    return np.transpose(mu).dot(sol)


def get_objective_value(sol, N, B, mu, sigma):
    return np.transpose(sol).dot(sigma).dot(sol) - np.transpose(mu).dot(sol) + P * np.square(np.ones((1, N)).dot(sol) - B)


def get_volatility(sol, N, B, sigma):
    return np.transpose(sol).dot(sigma).dot(sol)


work_id = 0
N = None
q = 1
B = None
P = 100
mu = None
sigma = None

data_filename = 'data/outN20q1B10P100.json'
with open(data_filename) as jsonfile:
    data = json.load(jsonfile)
    N = data['N']               # Universe size
    B = data['B']               # Budget
    mu = pd.Series(data['mu']).to_numpy()
    sigma = pd.DataFrame.from_dict(data['sigma'], orient='index').to_numpy()

classical_solutions_foldername = 'results/N20B10'
classical_solutions = []

for filename in os.listdir(classical_solutions_foldername):
    with open(classical_solutions_foldername+'/'+filename) as jsonfile:
        data = json.load(jsonfile)
        classical_solutions.append({'sol': data['solution'], 'objective': get_objective_value(data['solution'], N, B, mu, sigma), 'expected_return': get_expected_return(
            data['solution'], N, B, mu), 'volatility': get_volatility(data['solution'], N, B, sigma), 'equals_budget': equals_budget(data['solution'], N, B)})

set1_foldername = 'results/outnormalN20B10'
set2_foldername = 'results/outcliqueN20B10'

set1_samples = []
set2_samples = []

for filename in os.listdir(set1_foldername):
    with open(set1_foldername+'/'+filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader, None)  # Skip header
        for row in reader:
            sol = np.array(list(map(float, row[:-3])))
            for _ in range(int(row[-1])):
                set1_samples.append({'sol': sol, 'objective': get_objective_value(sol, N, B, mu, sigma), 'expected_return': get_expected_return(
                    sol, N, B, mu), 'volatility': get_volatility(sol, N, B, sigma), 'equals_budget': equals_budget(sol, N, B)})

for filename in os.listdir(set2_foldername):
    with open(set2_foldername+'/'+filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader, None)  # Skip header
        for row in reader:
            sol = np.array(list(map(float, row[:-3])))
            for _ in range(int(row[-1])):
                set2_samples.append({'sol': sol, 'objective': get_objective_value(sol, N, B, mu, sigma), 'expected_return': get_expected_return(
                    sol, N, B, mu), 'volatility': get_volatility(sol, N, B, sigma), 'equals_budget': equals_budget(sol, N, B)})

# 2 columns, 9 per 6 inches figure
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(9, 6))

set1_dominating_samples = list(
    filter(lambda x: x['equals_budget'], set1_samples))
set2_dominating_samples = list(
    filter(lambda x: x['equals_budget'], set2_samples))

set1_dominating_samples = list(filter(lambda x: not any(
    (x['expected_return'] < y['expected_return'] and x['volatility'] > y['volatility']) for y in set1_dominating_samples), set1_dominating_samples))
set2_dominating_samples = list(filter(lambda x: not any(
    (x['expected_return'] < y['expected_return'] and x['volatility'] > y['volatility']) for y in set2_dominating_samples), set2_dominating_samples))

ax1.scatter(list(map(lambda x: x['volatility'], set1_dominating_samples)), list(
    map(lambda x: x['expected_return'], set1_dominating_samples)), color='red', label='normal')
ax1.scatter(list(map(lambda x: x['volatility'], classical_solutions)), list(
    map(lambda x: x['expected_return'], classical_solutions)), color='blue', label='classical')

ax2.scatter(list(map(lambda x: x['volatility'], set2_dominating_samples)), list(
    map(lambda x: x['expected_return'], set2_dominating_samples)), color='red', label='clique')
ax2.scatter(list(map(lambda x: x['volatility'], classical_solutions)), list(
    map(lambda x: x['expected_return'], classical_solutions)), color='blue', label='classical')


ax1_epsilon = 0
for solution in classical_solutions:
    tmp = float('inf')
    for sample in set1_dominating_samples:
        tmp = min(tmp, max(sample['expected_return'] / solution['expected_return'],
                  sample['volatility']/solution['volatility']))
    ax1_epsilon = max(ax1_epsilon, tmp)

ax2_epsilon = 0
for solution in classical_solutions:
    tmp = float('inf')
    for sample in set2_dominating_samples:
        tmp = min(tmp, max(sample['expected_return'] / solution['expected_return'],
                  sample['volatility']/solution['volatility']))
    ax2_epsilon = max(ax2_epsilon, tmp)

# Tidy up the figure
(_, ax1_right) = ax1.get_xlim()
(_, ax2_right) = ax2.get_xlim()
(_, ax1_top) = ax1.get_ylim()
(_, ax2_top) = ax2.get_ylim()

right = max(ax1_right, ax2_right)
top = max(ax1_top, ax2_top)

ax1.grid(True)
ax1.set_xlim(0, right)
ax1.set_ylim(0, top)
ax1.legend()
ax1.set_title(f'ε = {ax1_epsilon}')
ax1.set_ylabel('Expected Return')
ax1.set_xlabel('Volatility')
ax2.grid(True)
ax2.set_xlim(0, right)
ax2.set_ylim(0, top)
ax2.legend()
ax2.set_title(f'ε = {ax2_epsilon}')
ax2.set_ylabel('Expected Return')
ax2.set_xlabel('Volatility')

# Get timestamp
date_obj = datetime.now()
date = 'Y{:04}M{:02}D{:02}h{:02}m{:02}s{:02}'.format(
    date_obj.year, date_obj.month, date_obj.day, date_obj.hour, date_obj.minute, date_obj.second)

folder_name = 'epsilon_indicator'

# Check if folder exists and creates if not
if not os.path.exists('images/' + folder_name):
    os.makedirs('images/' + folder_name)

fig.text(0.5, 0.005, 'How to interpret: Blue markers are part of the efficient frontier. The epsilon indicator is the minimum factor by which the red set has to be multiplied in the objective so as to weakly dominate the blue set.\nHence, the closer to 1 is the epsilon indicator, the better the red set.',
         ha='center', size='xx-small')

output_name = f'N{N}B{B}q{q}P{P}W{work_id}{date}'
fig.suptitle('Epsilon Indicator - ' + output_name)

# Save as 2160p image
plt.savefig(
    f'images/{folder_name}/{output_name}.png', dpi=360)
plt.show()
