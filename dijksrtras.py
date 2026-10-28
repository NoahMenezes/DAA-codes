INF = float('inf')

def Shortest_Path(v,cost, distance,parent,n):
    S = [False]*n

    for i in range(n):
        S[i] = False
        distance[i] = cost[v][i]

        if cost[v][i] != INF and i != v:
            parent[i] = v
        else:
            parent[i] = -1

    S[v] = True
    distance[v] = 0

    for _ in range(2,n):
        u = -1
        mindist = INF

        for i in range(n):
            if not S[i] and distance[i] < mindist:
                mindist = distance[i]
                u = i

        if u == -1:
            break

        S[u] = True

        for w in range(n):
            if not S[w] and cost[u][w] != INF:
                if distance[w] > distance[u] + cost[u][w]:
                    distance[w] = distance[u] + cost[u][w]
                    parent[w] = u

def get_path(parent,dest):
    path = []
    curr = dest
    while curr != -1:
        path.append(curr+1)
        curr = parent[curr]
    path.reverse()
    return "->".join(map(str,path))

cost_matrix = [
    [0, 11, INF, INF, INF, INF, INF, INF],
    [39, 0,  INF, 33, 30, 60, 89, 91],
    [INF,  27, 0,  24, 23, 21, 17, 12],
    [83,  INF, 64, 0,  INF, INF, 51, INF],
    [INF, 29, 80, INF, 0,  13, 71, 19],
    [INF,  48, 71, INF, INF, 0,  70, INF],
    [INF,  INF, INF, 88, INF, 46, 0,  69],
    [68, INF, 58, 32, 38, 33, 13, 0]
]

n = len(cost_matrix)
distance = [0]*n
source = 0
parent = [-1]*n
Shortest_Path(source,cost_matrix,distance,parent,n)

print("Shortest Path Results: ")
print(f"{'Source':<8} | {'Destination':<12} | {'Distance':<10} | {'Path'}")
for i in range(n):

    if i == source:
        continue

    ans = int(distance[i]) if distance[i] != INF else "Unreachable"
    path_str = get_path(parent,i) if distance[i] != INF else "-"
    print(f"{(source+1):<8} | {(i+1):<12} | {ans:<10} | {path_str}")


