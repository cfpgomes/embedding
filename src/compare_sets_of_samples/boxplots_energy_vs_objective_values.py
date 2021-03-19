import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from datetime import datetime
import os
import json
import csv

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

classical_solution_min_filename = 'results/IPL_linearized_N20q1.00B10P100_solution.json'
classical_solution_max_filename = 'results/IPL_linearized_max_N20q1.00B10P100_solution.json'

min_solution = None
max_solution = None

with open(classical_solution_min_filename) as jsonfile:
    data = json.load(jsonfile)
    min_solution = data['solution']

with open(classical_solution_max_filename) as jsonfile:
    data = json.load(jsonfile)
    max_solution = data['solution']

set1_filename = "results/outnormalN20q1.00B10P100chain512.csv"
set2_filename = "results/outcliqueN20q1.00B10P100chain512.csv"

set1_samples_energy = []
set2_samples_energy = []

set1_samples_value = []
set2_samples_value = []

with open(set1_filename) as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader, None)  # Skip header
    for row in reader:
        # To append energy num_occur times.
        set1_samples_energy.extend([float(row[-2])
                                   for i in range(int(row[-1]))])

        sol = np.array(list(map(float, row[:-3])))
        sol_value = q*np.transpose(sol).dot(sigma).dot(sol) - np.transpose(
            mu).dot(sol) + P * np.square(np.ones((1, N)).dot(sol) - B)

        set1_samples_value.extend([sol_value[0] for i in range(int(row[-1]))])

with open(set2_filename) as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader, None)  # Skip header
    for row in reader:
        # To append energy num_occur times.
        set2_samples_energy.extend([float(row[-2])
                                   for i in range(int(row[-1]))])

        sol = np.array(list(map(float, row[:-3])))
        sol_value = q*np.transpose(sol).dot(sigma).dot(sol) - np.transpose(
            mu).dot(sol) + P * np.square(np.ones((1, N)).dot(sol) - B)

        set2_samples_value.extend([sol_value[0] for i in range(int(row[-1]))])

# 2 columns, 9 per 6 inches figure
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(9, 6))

ax1_boxplots_dic = ax1.boxplot([set1_samples_energy, set2_samples_energy], labels=['normal', 'clique'])

ax2_boxplots_dic = ax2.boxplot([set1_samples_value, set2_samples_value], labels=['normal', 'clique'])

# Draw medians
for line in ax1_boxplots_dic['medians']:
    # get position data for median line
    x, y = line.get_xydata()[1]  # top of median line
    num = line.get_data()[1][1]
    # overlay median value
    # draw on right side
    ax1.text(x, y, f'{num:.2f}', horizontalalignment='left')

for line in ax2_boxplots_dic['medians']:
    # get position data for median line
    x, y = line.get_xydata()[1]  # top of median line
    num = line.get_data()[1][1]
    # overlay median value
    # draw on right side
    ax2.text(x, y, f'{num:.3f}', horizontalalignment='left')

# Draw outliers
for line in ax1_boxplots_dic['fliers']:
    # get position data
    x, y = line.get_xydata()[0] 
    # overlay number of outliers
    num = len(line.get_xydata())
    # draw on right side
    ax1.text(x+0.15, y, f'{num}\noutliers', horizontalalignment='left')

for line in ax2_boxplots_dic['fliers']:
    # get position data
    x, y = line.get_xydata()[0]
    # overlay number of outliers
    num = len(line.get_xydata())
    # draw on right side
    ax2.text(x+0.15, y, f'{num}\noutliers', horizontalalignment='left')

# Draw best classical value:
min_solution_value = q*np.transpose(min_solution).dot(sigma).dot(min_solution) - np.transpose(
            mu).dot(min_solution) + P * np.square(np.ones((1, N)).dot(min_solution) - B)
print(min_solution_value[0])
ax2.axhline(y=min_solution_value[0], color='red', linestyle='-', label='classical best')

# Draw worst classical value:
max_solution_value = q*np.transpose(max_solution).dot(sigma).dot(max_solution) - np.transpose(
            mu).dot(max_solution) + P * np.square(np.ones((1, N)).dot(max_solution) - B)
print(max_solution_value[0])
ax2.axhline(y=max_solution_value[0], color='darkred', linestyle='-', label='classical worst')

    
# Tidy up the figure
ax1.grid(True)
ax1.set_ylabel('Solution Energies')
ax1.set_xlabel('Embedding')
ax2.grid(True)
ax2.legend()
ax2.set_ylabel('Solution Objective Value')
ax2.set_xlabel('Embedding')

# Get timestamp
date_obj = datetime.now()
date = 'Y{:04}M{:02}D{:02}h{:02}m{:02}s{:02}'.format(
    date_obj.year, date_obj.month, date_obj.day, date_obj.hour, date_obj.minute, date_obj.second)

folder_name = "boxplots_energy_vs_objective_values"

# Check if folder exists and creates if not
if not os.path.exists('images/' + folder_name):
    os.makedirs('images/' + folder_name)

fig.text(0.5,0.005,'How to interpret: The lower the `y` value, the better. Therefore, lower boxplots suggest better performance.\nMoreover, outliers over the boxplots are undesired. Finally, the lower the mean line, the better.', ha='center', size='xx-small')

output_name = f'N{N}B{B}q{q}P{P}W{work_id}{date}'
fig.suptitle('Boxplots - ' + output_name)

# Save as 2160p image
plt.savefig(
    f'images/{folder_name}/{output_name}.png', dpi=360)
plt.show()
