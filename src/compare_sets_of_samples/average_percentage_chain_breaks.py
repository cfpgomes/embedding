import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from datetime import datetime
import os
import json
import csv

set_foldername = 'results/scenarioB1_N8_Pformulated_Cformulated1.500_annealer'

sum_fraction_chain_breaks = 0
num_samples = 0

for filename in os.listdir(set_foldername):
    with open(set_foldername+'/'+filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader, None)  # Skip header
        for row in reader:
            sum_fraction_chain_breaks += float(row[-3])
            num_samples += int(row[-1])

avg_fraction_chain_breaks = sum_fraction_chain_breaks/num_samples
print(f'{sum_fraction_chain_breaks}')
print(f'{num_samples}')
print(f'{avg_fraction_chain_breaks:0.5f}')