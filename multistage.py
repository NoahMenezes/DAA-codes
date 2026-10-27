INF = float('inf')
graph = {
    1: {2: 1, 3: 8, 4: 6},
    2: {5: 1, 6: 14, 7: 14},
    3: {5: 8, 6: 11, 7: 3},
    4: {5: 10, 7: 4},
    5: {8: 13, 9: 10, 10: 4},
    6: {8: 7, 9: 8, 10: 10},
    7: {9: 10, 10: 12},
    8: {11: 13, 12: 4, 13: 2},
    9: {11: 3, 12: 3, 13: 8},
    10: {11: 8, 12: 4, 13: 5},
    11: {14: 8},
    12: {14: 4},
    13: {14: 7},
    14: {}
}
n = 14  
k = 6   
vertex_to_stage = {
    1: 1,
    2: 2, 3: 2, 4: 2,
    5: 3, 6: 3, 7: 3,
    8: 4, 9: 4, 10: 4,
    11: 5, 12: 5, 13: 5,
    14: 6
}

def get_incoming_edges(v):
    incoming = {}
    for u in graph:
        if v in graph[u]:
            incoming[u] = graph[u][v]
    return incoming

def forward_graph(G, k, n):
    cost = {i: INF for i in range(1, n + 1)}
    d = {i: 0 for i in range(1, n + 1)}
    
    cost[n] = 0.0
    
    for j in range(n - 1, 0, -1):
        if not G[j]:
            continue
            
        min_cost = INF
        min_r = -1
        equations = []
        
        for r, weight in G[j].items():
            current_cost = weight + cost[r]
            equations.append(f"{weight}+{int(cost[r])}")
            if current_cost < min_cost:
                min_cost = current_cost
                min_r = r
                
        cost[j] = min_cost
        d[j] = min_r
        stage = vertex_to_stage[j]
        if len(equations) > 1:
            print(f"Cost(Vertex {j}, Stage {stage}) = min{{{', '.join(equations)}}} = {int(cost[j])}")
        else:
            print(f"Cost(Vertex {j}, Stage {stage}) = {equations[0]} = {int(cost[j])}")
        print(f"d(Vertex {j}, Stage {stage}) = {d[j]}\n")
            
    p = [0] * (k + 1)
    p[1] = 1
    p[k] = n
    for j in range(2, k):
        p[j] = d[p[j - 1]]
        
    path_str = " -> ".join(map(str, p[1:]))
    print(f"Path = {path_str}")
    print(f"Mincost = {int(cost[1])}\n")


def backward_graph(G, k, n):
    bcost = {i: INF for i in range(1, n + 1)}
    d = {i: 0 for i in range(1, n + 1)}
    
    bcost[1] = 0.0
    
    for j in range(2, n + 1):
        incoming = get_incoming_edges(j)
        if not incoming:
            continue 
        min_cost = INF
        min_r = -1
        equations = []
        
        for r, weight in incoming.items():
            if bcost[r] != INF:
                current_cost = bcost[r] + weight
                equations.append(f"{int(bcost[r])}+{weight}")
                if current_cost < min_cost:
                    min_cost = current_cost
                    min_r = r
                    
        bcost[j] = min_cost
        d[j] = min_r
        
        stage = vertex_to_stage[j]
        if len(equations) > 1:
            print(f"Cost(Vertex {j}, Stage {stage}) = min{{{', '.join(equations)}}} = {int(bcost[j])}")
        else:
            print(f"Cost(Vertex {j}, Stage {stage}) = {equations[0]} = {int(bcost[j])}")
        print(f"d(Vertex {j}, Stage {stage}) = {d[j]}\n")
    
    p = [0] * (k + 1)
    p[1] = 1
    p[k] = n
    for j in range(k - 1, 1, -1):
        p[j] = d[p[j + 1]]
        
    path_str = " -> ".join(map(str, p[1:]))
    print(f"Path = {path_str}")
    print(f"Mincost = {int(bcost[n])}")

if __name__ == "__main__":
    forward_graph(graph, k, n)
    backward_graph(graph, k, n)