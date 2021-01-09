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
|Data|Method|Model|Train|Valid|C|
|-|-|-|-|-|-|
|trees1{X,Y}| TODO | L-In-1 | 39.735 | 41.939 | Y | 
|boil1| Weighted vertices and edges on a small amount of data | L-In-1 | 127.701 | 107.297 | - |
|melt1| Weighted vertices and edges on a small amount of data | L-In-1 | 122.179 | 138.810 | - |
|boil2| boil1, Threshold for verticies shifted from 40 to 60 | L-In-1 | 95.877 | 91.354 | - |
|boil2| boil2, Verticies only | L-In-1 | 65.628 | 61.316 | Y |
| | | L-In-1 | | | - |
