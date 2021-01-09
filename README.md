# MGB (Molecules Go Brr)

TODO:

Wiener Index.

## Model Zoo

```
L-In-1
L-In-5,l-5-1
L-In-10,l-10-5,l-5-1
```

## Data Zoo

C = Convergence (1 to 5)

| File | Method | Notes | Model | Train | Valid | C |
|-|-|-|-|-|-|-|
|boil0 | Weighted verices and amount of bonds for each bond category as features |vertices weighted, bonds unweighted|L-In-1 | 39.735 | 41.939 | 5 | 
|boil1| Weighted vertices and edges on a small amount of data |non-normalized|L-In-1 | 127.701 | 107.297 | 2 | 
|melt1| Weighted vertices and edges on a small amount of data |non-normalized|L-In-1 | 122.179 | 138.810 | 2 |
|boil2| boil1, Threshold for verticies shifted from 40 to 60 |non-normalized|L-In-1 | 95.877 | 91.354 | 2 |
|boil2| boil2, Verticies only |non-normalized |L-In-1 | 65.628 | 61.316 | 5 |
|boil3 | Weighted vertices and edges | normalized data, added feature: molecule_length; mol_weight / 100 | L-In-1 | 31.164 | 27.502 | 5 |
|boil4 | Weighted vertices and edges | same as boil3 + hydrogen vertices added | L-In-1 | 24.025 | 23.512 | 5 |
|boil4 |  | | L-In-8,L-8-4,L-4-1 | 8.358 |  17.468 | 4 |

## Normalization
Vertices - by total amount of vertices

Edges, bonds - by total amount of edges
