import numpy as np
import json
import os

# Step 1: Get parameters N, q, B, P, tickers, sigma, and mu from data
f = open('data/out_diversified_N64_p1mo_i1d.json')
data = json.load(f)

N = data['N']               # Universe size

folder_name = 'results/N64_B0.5_diversified_classical'

for filename in os.listdir(folder_name):
    if '.lp.out' in filename:
        with open(f'{folder_name}/{filename}') as ff:
            solution = np.zeros(N, dtype=int)
            for line in ff.readlines():
                if 'x(' in line:
                    solution[int(line[2:].split(')')[0]) - 1] = 1
            solution_dict = {'solution': solution.tolist()}

            print(solution_dict)
            json_file = filename.replace(".lp.out", ".json")
            with open(f'{folder_name}/{json_file}', 'w') as fff:
                json.dump(solution_dict, fff)