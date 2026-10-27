
def print_matrices(k, A, P, n):
    print("\nk =", k)
    print("A matrix:")
    for i in range(n):
        print(A[i])

    print("P matrix:")
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append("-")
            else:
                row.append(P[i][j] + 1)
        print(row)

def get_path(i, j, P):
    if P[i][j] == i:
        return str(i + 1) + "-" + str(j + 1)

    return get_path(i, P[i][j], P) + "-" + str(j + 1)


def all_pairs_shortest_path():
    A = [
        [0, 17, 19, 25, 14, 28],
        [8, 0, 47, 9, 25, 27],
        [11, 25, 0, 24, 5, 11],
        [30, 38, 12, 0, 13, 24],
        [6, 11, 30, 16, 0, 26],
        [13, 14, 41, 14, 29, 0]
    ]

    n = len(A)
    P = [[i for j in range(n)] for i in range(n)]

    print_matrices(0, A, P, n)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]
                    P[i][j] = P[k][j]

        print_matrices(k + 1, A, P, n)

    print("\nShortest paths:")
    print("Source Destination Distance Path")

    for i in range(n):
        for j in range(n):
            if i != j:
                path = get_path(i, j, P)
                print(i + 1, j + 1, A[i][j], path)


all_pairs_shortest_path()
