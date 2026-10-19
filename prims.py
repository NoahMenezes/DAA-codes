INF = 999999
cost = [
    [INF, 68,  12,  49,  66,  17,  17,  INF,  69, 77],
    [68,  INF, 49,  29,  53,  79,  88,  61,  62,  15],
    [12,  49,  INF, INF, INF,  51, INF, INF,  82,  12],
    [49,  29,  INF, INF, 24,  68,  93,  95,  39,  99],
    [66,  53,  INF,  24,  INF, 53, 34,  14,  68,  76],
    [17,  79,  51,   68,  53, INF, 49,  11,  71,  58],
    [17,  88,  INF,  93, 34,  49,  INF, 29,50,  23],
    [INF, 61,  INF,  95,  14,  11,  29, INF, 67,  11],
    [69,  62,  82,  39,  68,  71,  50,  67,  INF, 24],
    [77,  15,  12,  99,  76,  58,  23, 11,  24,  INF],
]

n = len(cost)

selected = [False] * n
selected[0] = True

mst = []
total = 0
count = 1

for _ in range(n - 1):
    min_val = INF
    u = -1
    v = -1

    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and cost[i][j] < min_val:
                    min_val = cost[i][j]
                    u = i
                    v = j

    selected[v] = True
    mst.append((u, v))
    total += min_val
    print("Edge %d: (%d,%d)  cost = %d  | total = %d" % (count, u + 1, v + 1, min_val, total))
    count += 1

print("\nEdges in Minimum Spanning Tree:")
for a, b in mst:
    print(f"({a+1},{b+1})", end=" ")
print(f"\nMinimum Cost = {total}")
