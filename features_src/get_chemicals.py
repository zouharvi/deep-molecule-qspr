#!/usr/bin/env python3

from chemicals.critical import critical_data_Yaws
from chemicals import CAS_from_any, Tb, Tm, MW
import numpy as np
import pandas as pd
from networkx.algorithms import *
from pysmiles import read_smiles
import calculate_indices
import math


def count_atom_occurencies(G):
    vertices_occ = get_vertex_occurencies(G)
    atom_occurencies = {}
    atoms = G.nodes(data='element')
    for i in range(len(vertices_occ)):
        atom_type = atoms[i]
        if atom_type in atom_occurencies:
            atom_occurencies[atom_type] += vertices_occ[i]
        else:
            atom_occurencies[atom_type] = vertices_occ[i]
    atom_occurencies.update(get_edge_occurencies(G))

    return atom_occurencies
    

def get_vertex_occurencies(G):
    all_shortest_paths = shortest_path(G)
    vertices_occ = [ 0 for x in range(len(G))]
    for paths_from_v in all_shortest_paths.values() :
        for path in paths_from_v.values():
            for v in path:
                vertices_occ[v] += 1    
    vertices_occ = [x/(2*len(G)) for x in vertices_occ]
    return vertices_occ


def get_edge_occurencies(G):
    all_shortest_paths = shortest_path(G)
    atoms = G.nodes(data='element')
    edges_occ = {}
    order =  list(G.edges(data='order'))
    dict_order = {}
    for o in order:
        dict_order[str(o[0]) + '-'+ str(o[1])] = o[2]
        dict_order[str(o[1]) + '-'+ str(o[0])] = o[2]
    for paths_from_v in all_shortest_paths.values() :
        for path in paths_from_v.values():
            for i in range(len(path)-1):
                j = i+1
                vertices = sorted([atoms[path[i]],atoms[path[j]]])
                ord_dict_key = str(path[i]) + '-' + str(path[j])
                dict_key = vertices[0] + str(dict_order[ord_dict_key]) + vertices[1]
                if dict_key in edges_occ:
                    edges_occ[dict_key] += 1/(len(G)-1)
                else:
                    edges_occ[dict_key] = 1/(len(G)-1)
    return edges_occ
           
chemicals = pd.read_pickle("smiles.pickle")
chemicals_data = []
print(chemicals)
    
headers = []
targets = []
i = 0
for index, row in chemicals.iterrows(): 
    if not is_tree(G):
        continue
    i+=1
    if i%1 == 0:
        print(i)
    G = read_smiles(row["smiles"], explicit_hydrogen=True)
    try:
        mol_weight = MW(CAS_from_any(row["chemicals"]))
        boiling_point =  Tb(CAS_from_any(row['chemicals']))
    except(ValueError):
        continue
    if boiling_point == None or mol_weight == None:
        continue
    occ = count_atom_occurencies(G)
    occ.update({'boiling_point': boiling_point})
    """
    try:
        with timeout(2, exception=RuntimeError):
            occ.update({'GP_index': calculate_indices.calcuate_pisanski(G)})
    except RuntimeError:
        continue
    """
    occ.update({'ecc_index': sum(list(eccentricity(G).keys()))})
    wiener_index = calculate_indices.calculate_wiener(G)
    if wiener_index == 0:
        continue
    occ.update({'wiener_index': math.log(wiener_index)})        
    occ.update({'mol_weight': math.sqrt(mol_weight)/10})
    occ.update({'mol_length': len(G)})
    dia = diameter(G)
    occ.update({'side_chain': (len(G) - dia)/ dia })
    headers = list(set(headers) | set(occ.keys())) 
    chemicals_data.append(occ)

dataset = {x : [] for x in headers}
for chemical in chemicals_data:
    for i in range(len(dataset.keys())):
        if headers[i] in chemical:
            dataset[headers[i]].append(chemical[headers[i]])
        else:
            dataset[headers[i]].append(0)
original_df = pd.DataFrame(dataset)
original_df.to_pickle("boil_heavy.pickle")
print(original_df)

    

