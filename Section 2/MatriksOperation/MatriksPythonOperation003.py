#matriks scalar multiplication
from numpy import array

#define matriks
A = array ([
    [1,2],
    [3,4],
    [5,6]
])


print('Nilai A')
print(A)

#define scalar
b = 0.5
print('Nilai B')
print(b)

#multiply
C = A * b
print('Hasil Scalar A * b')
print(C)