import matplotlib.pyplot as plt
from datetime import datetime
import os

scenario_name = "Scenario_A2B3_N64_B0.8"
folder_name = 'boxplots_simple'

# Get timestamp
date_obj = datetime.now()
date = 'Y{:04}M{:02}D{:02}h{:02}m{:02}s{:02}'.format(
    date_obj.year, date_obj.month, date_obj.day, date_obj.hour, date_obj.minute, date_obj.second)
output_name = f'{scenario_name}_{date}'

# Check if folder exists and creates if not
if not os.path.exists('images/' + folder_name):
    os.makedirs('images/' + folder_name)

lessDmoreS = [1.666, 1.674, 1.666, 1.766, 1.803]
mediumDmediumS = [1.640, 1.691, 1.630, 1.664, 1.579]
moreDlessS = [1.932, 1.873, 1.682, 1.656, 1.619]

fig1, ax1 = plt.subplots(figsize=(9, 6))
ax1.set_title(output_name)
ax1.boxplot([lessDmoreS, mediumDmediumS, moreDlessS], labels=['lessDmoreS', 'mediumDmediumS', 'moreDlessS'])
ax1.yaxis.grid(True)
(ax1_bottom, ax1_top) = ax1.get_ylim()
ax1.set_ylim(1, ax1_top)

# Save as 2 1 6 0p image
plt.savefig(
    f'images/{folder_name}/{output_name}.png', dpi=360)
plt.show()