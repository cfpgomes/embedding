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

# A3N64
# list_set_epsilons = [
#     [1.5896707140453368, 1.692115874229774, 1.5797159691954805, 1.544775608544733, 1.6306603596458091],
#     [1.1543709462719736, 1.1808555712929112, 1.1965189175682915, 1.2054586123321147, 1.1451164825300342],
#     [1.480961077552874, 1.439785049594824, 1.49521532395618, 1.4271771706844985, 1.4703703494825286],
#     [1.712487317392762, 1.8350719836858504, 1.8867041380744307, 1.6599045066687057, 1.8170283525044424]
#     ]

# A3N32
# list_set_epsilons = [
#     [1.2742794349447089, 1.2884689100696118, 1.2773672514016263, 1.2753373162832464, 1.2330931799174467],
#     [1.1022627340052333, 1.1040043866764444, 1.107290257993464, 1.1095633593648768, 1.1030412770134137],
#     [1.3211551275053297, 1.3375576459869927, 1.3547221236814633, 1.273461244430681, 1.3830779041288135],
#     [1.3999197317543246, 1.3725234793287475, 1.3100230533839459, 1.268457109826973, 1.317538884521333]
#     ]

# A3N16
list_set_epsilons = [
    [1.0252990521071133, 1.0, 1.0252990521071133, 1.0398904698739035, 1.0252990521071133],
    [1.0184926535860195, 1.0138186993022122, 1.0183204025272334, 1.0146279197185049, 1.0099975432282287],
    [1.024987806680736, 1.0717989664330105, 1.0, 1.0, 1.0617306209896549],
    [1.0807158822709637, 1.0628970589064997, 1.0355813783849832, 1.0017552368401965, 1.0628970589064997]
    ]

# 2 columns, 9 per 6 inches figure
fig, ax1 = plt.subplots(figsize=(9, 6))
ax1.boxplot(list_set_epsilons, labels=labels)

# Tidy up the figure
(ax1_bottom, ax1_top) = ax1.get_ylim()

ax1.grid(True)
ax1.set_title('N16')
ax1.set_ylim(1, ax1_top)
ax1.set_ylabel('Epsilon Indicator')
ax1.set_xlabel('Dataset')


# Get timestamp
date_obj = datetime.now()
date = 'Y{:04}M{:02}D{:02}h{:02}m{:02}s{:02}'.format(
    date_obj.year, date_obj.month, date_obj.day, date_obj.hour, date_obj.minute, date_obj.second)

folder_name = 'boxplots_manual_input'

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
