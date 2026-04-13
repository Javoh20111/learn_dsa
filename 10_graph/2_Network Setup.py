## Network Setup
""" 
A company wants to set up a computer network connecting N offices. There are M possible cable connections available, each with an installation cost.

The company wants to connect all offices using the minimum total cable cost. However, not all offices may be connectable.

If it is possible to connect all offices, print two integers: the number of cables used and the total cost. If it is not possible, print -1.

Input
The first line contains two integers N and M (1 ≤ N ≤ 10^5, 0 ≤ M ≤ 2×10^5) — the number of offices and available cable connections.

Each of the next M lines contains three integers u, v, and w (1 ≤ u, v ≤ N, u ≠ v, 1 ≤ w ≤ 10^9) — a possible cable between offices u and v with cost w.

Output
If all offices can be connected, print two space-separated integers — the number of cables used and the total installation cost.

If it is not possible to connect all offices, print -1.

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
3 6
The network looks like:

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
The minimum cost network uses 3 cables: (2,3)=1, (3,4)=2, (1,2)=3. Cables used = 3, total cost = 6.

Sample Input 2:
Copy
4 2
1 2 10
3 4 5
Sample Output 2:
Copy
-1
The network looks like:

Copy
1---10---2     3---5---4
Offices {1,2} and {3,4} are in separate groups. It is impossible to connect all offices.
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