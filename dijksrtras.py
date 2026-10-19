def dijkstra(cost_matrix, source):
    n = len(cost_matrix)
    INF = float('inf')

    # Renamed variables for better readability
    visited = [False] * n
    distances = [INF] * n
    parent = [-1] * n

    # Initialization from the source node
    for i in range(n):
        distances[i] = cost_matrix[source][i]
        if cost_matrix[source][i] != INF:
            parent[i] = source

    distances[source] = 0
    visited[source] = True
    parent[source] = -1

    print("--- Dijkstra's Algorithm Execution ---")
    print(f"\nStep 1 : Initialized from Source Vertex {source + 1}")
    print(f"Visited   = {visited}")
    print(f"Parent    = {[x + 1 if x != -1 else -1 for x in parent]}")
    print(f"Distances = {distances}")

    # Main algorithm loop
    for step in range(2, n + 1):
        current_node = -1
        min_dist = INF

        # Find the unvisited vertex with the minimum distance
        for i in range(n):
            if not visited[i] and distances[i] < min_dist:
                min_dist = distances[i]
                current_node = i

        if current_node == -1:
            break  # All reachable vertices have been visited

        visited[current_node] = True

        # Relax adjacent vertices
        for neighbor in range(n):
            weight = cost_matrix[current_node][neighbor]
            if not visited[neighbor] and weight != INF:
                new_distance = distances[current_node] + weight
                if distances[neighbor] > new_distance:
                    distances[neighbor] = new_distance
                    parent[neighbor] = current_node

        print(f"\nStep {step} : Selected Vertex {current_node + 1}")
        print(f"Visited   = {visited}")
        print(f"Parent    = {[x + 1 if x != -1 else -1 for x in parent]}")
        print(f"Distances = {distances}")

    return distances, parent


def display_shortest_paths(distances, parent, source):
    def build_path(destination):
        path = []
        curr = destination
        while curr != -1:
            path.append(curr + 1)
            curr = parent[curr]
        path.reverse()
        return " -> ".join(map(str, path))

    print("\n" + "-" * 55)
    print(f"{'Source':<8}{'Dest':<8}{'Length':<10}{'Path'}")
    print("-" * 55)

    for i in range(len(distances)):
        if i == source:
            continue
            
        dist_val = int(distances[i]) if distances[i] != float('inf') else "INF"
        path_str = build_path(i) if dist_val != "INF" else "Unreachable"
        
        print(f"{source + 1:<8}{i + 1:<8}{dist_val:<10}{path_str}")


if __name__ == "__main__":
    INF = float('inf')
    cost_matrix = [
        [0,   35, 25, 20, 31, 28, INF, 20],
        [INF, 0,  30, INF, 15, 35, INF, INF],
        [33,  27, 0,  24, 23, 21, 17, 12],
        [27,  10, 20, 0,  INF, INF, 26, INF],
        [INF, 13, INF, 18, 0,  INF, 17, 21],
        [30,  32, INF, 31, INF, 0,  20, INF],
        [19,  INF, INF, 35, 17, 15, 0,  INF],
        [INF, INF, 35, 29, 30, INF, INF, 0]
    ]
    
    source_vertex = 0
    final_distances, parents = dijkstra(cost_matrix, source_vertex)
    display_shortest_paths(final_distances, parents, source_vertex)