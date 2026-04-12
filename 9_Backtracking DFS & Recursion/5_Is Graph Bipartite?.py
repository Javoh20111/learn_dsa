## Is Graph Bipartite?

""" 
There is an undirected graph with n nodes, where each node is numbered between 0 and n-1. You are given a list of edges.

The graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Determine whether the graph is bipartite.

Input
The first line contains two integers n and m (1 ≤ n ≤ 100, 0 ≤ m ≤ 500) — the number of nodes and edges.

Each of the next m lines contains two integers u and v (0 ≤ u, v < n) — an undirected edge between u and v.

Output
Print YES if the graph is bipartite, otherwise print NO.

Sample Input 1:
Copy
4 4
0 1
1 2
2 3
3 0
Sample Output 1:
Copy
YES
Graph (a 4-node cycle):

Copy
0 — 1
|   |
3 — 2
This is bipartite: set A = {0, 2}, set B = {1, 3}. Every edge connects a node in A to a node in B.

Sample Input 2:
Copy
3 3
0 1
1 2
2 0
Sample Output 2:
Copy
NO
Graph (a triangle):

Copy
    0
   / \\
  1 — 2
 """

from collections import defaultdict,deque
def solve():
    ## take input
    n,m = map(int,input().split())
    graph = defaultdict(list)

    ## make a graph
    for _ in range(m):
        u, v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    color = {}
    ## create bfs
    for s in range(n):
        if s in color:
            continue

        stack = deque()
        stack.append(s)
        color[s] = 0

        while stack:
            node = stack.popleft()
            for neigbor in graph[node]:
                if neigbor not in color:
                    color[neigbor] = 1-color[node]
                    stack.append(neigbor)
                elif color[neigbor] == color[node]:
                    print('NO')
                    return
    print('YES') 


solve()