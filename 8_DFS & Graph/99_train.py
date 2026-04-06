def dfs(start, graph):
    visited = set()

    def explore(node):
        print(f'Visiting node:{node}')
        visited.add(node)

        for neigbor in graph[node]:
            if neigbor not in visited:
                explore(neigbor)

    explore(start)
    return visited



graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

print(f'nodes visited: {dfs(0, graph)}')