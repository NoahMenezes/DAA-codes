INF=float('inf')
G={
    1:{2:1, 3:8, 4:6}, 2:{5:1, 6:14, 7:14},
    3:{5:8, 6:11, 7:3}, 4:{5:10, 7:4},
    5:{8:13, 9:10, 10:4}, 6:{8:7, 9:8, 10:10},
    7:{9:10, 10:12}, 8:{11:13, 12:4, 13:2},
    9:{11:3, 12:3, 13:8}, 10:{11:8, 12:4, 13:5},
    11:{14:8}, 12:{14:4}, 13:{14:7}, 14:{}
}

stage={1:1, 2:2, 3:2, 4:2, 5:3, 6:3, 7:3,
       8:4, 9:4, 10:4, 11:5, 12:5, 13:5, 14:6}
def fgraph():
    cost, d={i:INF for i in G}, {}
    cost[14]=0

    for v in range(13,0,-1):
        cost[v], d[v]=min((w+cost[r], r) for r,w in G[v].items())
        print(f"Cost({v}, Stage {stage[v]}) = {int(cost[v])}, d = {d[v]}")

    path=[1]
    while path[-1]!=14:
        path.append(d[path[-1]])
    print("Path ="," -> ".join(map(str,path)))
    print("Mincost =", cost[1])

def bgraph():
    cost,d={i:INF for i in G}, {}
    cost[1]=0

    for v in range(2, 15):
        cost[v], d[v] = min(
            (cost[u] + G[u][v], u)
            for u in G if v in G[u]
        )
        print(f"Cost({v}, Stage {stage[v]}) = {int(cost[v])}, d = {d[v]}")
    path=[14]

    while path[-1]!=1:
        path.append(d[path[-1]])
    path.reverse()
    print("Path ="," -> ".join(map(str,path)))
    print("Mincost =", cost[14])
fgraph()
bgraph()