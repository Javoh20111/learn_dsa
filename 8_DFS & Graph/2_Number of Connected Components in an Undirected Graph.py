## Number of Connected Components in an Undirected Graph

""" 
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [a_i, b_i] indicates that there is an undirected edge between nodes a_i and b_i in the graph.

Return the number of connected components in the graph.

Input
The first line contains two integers n and m (1 ≤ n ≤ 2 * 10^5, 0 ≤ m ≤ 2 * 10^5) — the number of nodes (labeled from 0 to n - 1) and the number of edges.

Each of the next m lines contains two integers a and b (0 ≤ a, b ≤ n - 1, a ≠ b) — the endpoints of an edge.

Output
Print a single integer — the number of connected components in the graph.

Sample Input 1:
5 3
0 1
1 2
3 4
Sample Output 1:
2
The graph looks like:

  Component 1:     Component 2:
  0---1---2        3---4
There are two connected components: {0, 1, 2} and {3, 4}.
"""



n, m = map(int, input().split())

edges = []
for _ in range(m):
    a, b = map(int, input().split())
    edges.append([a, b])
def count_components(n, edges):
    graph = {}
    for i in range(n):
        graph[i] = []
    
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    visited = set()
    
    def dfs(node):
        """Explore all nodes in one component"""
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    components = 0
    for node in range(n):
        if node not in visited:
            dfs(node)
            components += 1
    
    return components
result = count_components(n, edges)
print(result)