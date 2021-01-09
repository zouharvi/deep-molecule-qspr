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


|data|method|model|train|valid|note|
|-|-|-|-|-|-|
|trees1{X,Y}| TODO | l-I-1 | 39.735 | 41.939 | Stabilizes after e4000 | 
|{boil,melt}1| Weighted vertices and edges on a small amount of data | l-I-1 | 127.701 | 107.297 | Does not converge. Melting point slightly worse. |
|boil2| TODO | l-I-1 | 95.877 | 91.354 | Does not converge. |
| | | l-I-1 | | | |
