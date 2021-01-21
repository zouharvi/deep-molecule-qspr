# MGB (Molecules Go Brr)

TODO:

Wiener Index.

## Model Zoo

```
L-In-1
L-In-5,l-5-1
L-In-10,l-10-5,l-5-1
```

Leaky RELu(0.01)

## Data Zoo

C = Convergence, 1 (no) to 5 (best)

| File | Method | Notes | Model | Train | Valid | C |
|-|-|-|-|-|-|-|
|boil0 | Weighted verices and amount of bonds for each bond category as features |vertices weighted, bonds unweighted|L-In-1 | 39.735 | 41.939 | 5 | 
|boil1 | Weighted vertices and edges on a small amount of data |non-normalized| L-In-1 | 127.701 | 107.297 | 2 | 
|melt1 | Weighted vertices and edges on a small amount of data |non-normalized| L-In-1 | 122.179 | 138.810 | 2 |
|boil2 | boil1, Threshold for verticies shifted from 40 to 60 |non-normalized| L-In-1 | 95.877 | 91.354 | 2 |
|boil2 | boil2, Verticies only |non-normalized | L-In-1 | 65.628 | 61.316 | 5 |
|boil3 | Weighted vertices and edges | normalized data, added feature: molecule\_length; mol\_weight / 100 | L-In-1 | 31.164 | 27.502 | 5 |
|boil4 | Weighted vertices and edges | same as boil3 + hydrogen vertices added | L-In-1 | 24.025 | 23.512 | 5 |
|boil4 | | | L-In-8,L-8-4,L-4-1 | 8.358 | 17.468 | 4 |
|boil5 | Weighted vertices and edges with respect to bond order | bug on edge weights fixed | L-In-1 | 18.438 | 18.860 | 5 |
|boil5 | | | L-28-5-5,L-5-5,L-5-1 | 16.683 | 17.545 | 4 |
|boil6 | Eccentrity index and unweighted wiener index features added | | L-30-1 | 18.512 | 18.927 | 4 |
|boil6 | | | L-30-15,L-15-10,L-10-1 (lr=0.005)| 10.774 | 12.912 | 4 |
|boil7 | Root of mol. weight | | L-30-1 (lr=0.0025) |17.962 | 18.351  |4|
|boil8 | "Density of side chains" | Number of molecules outside of the core divided by number of atoms in the core | L-31-1 lr0.0025 | 17.291 | 17.445| 4 |
|boil8 | | | L-31-15,L-15-10,L-10-1 lr0.0025 | 11.701 | 12.469 | 3 |
|boil9 |Only number of vertices and edges of given classes as features | | |  | |  |



## Normalization

Vertices - by total amount of vertices

Edges, bonds - by total amount of edges
