#triangular matriks
from numpy import array
from numpy import tril
from numpy import triu

#define square matriks
M = array ([
    [1,2,3],
    [1,2,3],
    [1,2,3]])
print(M)

#lower triangular matriks
lower = tril (M)
print(lower)

#upper triangular matriks
upper = triu (M)
print(upper)