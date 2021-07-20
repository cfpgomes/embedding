import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['CMU Serif']
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


scenario_name = 'scenario1'
N1 = None
N2 = None
q = 1
mu1 = None
mu2 = None
sigma1 = None
sigma2 = None

data1_filename = 'data/out_industry_diversified_N64_p1mo_i1d.json'
data2_filename = 'data/out_correlated_N64_p1mo_i1d.json'

with open(data1_filename) as jsonfile:
    data = json.load(jsonfile)
    N1 = data['N']               # Universe size
    mu1 = pd.Series(data['mu']).to_numpy()
    sigma1 = pd.DataFrame.from_dict(data['sigma'], orient='index').to_numpy()

with open(data2_filename) as jsonfile:
    data = json.load(jsonfile)
    N2 = data['N']               # Universe size
    mu2 = pd.Series(data['mu']).to_numpy()
    sigma2 = pd.DataFrame.from_dict(data['sigma'], orient='index').to_numpy()


min_sigma1 = 0
max_sigma1 = 0
for i in range(N1):
    for j in range(i+1, N1):
        if sigma1[i][j] < 0:
            min_sigma1 += sigma1[i][j]
        else:
            max_sigma1 += sigma1[i][j]

max_mu1 = 0
for i in range(N1):
    if mu1[i] > 0:
        max_mu1 += mu1[i]

P1 = -q * min_sigma1 + max_mu1

min_sigma2 = 0
max_sigma2 = 0
for i in range(N2):
    for j in range(i+1, N2):
        if sigma2[i][j] < 0:
            min_sigma2 += sigma2[i][j]
        else:
            max_sigma2 += sigma2[i][j]

max_mu2 = 0
for i in range(N2):
    if mu2[i] > 0:
        max_mu2 += mu2[i]

P2 = -q * min_sigma2 + max_mu2

B1 = int(N1*0.5)
print(f'B1:{B1}')
classical_solutions1_foldername = 'results/scenarioA1_N64_classical'
classical_solutions1 = []

B2 = int(N2*0.5)
print(f'B2:{B2}')
classical_solutions2_foldername = 'results/N64_B0.5_correlated_classical'
classical_solutions2 = []

for filename in os.listdir(classical_solutions1_foldername):
    if '.json' in filename:
        with open(classical_solutions1_foldername+'/'+filename) as jsonfile:
            data = json.load(jsonfile)
            classical_solutions1.append({'sol': data['solution'], 'objective': get_objective_value(data['solution'], N1, B1, mu1, sigma1, P1), 'expected_return': get_expected_return(
                data['solution'], N1, B1, mu1), 'volatility': get_volatility(data['solution'], N1, B1, sigma1), 'equals_budget': equals_budget(data['solution'], N1, B1)})

for filename in os.listdir(classical_solutions2_foldername):
    if '.json' in filename:
        with open(classical_solutions2_foldername+'/'+filename) as jsonfile:
            data = json.load(jsonfile)
            classical_solutions2.append({'sol': data['solution'], 'objective': get_objective_value(data['solution'], N2, B2, mu2, sigma2, P2), 'expected_return': get_expected_return(
                data['solution'], N2, B2, mu2), 'volatility': get_volatility(data['solution'], N2, B2, sigma2), 'equals_budget': equals_budget(data['solution'], N2, B2)})

WS_filename = 'results/WV_N64_B0.5_industry_diversified/IPL_linearized_WV_N64q1.00B32.json'
with open(WS_filename) as jsonfile:
    data = json.load(jsonfile)
    WS_solution = {'sol': data['solution'], 'objective': get_objective_value(data['solution'], N1, B1, mu1, sigma1, P1), 'expected_return': get_expected_return(
        data['solution'], N1, B1, mu1), 'volatility': get_volatility(data['solution'], N1, B1, sigma1), 'equals_budget': equals_budget(data['solution'], N1, B1)}

print('max_sigma1:')
print(max_sigma1)
print('WS:')
print(WS_solution['volatility'])
max_sigma1 = WS_solution['volatility']
print('max_sigma1:')
print(max_sigma1)

set1_foldername = 'results/scenarioA2B3_N64_Pformulated_Cformulated1.000_Allocated_B0.5_mediumDmediumS_annealer_try6'
# set2_foldername = 'results/scenarioA3_N64_Pformulated_Cformulated1.000_Allocated_layout_correlated_annealer_try5'

set1_samples = []
# set2_samples = []

for filename in os.listdir(set1_foldername):
    with open(set1_foldername+'/'+filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader, None)  # Skip header
        for row in reader:
            sol = np.array(list(map(float, row[:-3])))
            for _ in range(int(row[-1])):
                set1_samples.append({'sol': sol, 'objective': get_objective_value(sol, N1, B1, mu1, sigma1, P1), 'expected_return': get_expected_return(
                    sol, N1, B1, mu1), 'volatility': get_volatility(sol, N1, B1, sigma1), 'equals_budget': equals_budget(sol, N1, B1)})

# for filename in os.listdir(set2_foldername):
#     with open(set2_foldername+'/'+filename) as csvfile:
#         reader = csv.reader(csvfile, delimiter=',', quotechar='"')
#         next(reader, None)  # Skip header
#         for row in reader:
#             sol = np.array(list(map(float, row[:-3])))
#             for _ in range(int(row[-1])):
#                 set2_samples.append({'sol': sol, 'objective': get_objective_value(sol, N2, B2, mu2, sigma2, P2), 'expected_return': get_expected_return(
#                     sol, N2, B2, mu2), 'volatility': get_volatility(sol, N2, B2, sigma2), 'equals_budget': equals_budget(sol, N2, B2)})


print(len(set1_samples))
# print(len(set2_samples))

