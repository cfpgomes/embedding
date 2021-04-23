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

lessDmoreS = [ 1.988]
mediumDmediumS = [float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]
moreDlessS = [float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]

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