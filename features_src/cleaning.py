#!/usr/bin/env python3

import pickle
import numpy as np
import pandas as pd


data = (pd.read_pickle("boil_heavy.pickle")).to_dict('list')
keys = list(data.keys())
features = list(data.values())
bad_indexes = []
for i in range(len(features)):
    if (len([x for x in features[i] if x!=0 ])< 50):
        bad_indexes.append(i)
        
by_molecules = np.transpose(features)
to_delete = []

for i in range(len(by_molecules)):
    for index in bad_indexes:
        if by_molecules[i][index]!=0:
            to_delete.append(i)

to_delete = sorted(set(to_delete), reverse=True)

for index in to_delete:
    for key in keys:
        data[key].pop(index)
        
features_to_delete = []

for key, value in data.items():
    if sum(value) == 0:
        features_to_delete.append(key)

for feature in features_to_delete:
    data.pop(feature, None)
        
print(len(data.keys()))
with open('boil12.pickle', 'wb') as handle:
    pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)


        
    