# 2 columns, 9 per 6 inches figure
fig, ax1 = plt.subplots(figsize=(5, 4))

# Exclude non complying with budget
set1_dominating_samples = list(
    filter(lambda x: x['equals_budget'], set1_samples))
# set2_dominating_samples = list(
#     filter(lambda x: x['equals_budget'], set2_samples))

# Exclude below zero return
set1_dominating_samples = list(
    filter(lambda x: x['expected_return'] > 0, set1_dominating_samples))
# set2_dominating_samples = list(
#     filter(lambda x: x['expected_return'] > 0, set2_dominating_samples))

print(len(set1_dominating_samples))
# print(len(set2_dominating_samples))

# Exclude dominated
set1_dominating_samples = list(filter(lambda x: not any(
    (x['expected_return'] < y['expected_return'] and x['volatility'] > y['volatility']) for y in set1_dominating_samples), set1_dominating_samples))
# set2_dominating_samples = list(filter(lambda x: not any(
#     (x['expected_return'] < y['expected_return'] and x['volatility'] > y['volatility']) for y in set2_dominating_samples), set2_dominating_samples))

print(len(set1_dominating_samples))
# print(len(set2_dominating_samples))

set1_valid_samples = list(filter(lambda x: x['equals_budget'], set1_samples))
# set2_valid_samples = list(filter(lambda x: x['equals_budget'], set2_samples))

ax1.scatter(list(map(lambda x: x['volatility'], set1_valid_samples)), list(
    map(lambda x: x['expected_return'], set1_valid_samples)), color='silver', label='feasible solution', s=4)
# ax2.scatter(list(map(lambda x: x['volatility'], set2_valid_samples)), list(
#     map(lambda x: x['expected_return'], set2_valid_samples)), color='silver', label='annealer', s=4)

ax1.scatter(list(map(lambda x: x['volatility'], set1_dominating_samples)), list(
    map(lambda x: x['expected_return'], set1_dominating_samples)), color='red', label='approximation frontier')
ax1.scatter(list(map(lambda x: x['volatility'], classical_solutions1)), list(
    map(lambda x: x['expected_return'], classical_solutions1)), color='blue', label='representation', s=4)

# ax2.scatter(list(map(lambda x: x['volatility'], set2_dominating_samples)), list(
#     map(lambda x: x['expected_return'], set2_dominating_samples)), color='red', label='annealer best')
# ax2.scatter(list(map(lambda x: x['volatility'], classical_solutions2)), list(
#     map(lambda x: x['expected_return'], classical_solutions2)), color='blue', label='classical', s=4)


ax1_epsilon = 0
for b in classical_solutions1:
    tmp = float('inf')
    for a in set1_dominating_samples:
        obj_ret_div = b['expected_return'] / a['expected_return']
        obj_vol_div = (max_sigma1 - b['volatility']) / \
            (max_sigma1 - a['volatility'])
        tmp = min(tmp, max(obj_ret_div, obj_vol_div))
    ax1_epsilon = max(ax1_epsilon, tmp)

# ax2_epsilon = 0
# for b in classical_solutions2:
#     tmp = float('inf')
#     for a in set2_dominating_samples:
#         obj_ret_div = b['expected_return'] / a['expected_return']
#         obj_vol_div = (max_sigma2 - b['volatility']) / \
#             (max_sigma2 - a['volatility'])
#         tmp = min(tmp, max(obj_ret_div, obj_vol_div))
#     ax2_epsilon = max(ax2_epsilon, tmp)

# Tidy up the figure
(ax1_left, ax1_right) = ax1.get_xlim()
# (ax2_left, ax2_right) = ax2.get_xlim()
(ax1_bottom, ax1_top) = ax1.get_ylim()
# (ax2_bottom, ax2_top) = ax2.get_ylim()

# right = max(ax1_right, ax2_right)
# left = min(ax1_left, ax2_left)
# top = max(ax1_top, ax2_top)
# bottom = min(ax1_bottom, ax2_bottom)

# left = min(0, left)
# bottom = min(0, bottom)

ax1.grid(True)
ax1.set_xlim(0, ax1_right)
ax1.set_ylim(0, ax1_top)
ax1.legend()
ax1.set_title(f'{set1_foldername}\nε = {ax1_epsilon}', size='xx-small')
ax1.set_ylabel('Expected Return')
ax1.set_xlabel('Volatility')
# ax2.grid(True)
# ax2.set_xlim(left, right)
# ax2.set_ylim(bottom, top)
# ax2.legend()
# ax2.set_title(f'{set2_foldername}\nε = {ax2_epsilon}', size='xx-small')
# ax2.set_ylabel('Expected Return')
# ax2.set_xlabel('Volatility')

print(f'{ax1_epsilon:0.3f}\n')
# print(f'{ax2_epsilon:0.3f}\n')

# Get timestamp
date_obj = datetime.now()
date = 'Y{:04}M{:02}D{:02}h{:02}m{:02}s{:02}'.format(
    date_obj.year, date_obj.month, date_obj.day, date_obj.hour, date_obj.minute, date_obj.second)

folder_name = 'epsilon_indicator'

# Check if folder exists and creates if not
if not os.path.exists('images/' + folder_name):
    os.makedirs('images/' + folder_name)

# fig.text(0.5, 0.005, 'How to interpret: Blue markers are part of the efficient frontier. The epsilon indicator is the minimum factor by which the red set has to be multiplied in the objective so as to weakly dominate the blue set.\nHence, the closer to 1 is the epsilon indicator, the better the red set.',
#          ha='center', size='xx-small')

output_name = f'{scenario_name}{date}'
# fig.suptitle('Epsilon Indicator - ' + output_name)

# Save as 2 1 6 0p image
plt.savefig(
    f'images/{folder_name}/{output_name}.pdf', dpi=360)
plt.show()
