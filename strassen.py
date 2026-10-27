import numpy as np
import time
import timeit

def Normal_Multiplication(A, B):
    n = A.shape[0]
    # Initialize a matrix of zeros
    C = np.zeros((n, n), dtype=int)
    # Standard O(N^3) multiplication using 3 loops
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def Strassen(A, B):
    A = np.asarray(A)
    B = np.asarray(B)

    n = A.shape[0]

    if n <= 2:
        c11 = ((A[0][0]*B[0][0]) + (A[0][1]*B[1][0]))
        c12 = ((A[0][0]*B[0][1]) + (A[0][1]*B[1][1]))
        c21 = ((A[1][0]*B[0][0]) + (A[1][1]*B[1][0]))
        c22 = ((A[1][0]*B[0][1]) + (A[1][1]*B[1][1]))

        return np.block([[c11, c12], 
                         [c21, c22]])

    mid = n // 2

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
A=np.array([[1,2],
            [3,4]])
B=np.array([[5,6],
            [7,8]])
print("Normal Multiplication Result:")
print(Normal_Multiplication(A, B))
print("\nStrassen Multiplication Result:")
print(Strassen(A, B))
if __name__ == "__main__":
    sizes = [32, 64, 128, 256, 512]
    
    print(f"{'Size (N)':<8} | {'Normal time()':<15} | {'Normal timeit':<15} | {'Strassen time()':<17} | {'Strassen timeit':<15}")
    print("-" * 81)
    
    for n in sizes:
        A = np.random.randint(1, 10, size=(n, n))
        B = np.random.randint(1, 10, size=(n, n))
        
        start = time.time()
        Normal_Multiplication(A, B)
        normal_time = time.time() - start
        
        stmt_normal = lambda: Normal_Multiplication(A, B)
        normal_timeit = timeit.timeit(stmt_normal, number=1)
        
        # Benchmarking Strassen Multiplication
        start = time.time()
        Strassen(A, B)
        strassen_time = time.time() - start
        
        stmt_strassen = lambda: Strassen(A, B)
        strassen_timeit = timeit.timeit(stmt_strassen, number=1)
        
        # Print the row results
        print(f"{n:<8} | {normal_time:<15.6f} | {normal_timeit:<15.6f} | {strassen_time:<17.6f} | {strassen_timeit:<15.6f}")