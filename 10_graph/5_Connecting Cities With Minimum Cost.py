## Connecting Cities With Minimum Cost

"""

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