#diagonal matriks
from numpy import array
from numpy import diag

#define square matriks
M = array ([
    [1,2,3],
    [1,2,3],
    [1,2,3]
])
print(M)

#extract diagonal vector
d = diag(M)
print(d)

#create diagonal matriks from vector
D = diag (d)
print(D)
