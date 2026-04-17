'''from collections import deque,defaultdict
## take input
def solve():
    n, m = map(int,input().split())
    edges = []
    for _ in range(m):
        u,v,w = map(int,input().split())
        edges.append((u,v,w))
    edges.sort()

    parent = list(range(n+1))
    rank = [0] * (n+1)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x,y):
        px,py = find(x),find(y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px,py = py,px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px]+=1
        return True

    total_weight = 0
    used_edges = 0
    for u,v,w in edges:
        if union(u,v):
            total_weight+=w
            used_edges+=1
            if used_edges == n-1:
                break
    print(total_weight)
solve()
'''

