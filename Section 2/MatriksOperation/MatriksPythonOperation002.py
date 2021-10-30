#matriks dot
from numpy import array

#1st matriks
A = array ([
    [1,2],
    [3,4],
    [5,6]
])

B = array ([
    [1,2],
    [3,4]
])

#multiply
C = A.dot(B)

#multiply using @
D = A @ B


print(A)
print(B)
print(C)
print(D)