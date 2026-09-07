import numpy as np

def Strassen(A,B):
    A = np.asarray(A)
    B = np.asarray(B)

    n = A.shape[0]

    if n<=2:
        c11 = ((A[0][0]*B[0][0]) + (A[0][1]*B[1][0]))
        c12 = ((A[0][0]*B[0][1]) + (A[0][1]*B[1][1]))
        c21 = ((A[1][0]*B[0][0]) + (A[1][1]*B[1][0]))
        c22 = ((A[1][0]*B[0][1]) + (A[1][1]*B[1][1]))

        return np.block([[c11, c12], 
                         [c21, c22]])

    mid = n//2

    A11, A12 = A[:mid, :mid], A[:mid ,mid:]
    A21, A22 = A[mid: , :mid], A[mid: , mid:]

    B11, B12 = B[:mid, :mid], B[:mid ,mid:]
    B21, B22 = B[mid: , :mid], B[mid: , mid:]

    P = Strassen(A11, B12 - B22)
    Q = Strassen(A11+A12, B22)
    R = Strassen(A21+A22, B11)
    S = Strassen(A22, B21 - B11)
    T = Strassen(A11+A22, B11+B22)
    U = Strassen(A12-A22, B21+B22)
    V = Strassen(A11-A21, B11+B12)
    C11 = T + S - Q + U
    C12 = P + Q
    C21 = R + S
    C22 = T + P - R - V

    return np.block([[C11, C12],
                     [C21, C22]])

A = np.array([[7,8], [9,8]])
B = np.array([[14,12],[2,20]])

result = Strassen(A,B)
Strassen(A,B)
print(result)

