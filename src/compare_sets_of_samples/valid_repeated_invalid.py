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

# 9 per 6 inches figure
plt.rcParams.update({'figure.autolayout': True})
fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(
    9, 6), gridspec_kw={'height_ratios': [4, 5]})

set1_dominating_samples = list(
    filter(lambda x: x['equals_budget'], set1_samples))
set2_dominating_samples = list(
    filter(lambda x: x['equals_budget'], set2_samples))

set1_dominating_samples = list(filter(lambda x: not any(
    (x['expected_return'] < y['expected_return'] and x['volatility'] > y['volatility']) for y in set1_dominating_samples), set1_dominating_samples))
set2_dominating_samples = list(filter(lambda x: not any(
    (x['expected_return'] < y['expected_return'] and x['volatility'] > y['volatility']) for y in set2_dominating_samples), set2_dominating_samples))

# Valid
# Invalid
# Repeated
# Repeated valids
# Expected Return
# Volatility

set1_valid_samples = list(filter(lambda x: x['equals_budget'], set1_samples))
set2_valid_samples = list(filter(lambda x: x['equals_budget'], set2_samples))
set1_unique_samples = np.unique(
    list(map(lambda x: x['sol'], set1_samples)), axis=0)
set2_unique_samples = np.unique(
    list(map(lambda x: x['sol'], set2_samples)), axis=0)
set1_unique_valid_samples = list(
    filter(lambda x: equals_budget(x, N, B), set1_unique_samples))
set2_unique_valid_samples = list(
    filter(lambda x: equals_budget(x, N, B), set2_unique_samples))

set1_num_valid = len(set1_valid_samples) / len(set1_samples)
set2_num_valid = len(set2_valid_samples) / len(set2_samples)
set1_num_invalid = (len(set1_samples) -
                    len(set1_valid_samples)) / len(set1_samples)
set2_num_invalid = (len(set2_samples) -
                    len(set2_valid_samples)) / len(set2_samples)
set1_num_repeated = (len(set1_samples) -
                     len(set1_unique_samples)) / len(set1_samples)
set2_num_repeated = (len(set2_samples) -
                     len(set2_unique_samples)) / len(set2_samples)

set1_average_expected_return = sum(list(map(lambda x: x['expected_return'], set1_samples)))/len(
    list(map(lambda x: x['expected_return'], set1_samples)))
set2_average_expected_return = sum(list(map(lambda x: x['expected_return'], set2_samples)))/len(
    list(map(lambda x: x['expected_return'], set2_samples)))

set1_average_volatility = sum(list(map(lambda x: x['volatility'], set1_samples)))/len(
    list(map(lambda x: x['volatility'], set1_samples)))
set2_average_volatility = sum(list(map(lambda x: x['volatility'], set2_samples)))/len(
    list(map(lambda x: x['volatility'], set2_samples)))


set1_num_repeated_valid = (len(set1_valid_samples) -
                           len(set1_unique_valid_samples)) / len(set1_samples)
set2_num_repeated_valid = (len(set2_valid_samples) -
                           len(set2_unique_valid_samples)) / len(set2_samples)
set1_average_expected_return_valid = sum(list(map(lambda x: x['expected_return'], set1_valid_samples)))/len(
    list(map(lambda x: x['expected_return'], set1_valid_samples)))
set2_average_expected_return_valid = sum(list(map(lambda x: x['expected_return'], set2_valid_samples)))/len(
    list(map(lambda x: x['expected_return'], set2_valid_samples)))
set1_average_volatility_valid = sum(list(map(lambda x: x['volatility'], set1_valid_samples)))/len(
    list(map(lambda x: x['volatility'], set1_valid_samples)))
set2_average_volatility_valid = sum(list(map(lambda x: x['volatility'], set2_valid_samples)))/len(
    list(map(lambda x: x['volatility'], set2_valid_samples)))


set1_epsilon = 0
for solution in classical_solutions:
    tmp = float('inf')
    for sample in set1_dominating_samples:
        tmp = min(tmp, max(sample['expected_return'] / solution['expected_return'],
                           sample['volatility']/solution['volatility']))
    set1_epsilon = max(set1_epsilon, tmp)

set2_epsilon = 0
for solution in classical_solutions:
    tmp = float('inf')
    for sample in set2_dominating_samples:
        tmp = min(tmp, max(sample['expected_return'] / solution['expected_return'],
                           sample['volatility']/solution['volatility']))
    set2_epsilon = max(set2_epsilon, tmp)

bar1_names = ['Valid', 'Invalid', 'Repeated','Repeated Valids']

bar2_names = ['Average Expected Return', 'Average Volatility', 'Average Expected Return of Valid', 'Average Volatility of Valids', 'Epsilon Indicator']

ax1.barh(bar1_names, [set1_num_valid, set1_num_invalid, set1_num_repeated, set1_num_repeated_valid], align='edge', height=0.4, label='normal', color='red')
for i, v in enumerate([set1_num_valid, set1_num_invalid, set1_num_repeated, set1_num_repeated_valid]):
    ax1.text(v, i+0.2, f'{v:.3f}', va='center')

ax1.barh(bar1_names, [set2_num_valid, set2_num_invalid, set2_num_repeated, set2_num_repeated_valid], align='edge', height=-0.4, label='clique', color='blue')
for i, v in enumerate([set2_num_valid, set2_num_invalid, set2_num_repeated, set2_num_repeated_valid]):
    ax1.text(v, i-0.2, f'{v:.3f}', va='center')

ax2.barh(bar2_names, [set1_average_expected_return, set1_average_volatility, set1_average_expected_return_valid, set1_average_volatility_valid, set1_epsilon], align='edge', height=0.4, label='normal', color='red')
for i, v in enumerate([set1_average_expected_return, set1_average_volatility, set1_average_expected_return_valid, set1_average_volatility_valid, set1_epsilon]):
    ax2.text(v, i+0.2, f'{v:.3f}', va='center')

ax2.barh(bar2_names, [set2_average_expected_return, set2_average_volatility, set2_average_expected_return_valid, set2_average_volatility_valid, set2_epsilon], align='edge', height=-0.4, label='clique', color='blue')
for i, v in enumerate([set2_average_expected_return, set2_average_volatility, set2_average_expected_return_valid, set2_average_volatility_valid, set2_epsilon]):
    ax2.text(v, i-0.2, f'{v:.3f}', va='center')

# Tidy up the figure
ax1.grid(True)
ax1.legend()
ax1.set_xlim(0,1)
ax1.set_xlabel('Proportion')
ax2.grid(True)
ax2.legend()
ax2.set_xlabel('Value')

# Get timestamp
date_obj = datetime.now()
date = 'Y{:04}M{:02}D{:02}h{:02}m{:02}s{:02}'.format(
    date_obj.year, date_obj.month, date_obj.day, date_obj.hour, date_obj.minute, date_obj.second)

folder_name = 'valid_repeated_invalid'

# Check if folder exists and creates if not
if not os.path.exists('images/' + folder_name):
    os.makedirs('images/' + folder_name)

output_name = f'N{N}B{B}q{q}P{P}W{work_id}{date}'
fig.suptitle('Valid Repeated Invalid - ' + output_name)

# Save as 2160p image
plt.savefig(
    f'images/{folder_name}/{output_name}.png', dpi=360)
plt.show()
