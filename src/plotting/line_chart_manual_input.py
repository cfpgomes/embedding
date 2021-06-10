import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['CMU Serif']
from datetime import datetime
import os

# 2 columns, 9 per 6 inches figure
fig, ax1 = plt.subplots(figsize=(4, 4))

x = [0.125, 0.250, 0.375, 0.5, 0.625, 0.75, 0.875, 1, 1.125, 1.25, 1.375, 1.5]

# # N = 16
# # Try 1
# ax1.plot(x, [18.844, 1.075, 1.057, 1.099, 1.098, 1.12, 1.123, 1.119, 1.099, 1.092, 1.11, 1.101], label='try 1', color='mistyrose')

# # Try 2
# ax1.plot(x, [2.314, 1.098, 1.109, 1.114, 1.11, 1.077, 1.12, 1.141, 1.114, 1.101, 1.169, 1.126], label='try 2', color='navajowhite')

# # Try 3
# ax1.plot(x, [1.551, 1.07, 1.032, 1.04, 1.074, 1.141, 1.134, 1.141, 1.101, 1.092, 1.092, 1.12], label='try 3', color='lavender')

# # Avg
# ax1.plot(x, [7.569666667, 1.081, 1.066, 1.084333333, 1.094, 1.112666667, 1.125666667, 1.133666667, 1.104666667, 1.095, 1.123666667, 1.115666667], label='average', color='black')

# # Default chain strength
# ax1.plot([0, 0.125, 0.250, 0.375, 0.5, 0.625, 0.75, 0.875, 1, 1.125, 1.25, 1.375, 1.5], [1.077333333, 1.077333333, 1.077333333, 1.077333333, 1.077333333, 1.077333333, 1.077333333, 1.077333333, 1.077333333, 1.077333333, 1.077333333, 1.077333333, 1.077333333], label='default', color='r')


# # N = 32
# # Try 1
# ax1.plot(x, [1.767, 1.178, 1.203, 1.331, 1.269, 1.429, 1.43, 1.25, 1.142, 1.355, 1.352, 1.345], label='try 1', color='mistyrose')

# # Try 2
# ax1.plot(x, [1.813, 1.256, 1.336, 1.257, 1.322, 1.299, 1.307, 1.35, 1.327, 1.266, 1.198, 1.325], label='try 2', color='navajowhite')

# # Try 3
# ax1.plot(x, [1.76, 1.266, 1.235, 1.325, 1.332, 1.27, 1.229, 1.252, 1.248, 1.303, 1.247, 1.391], label='try 3', color='lavender')

# # Avg
# ax1.plot(x, [1.78, 1.233333333, 1.258, 1.304333333, 1.307666667, 1.332666667, 1.322, 1.284, 1.239, 1.308, 1.265666667, 1.353666667], label='average', color='black')

# # Default chain strength
# ax1.plot([0, 0.125, 0.250, 0.375, 0.5, 0.625, 0.75, 0.875, 1, 1.125, 1.25, 1.375, 1.5], [1.811333333, 1.811333333, 1.811333333, 1.811333333, 1.811333333, 1.811333333, 1.811333333, 1.811333333, 1.811333333, 1.811333333, 1.811333333, 1.811333333, 1.811333333], label='default', color='r')


# N = 64
# Try 1
ax1.plot(x, [1.977, 1.474, 1.58, 1.5, 1.41, 1.523, 1.587, 1.526, 1.539, 1.61, 1.465, 1.423], label='try 1', color='mistyrose')

# Try 2
ax1.plot(x, [2.185, 1.55, 1.492, 1.502, 1.503, 1.516, 1.489, 1.485, 1.43, 1.549, 1.508, 1.597], label='try 2', color='navajowhite')

# Try 3
ax1.plot(x, [1.641, 1.539, 1.384, 1.495, 1.503, 1.474, 1.409, 1.47, 1.547, 1.568, 1.538, 1.362], label='try 3', color='lavender')

# Avg
ax1.plot(x, [1.934333333, 1.521, 1.485333333, 1.499, 1.472, 1.504333333, 1.495, 1.493666667, 1.505333333, 1.575666667, 1.503666667, 1.460666667], label='average', color='black')

# Default chain strength
ax1.plot([0, 0.125, 0.250, 0.375, 0.5, 0.625, 0.75, 0.875, 1, 1.125, 1.25, 1.375, 1.5], [1.997, 1.997, 1.997, 1.997, 1.997, 1.997, 1.997, 1.997, 1.997, 1.997, 1.997, 1.997, 1.997], label='default', color='r')

# Tidy up the figure
# (ax1_bottom, ax1_top) = ax1.get_ylim()

ax1.grid(axis='y')
# ax1.set_title(title)
ax1.set_xlim(0, 1.5)
ax1.set_ylim(1, 2)
ax1.set_ylabel('Epsilon Indicator')
ax1.set_xlabel('Chain Strength as a Factor of $\mathregular{M_Q}$')
ax1.legend()


# Get timestamp
date_obj = datetime.now()
date = 'Y{:04}M{:02}D{:02}h{:02}m{:02}s{:02}'.format(
    date_obj.year, date_obj.month, date_obj.day, date_obj.hour, date_obj.minute, date_obj.second)

folder_name = 'line_chart_manual_input'

# Check if folder exists and creates if not
if not os.path.exists('images/' + folder_name):
    os.makedirs('images/' + folder_name)

# fig.text(0.5, 0.005, 'How to interpret: The epsilon indicator is the minimum factor by which the annealer set has to be multiplied in the objective so as to weakly dominate the classical set.\nHence, the closer to 1 is the epsilon indicator, the better the annealer set.',
#          ha='center', size='xx-small')

output_name = f'{date}'
# fig.suptitle('Boxplots - ' + output_name)

# Save as 2 1 6 0p image
plt.savefig(
    f'images/{folder_name}/{output_name}.pdf', dpi=360)
plt.show()
