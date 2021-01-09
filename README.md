# MGB (Molecules Go Brr)

TODO:

Wiener Index.

## Model Zoo

```
l-I-1
l-I-5,l-5-1
l-I-10,l-10-5,l-5-1
```

## Data Zoo


|Data|Method|Model|Train|Valid|Convergence| Notes |
|-|-|-|-|-|-||
|trees1{X,Y}| TODO | l-I-1 | 39.735 | 41.939 | X | |
|boil1| Weighted vertices and edges on a small amount of data | l-I-1 | 127.701 | 107.297 | - | |
|melt1| Weighted vertices and edges on a small amount of data | l-I-1 | 122.179 | 138.810 | - | |
|boil2| boil1, Threshold for verticies shifted from 40 to 60 | l-I-1 | 95.877 | 91.354 | - | |
|boil2| boil2, Verticies only | l-I-1 | 65.628 | 61.316 | X | |
| | | l-I-1 | | | - | |
|boil3 | Weighted vertices and edges | | | | - | non-normalized data, added feature: molecule_length |
