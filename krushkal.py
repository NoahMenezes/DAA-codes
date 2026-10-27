import heapq
INF = float('inf')

cost = [
    [INF, 16,  32,  81,  97,  54,  28,  37,  57,  21],
    [16,  INF, 53,  42,  47,  53,  49,  41,  95,  49],
    [32,  53,  INF, 86,  69,  50,  10,  88,  50,  56],
    [81,  42,  86,  INF, INF, INF, 73,  36,  16,  INF],
    [97,  47,  69,  INF, INF, 65,  INF, INF, 18,  26],
    [54,  53,  50,  INF, 65,  INF, 38,  75,  10,  55],
    [28,  49,  10,  73,  INF, 38,  INF, 20,  12,  52],
    [37,  41,  88,  36,  INF, 75,  20,  INF, 69,  78],
    [57,  95,  50,  16,  18,  10,  12,  69,  INF, 54],
    [21,  49,  56,  INF, 26,  55,  52,  78,  54,  INF],
]

def find(parent, i):
    while parent[i] > 0:
        i = parent[i]

    return i

def Union(parent, i, j):
    parent[i] = j

def Kruskal(cost):
    n = len(cost)
    parent = [-1] * (n+1)
    edges = []

    for i in range(n):
        for j in range(i+1,n):
            if cost[i][j] != INF:
                heapq.heappush(edges,(cost[i][j], i+1, j+1))

    i = 0
    mincost = 0
    print(f"{'T':<5} | {'1':<5} {'2':<5}")
    

    while i < n-1 and edges:
        weight, u, v = heapq.heappop(edges)
        j = find(parent, u)
        k = find(parent, v)
    
        if j != k:
            i += 1
            mincost += weight
            Union(parent, j, k)
            print(f"{i:<5} | {u:<5} {v:<5}")

    if i != n-1:
        print("No Spanning Tree\n")
    else:
        print(f"Mincost = {mincost}")

Kruskal(cost)