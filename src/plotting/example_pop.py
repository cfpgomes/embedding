import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['CMU Serif']

arr = np.array([[1,  0,  1,  0],
                [0, -1, -2,  0],
                [2,  0,  2,  0],
                [2,  0,  1,  3]])

print(arr)

mu = np.mean(arr, 1)

print(mu)

sigma = np.cov(arr)

print(sigma)

label = []
exp_ret = []
vol = []

for a in [1,0]:
    for b in [1,0]:
        for c in [1,0]:
            for d in [1,0]:
                if a + b + c + d != 2:
                    continue
                print(a,b,c,d)
                x = np.array([a,b,c,d])
                exp_ret.append(mu.dot(x))
                vol.append(x.dot(sigma).dot(x))

print(exp_ret)
print(vol)

fig, ax1 = plt.subplots(figsize=(5, 4)) 

ax1.scatter([vol[0], vol[2], vol[3], vol[5]],[exp_ret[0], exp_ret[2], exp_ret[3], exp_ret[5]], color = 'limegreen', label='non-dominated point')
ax1.scatter([vol[1], vol[4]],[exp_ret[1], exp_ret[4]], color = 'firebrick', label='dominated point')


for i, txt in enumerate(['$\mathcal{P}_1$','$\mathcal{P}_2$','$\mathcal{P}_3$','$\mathcal{P}_4$','$\mathcal{P}_5$','$\mathcal{P}_6$']):
    ax1.annotate(txt, (vol[i]+0.03, exp_ret[i]+0.03))

# Tidy up the figure
(ax1_left, ax1_right) = ax1.get_xlim()
(ax1_bottom, ax1_top) = ax1.get_ylim()
ax1.grid(True)
ax1.legend()
ax1.set_xlim(0, 4.5)
ax1.set_ylim(ax1_bottom, 3)
ax1.set_ylabel('Expected Return')
ax1.set_xlabel('Volatility')

plt.show()