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


def get_objective_value(sol, N, B, mu, sigma, P):
    return np.transpose(sol).dot(sigma).dot(sol) - np.transpose(mu).dot(sol) + P * np.square(np.ones((1, N)).dot(sol) - B)


def get_volatility(sol, N, B, sigma):
    return np.transpose(sol).dot(sigma).dot(sol)


scenario_name = 'S1'
N = None
q = 1
mu = None
sigma = None

data_filename = 'data/out_industry_diversified_N16_P1mo_i1d.json'
with open(data_filename) as jsonfile:
    data = json.load(jsonfile)
    N = data['N']               # Universe size
    mu = pd.Series(data['mu']).to_numpy()
    sigma = pd.DataFrame.from_dict(data['sigma'], orient='index').to_numpy()

min_sigma = 0
max_sigma = 0
for i in range(N):
    for j in range(i+1, N):
        if sigma[i][j] < 0:
            min_sigma += sigma[i][j]
        else:
            max_sigma += sigma[i][j]

max_mu = 0
for i in range(N):
    if mu[i] > 0:
        max_mu += mu[i]

P = -q * min_sigma + max_mu

B = int(N*0.5)
print(f'B:{B}')

# classical_solutions_foldername = 'results/N16_B0.5_industry_diversified_classical'
classical_solutions_foldername = 'results/scenarioA1_N16_classical'
classical_solutions = []

for filename in os.listdir(classical_solutions_foldername):
    if '.json' in filename:
        with open(classical_solutions_foldername+'/'+filename) as jsonfile:
            data = json.load(jsonfile)
            classical_solutions.append({'sol': data['solution'], 'objective': get_objective_value(data['solution'], N, B, mu, sigma, P), 'expected_return': get_expected_return(
                data['solution'], N, B, mu), 'volatility': get_volatility(data['solution'], N, B, sigma), 'equals_budget': equals_budget(data['solution'], N, B)})


WS_filename = 'results/WV_N16_B0.5_industry_diversified/IPL_linearized_WV_N16q1.00B8.json'
with open(WS_filename) as jsonfile:
    data = json.load(jsonfile)
    WS_solution = {'sol': data['solution'], 'objective': get_objective_value(data['solution'], N, B, mu, sigma, P), 'expected_return': get_expected_return(
        data['solution'], N, B, mu), 'volatility': get_volatility(data['solution'], N, B, sigma), 'equals_budget': equals_budget(data['solution'], N, B)}

print('WS:')
print(WS_solution['volatility'])

print('max_sigma:')
print(max_sigma)
max_sigma = WS_solution['volatility']
print('max_sigma:')
print(max_sigma)

list_set_epsilons = []

list_set_foldernames = [
    [
    'results/S2b_16_0.125_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try1',
    'results/S2c_16_0.25_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try1',
    'results/S2d_16_0.375_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try1',
    'results/S2e_16_0.5_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try1',
    'results/S2f_16_0.625_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try1',
    'results/S2g_16_0.75_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try1',
    'results/S2h_16_0.875_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try1',
    'results/S2i_16_1.0_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try1',
    'results/S2j_16_1.125_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try1',
    'results/S2k_16_1.25_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try1',
    'results/S2l_16_1.375_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try1',
    'results/S2m_16_1.5_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try1'],
    [
    'results/S2b_16_0.125_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try2',
    'results/S2c_16_0.25_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try2',
    'results/S2d_16_0.375_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try2',
    'results/S2e_16_0.5_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try2',
    'results/S2f_16_0.625_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try2',
    'results/S2g_16_0.75_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try2',
    'results/S2h_16_0.875_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try2',
    'results/S2i_16_1.0_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try2',
    'results/S2j_16_1.125_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try2',
    'results/S2k_16_1.25_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try2',
    'results/S2l_16_1.375_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try2',
    'results/S2m_16_1.5_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try2'],
    [
    'results/S2b_16_0.125_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try3',
    'results/S2c_16_0.25_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try3',
    'results/S2d_16_0.375_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try3',
    'results/S2e_16_0.5_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try3',
    'results/S2f_16_0.625_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try3',
    'results/S2g_16_0.75_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try3',
    'results/S2h_16_0.875_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try3',
    'results/S2i_16_1.0_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try3',
    'results/S2j_16_1.125_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try3',
    'results/S2k_16_1.25_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try3',
    'results/S2l_16_1.375_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try3',
    'results/S2m_16_1.5_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try3'],
    [
    'results/S2a_16_default_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try1',
    'results/S2a_16_default_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try2',
    'results/S1b_16_default_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try1',
    'results/S1b_16_default_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try2',
    'results/S1b_16_default_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try3',
    'results/S1b_16_default_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try4',
    'results/S1b_16_default_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try5',
    'results/S1b_16_default_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try6',
    'results/S1b_16_default_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try7',
    'results/S1b_16_default_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try8',
    'results/S1b_16_default_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try9',
    'results/S1b_16_default_1000per_minimal_0.5_normal_standard_industry_diversified_pegasus_try10']
]

