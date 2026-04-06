def dfs(start, graph):
    visited = set()

    def explore(node):
        print(f'Visiting node:{node}')
        visited.add(node)

        for neigbor in graph(node):
            


graph = {
    0:[1],
    1:[0,2],
    2:[1]
}
print(f'nodes visited: {''}')