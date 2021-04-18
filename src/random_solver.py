import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from datetime import datetime
import os
import json
import csv

folder_name = 'scenarioB3_N64_B0.5_random'

N = 64
B = int(N * 0.5)

allocated = 2104

# Check if folder exists and creates if not
if not os.path.exists('results/' + folder_name):
    os.makedirs('results/' + folder_name)


def rand_bin_array(B, N):
    arr = np.zeros(N, dtype=int)
    arr[:B] = 1
    np.random.shuffle(arr)
    return list(arr)


with open('results/' + folder_name + '/sample.csv', 'w') as f:
    f.write('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,chain_break_fraction,energy,num_occurrences\n')

    for _ in range(allocated):
        sol = rand_bin_array(B, N)
        for x in sol:
            f.write(str(x)+',')
        f.write('0.0,0.0,1\n')
        