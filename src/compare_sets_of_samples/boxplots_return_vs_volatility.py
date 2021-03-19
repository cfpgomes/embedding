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

set1_samples_expected_return = []
set2_samples_expected_return = []

set1_samples_volatility = []
set2_samples_volatility = []

with open(set1_filename) as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader, None)  # Skip header
    for row in reader:
        sol = np.array(list(map(float, row[:-3])))
        sol_expected_return = np.transpose(mu).dot(sol)
        sol_volatility = q*np.transpose(sol).dot(sigma).dot(sol)

        set1_samples_expected_return.extend(
            [sol_expected_return for i in range(int(row[-1]))])
        set1_samples_volatility.extend(
            [sol_volatility for i in range(int(row[-1]))])

with open(set2_filename) as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader, None)  # Skip header
    for row in reader:
        sol = np.array(list(map(float, row[:-3])))
        sol_expected_return = np.transpose(mu).dot(sol)
        sol_volatility = q*np.transpose(sol).dot(sigma).dot(sol)

        set2_samples_expected_return.extend(
            [sol_expected_return for i in range(int(row[-1]))])
        set2_samples_volatility.extend(
            [sol_volatility for i in range(int(row[-1]))])

# 2 columns, 9 per 6 inches figure
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(9, 6))

ax1_boxplots_dic = ax1.boxplot(
    [set1_samples_expected_return, set2_samples_expected_return], labels=['normal', 'clique'])

ax2_boxplots_dic = ax2.boxplot(
    [set1_samples_volatility, set2_samples_volatility], labels=['normal', 'clique'])

# Draw medians
for line in ax1_boxplots_dic['medians']:
    # get position data for median line
    x, y = line.get_xydata()[1]  # top of median line
    num = line.get_data()[1][1]
    # overlay median value
    # draw on right side
    ax1.text(x, y, f'{num:.3f}', horizontalalignment='left')

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


# Tidy up the figure
ax1.grid(True)
ax1.set_ylabel('Expected Return')
ax1.set_xlabel('Embedding')
ax2.grid(True)
ax2.set_ylabel('Volatility')
ax2.set_xlabel('Embedding')


# Get timestamp
date_obj = datetime.now()
date = 'Y{:04}M{:02}D{:02}h{:02}m{:02}s{:02}'.format(
    date_obj.year, date_obj.month, date_obj.day, date_obj.hour, date_obj.minute, date_obj.second)

folder_name = "boxplots_return_vs_volatility"

# Check if folder exists and creates if not
if not os.path.exists('images/' + folder_name):
    os.makedirs('images/' + folder_name)

fig.text(0.5, 0.005, 'How to interpret: The higher the expected return, the better. The lower the volatility, the better.',
         ha='center', size='xx-small')

output_name = f'N{N}B{B}q{q}P{P}W{work_id}{date}'
fig.suptitle('Boxplots - ' + output_name)

# Save as 2160p image
plt.savefig(
    f'images/{folder_name}/{output_name}.png', dpi=360)
plt.show()