labels = ['try1', 'try2', 'try3', 'default']

for set_foldernames in list_set_foldernames:

    set_list_samples = []

    for set_foldername in set_foldernames:
        set_samples = []
        for filename in os.listdir(set_foldername):
            with open(set_foldername+'/'+filename) as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                next(reader, None)  # Skip header
                for row in reader:
                    sol = np.array(list(map(float, row[:-3])))
                    for _ in range(int(row[-1])):
                        set_samples.append({'sol': sol, 'objective': get_objective_value(sol, N, B, mu, sigma, P), 'expected_return': get_expected_return(
                            sol, N, B, mu), 'volatility': get_volatility(sol, N, B, sigma), 'equals_budget': equals_budget(sol, N, B)})
        set_list_samples.append(set_samples)

    set_list_dominating_samples = []

    # Exclude non complying with budget
    for set_samples in set_list_samples:
        set_list_dominating_samples.append(list(
            filter(lambda x: x['equals_budget'], set_samples)))

    print(len(set_list_dominating_samples[0]))
    print(len(set_list_dominating_samples[1]))

    # Exclude below zero return
    for i in range(len(set_list_dominating_samples)):
        set_list_dominating_samples[i] = list(
            filter(lambda x: x['expected_return'] > 0, set_list_dominating_samples[i]))

    print(len(set_list_dominating_samples[0]))
    print(len(set_list_dominating_samples[1]))

    # Exclude dominated
    for i in range(len(set_list_dominating_samples)):
        set_list_dominating_samples[i] = list(filter(lambda x: not any(
            (x['expected_return'] < y['expected_return'] and x['volatility'] > y['volatility']) for y in set_list_dominating_samples[i]), set_list_dominating_samples[i]))

    print(len(set_list_dominating_samples[0]))
    print(len(set_list_dominating_samples[1]))

    set_list_epsilon = []

    for i in range(len(set_list_dominating_samples)):
        epsilon = 0
        for b in classical_solutions:
            tmp = float('inf')
            for a in set_list_dominating_samples[i]:
                obj_ret_div = b['expected_return'] / a['expected_return']
                obj_vol_div = (max_sigma - b['volatility']) / \
                    (max_sigma - a['volatility'])
                tmp = min(tmp, max(obj_ret_div, obj_vol_div))
            epsilon = max(epsilon, tmp)
        set_list_epsilon.append(epsilon)

    for epsilon in set_list_epsilon:
        print(epsilon)
    list_set_epsilons.append(set_list_epsilon)

print(f'final:\n{list_set_epsilons}')

# 2 columns, 9 per 6 inches figure
fig, ax1 = plt.subplots(figsize=(9, 6))
ax1.boxplot(list_set_epsilons, notch=True, labels=labels)

# Tidy up the figure
(ax1_bottom, ax1_top) = ax1.get_ylim()

ax1.grid(True)
ax1.set_title('N16')
ax1.set_ylim(1, ax1_top)
ax1.set_ylabel('Epsilon Indicator')
ax1.set_xlabel('Mode')


# Get timestamp
date_obj = datetime.now()
date = 'Y{:04}M{:02}D{:02}h{:02}m{:02}s{:02}'.format(
    date_obj.year, date_obj.month, date_obj.day, date_obj.hour, date_obj.minute, date_obj.second)

folder_name = 'boxplots_simple'

# Check if folder exists and creates if not
if not os.path.exists('images/' + folder_name):
    os.makedirs('images/' + folder_name)

fig.text(0.6, 0.005, 'How to interpret: The epsilon indicator is the minimum factor by which the annealer set has to be multiplied in the objective so as to weakly dominate the classical set.\nHence, the closer to 1 is the epsilon indicator, the better the annealer set.',
         ha='center', size='xx-small')

output_name = f'{scenario_name}{date}'
fig.suptitle('Boxplots - ' + output_name)

# Save as 2 1 6 0p image
plt.savefig(
    f'images/{folder_name}/{output_name}.png', dpi=360)
plt.show()
