#!/bin/python3

import numpy as np
import pickle

with open('data/treesY.pickle', 'rb') as f:
    dataTrainY = pickle.load(f)

avg = np.average(dataTrainY)
print(f'avg {avg:.3f}')
print(f'max {max(dataTrainY):.3f}')
print(f'min {min(dataTrainY):.3f}')
print(f'naive {np.sqrt(np.average([(x-avg)**2 for x in dataTrainY])):.3}')