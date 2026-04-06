""" def dfs(start, graph):
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

print(f'nodes visited: {dfs(0, graph)}') """


def count_components(graph):
    """Count how many connected components are in the graph"""
    
    visited = set()  # Track visited nodes
    components = 0   # Count of components
    
    def dfs(node):
        """Explore one complete component"""
        visited.add(node)
        print(f"  Visiting: {node}")
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
    
    # Check each node
    for node in graph:
        if node not in visited:
            print(f"\nFound new component! Starting DFS from {node}")
            dfs(node)
            components += 1
            print(f"Visited so far: {visited}")
    
    return components
# Example
graph = {
    0: [1],
    1: [0],
    2: [3],
    3: [2, 4],
    4: [3]
}

result = count_components(graph)
print(f"\n\nTotal components: {result}")