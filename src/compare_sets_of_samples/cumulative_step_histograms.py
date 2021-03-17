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

ax1.hist(set1_samples_energy, 1000, density=True, histtype='step',
         cumulative=True, label='normal')

ax1.hist(set2_samples_energy, 1000, density=True, histtype='step',
         cumulative=True, label='clique')

ax2.hist(set1_samples_value, 1000, density=True, histtype='step',
         cumulative=True, label='normal')

ax2.hist(set2_samples_value, 1000, density=True, histtype='step',
         cumulative=True, label='clique')

# Tidy up the figure
fig.suptitle('Cumulative step histograms')
ax1.grid(True)
ax1.legend(loc='right')
ax1.set_title('Solution Energies')
ax1.set_xlabel('Solution Energy in D-Wave System')
ax1.set_ylabel('Likelihood of occurrence')
ax2.grid(True)
ax2.legend(loc='right')
ax2.set_title('Objective Values')
ax2.set_xlabel('Solution Objective Value')
ax2.set_ylabel('Likelihood of occurrence')

# Get timestamp
date_obj = datetime.now()
date = 'Y{:04}M{:02}D{:02}h{:02}m{:02}s{:02}'.format(
    date_obj.year, date_obj.month, date_obj.day, date_obj.hour, date_obj.minute, date_obj.second)

# Check if folder exists and creates if not
if not os.path.exists('images/cumulative_step_histograms'):
    os.makedirs('images/cumulative_step_histograms')

fig.text(0.5,0.005,'How to interpret: For every `x`, its associated `y` is the percentage of samples with a value lower than it.\nTherefore, for any `x`, the higher its `y` value, the better.', ha='center', size='xx-small')

# Save as 2160p image
plt.savefig(
    f'images/cumulative_step_histograms/N{N}B{B}q{q}P{P}W{work_id}{date}.png', dpi=360)
plt.show()
