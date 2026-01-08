def bfs(graph, start):
    visited = []
    queue = [start]

    print("BFS Traversal:", end=" ")

    while queue:
        node = queue.pop(0)

        if node not in visited:
            print(node, end=" ")
            visited.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# -------- Input inside the code --------
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

start_node = 'A'

bfs(graph, start_node)
