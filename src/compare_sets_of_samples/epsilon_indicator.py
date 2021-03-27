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
mu = None
sigma = None

data_filename = 'data/out_N50_p1mo_i1d.json'
with open(data_filename) as jsonfile:
    data = json.load(jsonfile)
    N = data['N']               # Universe size
    mu = pd.Series(data['mu']).to_numpy()
    sigma = pd.DataFrame.from_dict(data['sigma'], orient='index').to_numpy()


min_sigma = 0
for i in range(N):
    for j in range(i+1, N):
        if sigma[i][j] < 0:
            min_sigma += sigma[i][j]

max_mu = 0
for i in range(N):
    if mu[i] > 0:
        max_mu += mu[i]

P = -q * min_sigma + max_mu

B1 = int(N*0.5)
classical_solutions1_foldername = 'results/scenario2_B0.5_classical'
classical_solutions1 = []

B2 = int(N*0.5)
classical_solutions2_foldername = 'results/scenario2_B0.5_classical'
classical_solutions2 = []

for filename in os.listdir(classical_solutions1_foldername):
    if '.json' in filename:
        with open(classical_solutions1_foldername+'/'+filename) as jsonfile:
            data = json.load(jsonfile)
            classical_solutions1.append({'sol': data['solution'], 'objective': get_objective_value(data['solution'], N, B1, mu, sigma), 'expected_return': get_expected_return(
                data['solution'], N, B1, mu), 'volatility': get_volatility(data['solution'], N, B1, sigma), 'equals_budget': equals_budget(data['solution'], N, B1)})

for filename in os.listdir(classical_solutions2_foldername):
    if '.json' in filename:
        with open(classical_solutions2_foldername+'/'+filename) as jsonfile:
            data = json.load(jsonfile)
            classical_solutions2.append({'sol': data['solution'], 'objective': get_objective_value(data['solution'], N, B2, mu, sigma), 'expected_return': get_expected_return(
                data['solution'], N, B2, mu), 'volatility': get_volatility(data['solution'], N, B2, sigma), 'equals_budget': equals_budget(data['solution'], N, B2)})

set1_foldername = 'results/scenario2_B0.5_normal_fixed_chain_strength_fixed_P_10000_shots'
set2_foldername = 'results/scenario2_B0.5_clique_fixed_chain_strength_fixed_P_10000_shots'

set1_samples = []
set2_samples = []

for filename in os.listdir(set1_foldername):
    with open(set1_foldername+'/'+filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader, None)  # Skip header
        for row in reader:
            sol = np.array(list(map(float, row[:-3])))
            for _ in range(int(row[-1])):
                set1_samples.append({'sol': sol, 'objective': get_objective_value(sol, N, B1, mu, sigma), 'expected_return': get_expected_return(
                    sol, N, B1, mu), 'volatility': get_volatility(sol, N, B1, sigma), 'equals_budget': equals_budget(sol, N, B1)})

for filename in os.listdir(set2_foldername):
    with open(set2_foldername+'/'+filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader, None)  # Skip header
        for row in reader:
            sol = np.array(list(map(float, row[:-3])))
            for _ in range(int(row[-1])):
                set2_samples.append({'sol': sol, 'objective': get_objective_value(sol, N, B2, mu, sigma), 'expected_return': get_expected_return(
                    sol, N, B2, mu), 'volatility': get_volatility(sol, N, B2, sigma), 'equals_budget': equals_budget(sol, N, B2)})

# 2 columns, 9 per 6 inches figure
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(9, 6))

set1_dominating_samples = list(
    filter(lambda x: x['equals_budget'], set1_samples))
set2_dominating_samples = list(
    filter(lambda x: x['equals_budget'], set2_samples))

print(len(set1_dominating_samples))
print(len(set2_dominating_samples))

set1_dominating_samples = list(filter(lambda x: not any(
    (x['expected_return'] < y['expected_return'] and x['volatility'] > y['volatility']) for y in set1_dominating_samples), set1_dominating_samples))
set2_dominating_samples = list(filter(lambda x: not any(
    (x['expected_return'] < y['expected_return'] and x['volatility'] > y['volatility']) for y in set2_dominating_samples), set2_dominating_samples))

print(len(set1_dominating_samples))
print(len(set2_dominating_samples))

ax1.scatter(list(map(lambda x: x['volatility'], set1_dominating_samples)), list(
    map(lambda x: x['expected_return'], set1_dominating_samples)), color='red', label='normal')
ax1.scatter(list(map(lambda x: x['volatility'], classical_solutions1)), list(
    map(lambda x: x['expected_return'], classical_solutions1)), color='blue', label='classical')

ax2.scatter(list(map(lambda x: x['volatility'], set2_dominating_samples)), list(
    map(lambda x: x['expected_return'], set2_dominating_samples)), color='red', label='clique')
ax2.scatter(list(map(lambda x: x['volatility'], classical_solutions2)), list(
    map(lambda x: x['expected_return'], classical_solutions2)), color='blue', label='classical')


ax1_epsilon = 0
for solution in set1_dominating_samples:
    tmp = float('inf')
    for sample in classical_solutions1:
        obj_ret_div = sample['expected_return'] / solution['expected_return']
        obj_vol_div = sample['volatility'] / solution['volatility']
        tmp = min(tmp, max(obj_ret_div, obj_vol_div))
    ax1_epsilon = max(ax1_epsilon, tmp)

ax2_epsilon = 0
for solution in set2_dominating_samples:
    tmp = float('inf')
    for sample in classical_solutions2:
        obj_ret_div = sample['expected_return'] / solution['expected_return']
        obj_vol_div = sample['volatility'] / solution['volatility']
        tmp = min(tmp, max(obj_ret_div, obj_vol_div))
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
ax1.set_title(f'{set1_foldername}\nε = {ax1_epsilon}', size='xx-small')
ax1.set_ylabel('Expected Return')
ax1.set_xlabel('Volatility')
ax2.grid(True)
ax2.set_xlim(0, right)
ax2.set_ylim(0, top)
ax2.legend()
ax2.set_title(f'{set2_foldername}\nε = {ax2_epsilon}', size='xx-small')
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

output_name = f'N{N}q{q}P{P}W{work_id}{date}'
fig.suptitle('Epsilon Indicator - ' + output_name)

# Save as 2160p image
plt.savefig(
    f'images/{folder_name}/{output_name}.png', dpi=360)
plt.show()
