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

import sys
input = sys.stdin.readline

def solve():
    ## take itput 1 step
    n,m = map(int,input().split())
    edges = []

    for _ in range(m):
        u,v,w = map(int,input().split())
        edges.append((w,u,v))
    edges.sort()

    ## Step 4 find root
    parent = list(range(n+1))
    rank = [0]*(n+1)
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x,y):
        px, py = find(x),find(y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px]+=1
        return True

    ## step-2
    total = 0
    max_edges = 0

    for w, u, v in edges:
        if union(u,v):
            total += w
            max_edges += 1
        if max_edges == n-1:
            break
    print(total)
solve()