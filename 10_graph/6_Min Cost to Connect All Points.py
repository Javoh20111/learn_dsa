## Min Cost to Connect All Points

""" 
You are given N points in a 2D plane. The cost to connect two points (x1, y1) and (x2, y2) is the Manhattan distance: |x1 - x2| + |y1 - y2|.

Return the minimum cost to connect all points such that there is a path between every pair of points. A connection between any two points forms a bidirectional edge.

Input
The first line contains an integer N (1 ≤ N ≤ 1000).

Each of the next N lines contains two integers x_i and y_i (-10^6 ≤ x_i, y_i ≤ 10^6) — the coordinates of the i-th point.

Output
Print a single integer — the minimum cost to connect all points.

Sample Input 1:
Copy
5
0 0
2 2
3 10
5 2
7 0
Sample Output 1:
Copy
20
The points and their positions:

Copy
  y
 10|       C(3,10)
   |
   |
   |
  2|  B(2,2)  D(5,2)
  0|A(0,0)        E(7,0)
   +-------------------> x
   0  2  3  5  7
Optimal connections: A-B (cost 4), B-D (cost 3), D-E (cost 4), C-D (cost 10). Minimum total cost = 4 + 3 + 4 + 10 - 1 = 20.

Sample Input 2:
Copy
3
0 0
1 1
1 0
Sample Output 2:
Copy
2
Copy
  y
  1|  B(1,1)
  0|A(0,0) C(1,0)
   +---------> x
   0  1
Connect A-C (cost 1) and C-B (cost 1). Total = 2.
 """

import sys
input = sys.stdin.readline

def solve():
    ## take input 
    n = int(input())
    edges = []
    ## make points
    points = []
    for _ in range(n):
        x,y = map(int,input().split())
        points.append((x,y))

    ## make edges
    for u in range(n):
        for v in range(u + 1, n):
            w = (abs(points[u][0]-points[v][0])+abs(points[u][1]-points[v][1]))
            edges.append((w,u,v))
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
        print(total)
solve()
