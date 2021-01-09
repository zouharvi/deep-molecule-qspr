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

C = Convergence
| File | Method | Notes | Model | Train | Valid | C |
|-|-|-|-|-|-|-|
|boil0 | Weighted verices and amount of bonds for each bond category as features ||L-In-1 | 39.735 | 41.939 | Y | vertices weighted, bonds unweighted|
|boil1| Weighted vertices and edges on a small amount of data ||L-In-1 | 127.701 | 107.297 | - |non-normalized |
|melt1| Weighted vertices and edges on a small amount of data ||L-In-1 | 122.179 | 138.810 | - |non-normalized  |
|boil2| boil1, Threshold for verticies shifted from 40 to 60 ||L-In-1 | 95.877 | 91.354 | - |non-normalized  |
|boil2| boil2, Verticies only | |L-In-1 | 65.628 | 61.316 | Y |non-normalized  |
|boil3 | Weighted vertices and edges | non-normalized data, added feature: molecule_length | L-In-1 | | | - |
