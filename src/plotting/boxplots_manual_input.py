import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from datetime import datetime
import os
import json
import csv

scenario_name = 'scenarioA3'

labels = ['diversified', 'correlated', 'industry_diversified', 'industry_correlated']

list_set_epsilons = [
    [1.7588471190599633, 1.8468055964402361, 1.541412849083435, 1.8439764280058868, 1.661133731808539],
    [1.3064818016221893, 1.373028558503523, 1.2669673625727889, 1.3423348475758754, 1.3221942289753006],
    [1.480961077552874, 1.439785049594824, 1.49521532395618, 1.4271771706844985, 1.4703703494825286],
    [1.712487317392762, 1.8350719836858504, 1.8867041380744307, 1.6599045066687057, 1.8170283525044424]
    ]

# 2 columns, 9 per 6 inches figure
fig, ax1 = plt.subplots(figsize=(9, 6))
ax1.boxplot(list_set_epsilons, labels=labels)

# Tidy up the figure
(ax1_bottom, ax1_top) = ax1.get_ylim()

ax1.grid(True)
ax1.set_title('N64')
ax1.set_ylim(1, ax1_top)
ax1.set_ylabel('Epsilon Indicator')
ax1.set_xlabel('Dataset')


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
