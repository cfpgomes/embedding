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
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(9, 6))

vmin_energy = min(min(set1_samples_energy), min(set2_samples_energy))
vmax_energy = max(max(set1_samples_energy), max(set2_samples_energy))
vmin_value = min(min(set1_samples_value), min(set2_samples_value))
vmax_value = max(max(set1_samples_value), max(set2_samples_value))

print(vmin_energy, vmax_energy)
print(vmin_value, vmax_value)

ax1.scatter(list(range(len(set1_samples_energy))),
            set1_samples_energy, c='red', marker='|')
ax1.set_ylim(vmin_energy, vmax_energy)

ax2.scatter(list(range(len(set1_samples_value))),
            set1_samples_value, c='red', marker='|')
ax2.set_ylim(vmin_value, vmax_value)

ax3.scatter(list(range(len(set2_samples_energy))),
            set2_samples_energy, c='blue', marker='|')
ax3.set_ylim(vmin_energy, vmax_energy)

ax4.scatter(list(range(len(set2_samples_value))),
            set2_samples_value, c='blue', marker='|')
ax4.set_ylim(vmin_value, vmax_value)


# Tidy up the figure
ax1.grid(True)
ax1.set_title('Solution Energy')
ax1.set_ylabel('Normal Embedding')
ax2.grid(True)
ax2.set_title('Solution Objective Value')
ax3.grid(True)
ax3.set_xlabel('Solution Index')
ax3.set_ylabel('Clique Embedding')
ax4.grid()
ax4.set_xlabel('Solution Index')

# Get timestamp
date_obj = datetime.now()
date = 'Y{:04}M{:02}D{:02}h{:02}m{:02}s{:02}'.format(
    date_obj.year, date_obj.month, date_obj.day, date_obj.hour, date_obj.minute, date_obj.second)

folder_name = "scatters_energy_vs_objective_value"

# Check if folder exists and creates if not
if not os.path.exists('images/' + folder_name):
    os.makedirs('images/' + folder_name)

fig.text(0.5, 0.005, 'How to interpret: The lower the value, the better. Hence, the bigger the share of solutions in the lowest value levels, the better.',
         ha='center', size='xx-small')

output_name = f'N{N}B{B}q{q}P{P}W{work_id}{date}'
fig.suptitle('Scatters Energy and Objective Value - ' + output_name)

# Save as 2160p image
plt.savefig(
    f'images/{folder_name}/{output_name}.png', dpi=360)
plt.show()
