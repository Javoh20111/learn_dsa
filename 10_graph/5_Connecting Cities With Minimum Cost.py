## Connecting Cities With Minimum Cost

"""
There are N cities labeled from 1 to N. You are given a list of M connections, where each connection specifies two cities and the cost to connect them with a bidirectional road.

Return the minimum cost to connect all cities such that there is a path between every pair of cities. If it is not possible to connect all cities, return -1.

Input
The first line contains two integers N and M (1 ≤ N ≤ 10^4, 0 ≤ M ≤ 10^5) — the number of cities and connections.

Each of the next M lines contains three integers u, v, and w (1 ≤ u, v ≤ N, u ≠ v, 1 ≤ w ≤ 10^6) — a possible road between cities u and v with cost w.

Output
Print a single integer — the minimum cost to connect all cities, or -1 if it is impossible.

Sample Input 1:
4 5
1 2 3
1 3 5
2 3 1
2 4 4
3 4 2
Sample Output 1:
6
The graph looks like:

    1
   / \\
  3   5
 /     \\
2---1---3
 \     /
  4   2
   \ /
    4
Connect cities with edges (2,3)=1, (3,4)=2, (1,2)=3. Total cost = 6.

Sample Input 2:
4 2
1 2 5
3 4 8
Sample Output 2:
-1
The graph looks like:

1---5---2     3---8---4
Cities {1,2} and {3,4} are in separate components. Cannot connect all cities.
"""

import sys
input = sys.stdin.readline

def solve():
    ## Take input
    n,m = map(int,input().split())
    edges = []

    for _ in range(m):
        u,v,w = map(int,input().split())
        edges.append((w,v,u))
    edges.sort()
    ## root finder
    parent = list(range(n+1))
    rank = [0] * (n+1)
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    ## connector
    def union(x,y):
        px,py = find(x),find(y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px,py=py,px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px]+=1
        return True

    ## Step 1 Make a loop to count and check availablity
    total = 0
    total_edges = 0
    for w,u,v in edges:
        if union(u,v):
            total+=w
            total_edges += 1
        if total_edges == n-1:
            break
    if total_edges != n-1:
        print(-1)
    else:
        print(total_edges,total)
solve()