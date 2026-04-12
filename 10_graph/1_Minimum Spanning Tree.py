""" 
You are given a connected undirected weighted graph with N nodes and M edges. Find the total weight of the Minimum Spanning Tree (MST) of the graph.

A Minimum Spanning Tree is a subset of edges that connects all nodes with the minimum possible total edge weight, without forming any cycle.

Input
The first line contains two integers N and M (2 ≤ N ≤ 10^5, N-1 ≤ M ≤ 2×10^5) — the number of nodes and edges.

Each of the next M lines contains three integers u, v, and w (1 ≤ u, v ≤ N, u ≠ v, 1 ≤ w ≤ 10^9) — an undirected edge between nodes u and v with weight w.

Output
Print a single integer — the total weight of the Minimum Spanning Tree.

Sample Input 1:
Copy
4 5
1 2 3
1 3 5
2 3 1
2 4 4
3 4 2
Sample Output 1:
Copy
6
The graph looks like:

Copy
    1
   / \\
  3   5
 /     \\
2---1---3
 \     /
  4   2
   \ /
    4
The MST picks edges (2,3) with weight 1, (3,4) with weight 2, and (1,2) with weight 3. Total MST weight = 1 + 2 + 3 = 6.
 """
from collections import defaultdict
def solve()
    ## take input
    n,m = map(int, input().split())
    graph = defaultdict(list)

    for _ in range():
        u,v,w = map(int, input().split())
        graph[u].append((v,w))
        graph[v].append((u,w))

    
solve()