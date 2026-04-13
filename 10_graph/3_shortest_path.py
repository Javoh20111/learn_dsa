""" 
You are given a weighted directed graph with N nodes and M edges. Find the shortest distance from node S to node T.

Input
The first line contains two integers N and M (2 ≤ N ≤ 10^5, 0 ≤ M ≤ 2*10^5) — the number of nodes and edges.

The second line contains two integers S and T (1 ≤ S, T ≤ N, S ≠ T) — the source and target nodes.

Each of the next M lines contains three integers u, v, and w (1 ≤ u, v ≤ N, u ≠ v, 1 ≤ w ≤ 10^9) — a directed edge from node u to node v with weight w.

Output
Print a single integer — the shortest distance from S to T. If there is no path from S to T, print -1.

Sample Input 1:
Copy
4 5
1 4
1 2 2
1 3 5
2 3 1
2 4 7
3 4 3
Sample Output 1:
Copy
6
The graph looks like:

Copy
        2         7
   1 -------> 2 -------> 4
   |          |           ^
   |    5     | 1     3   |
   +--------> 3 ---------+
Shortest path: 1 → 2 → 3 → 4 with distance 2 + 1 + 3 = 6.
 """
import heapq
from collections import defaultdict,deque

def solve():
    ## take input
    n,m = map(int,input().split())
    s,t = map(int,input().split())
    graph = defaultdict(list)

    ## make graph 
    for _ in range(m):
        u,v,w = map(int,input().split())
        graph[u].append((v,w))

    ## create a table to track shortes path
    dist = {}
    for i in range(1, n+1):
        dist[i] = float('inf')
    dist[s] = 0

    heap = [(0,s)]
    while heap:
        d, node = heapq.heappop(heap)

        if d>dist[node]:
            continue
        if node==t:
            print(dist[t])
            return
        for neigbor, weight in graph[node]:
            new_dist = dist[node] + weight
            if new_dist < dist[neigbor]:
                dist[neigbor] = new_dist
                heapq.heappush(heap, (new_dist, neigbor))
    print(-1)

solve()