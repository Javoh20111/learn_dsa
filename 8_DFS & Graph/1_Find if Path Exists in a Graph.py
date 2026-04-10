## Find if Path Exists in a Graph

"""
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [u_i, v_i] denotes a bi-directional edge between vertex u_i and vertex v_i. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given n, edges, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

Input
The first line contains two integers n and m (1 ≤ n ≤ 2 * 10^5, 0 ≤ m ≤ 2 * 10^5) — the number of vertices and the number of edges.

Each of the next m lines contains two integers u and v (0 ≤ u, v ≤ n - 1, u ≠ v) — the endpoints of an edge.

The last line contains two integers source and destination (0 ≤ source, destination ≤ n - 1).

Output
Print true if there is a valid path from source to destination, or false otherwise.

Sample Input 1:

3 3
0 1
1 2
2 0
0 2
Sample Output 1:

true
The graph looks like:


    0
   / \
  1---2
There are two paths from vertex 0 to vertex 2: 0 → 1 → 2 and 0 → 2.


"""
from collections import defaultdict
import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    s, d = map(int, input().split())

    if s == d:
        print('true')
        return

    visited = set()
    stack = [s]

    while stack:
        node = stack.pop()
        if node == d:
            print('true')
            return
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

    print('false')

solve()