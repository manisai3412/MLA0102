def dfs(graph, start):
    visited = []
    stack = [start]

    print("DFS Traversal:", end=" ")

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node, end=" ")
            visited.append(node)

            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# -------- Input inside the code --------
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

start_node = 'A'

dfs(graph, start_node)
