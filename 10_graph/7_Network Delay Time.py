## Network Delay Time

""" 
There are N network nodes labeled from 1 to N. You are given a list of M directed weighted edges representing travel times, and a starting node K.

A signal is sent from node K. Determine the minimum time it takes for all N nodes to receive the signal. If it is impossible for all nodes to receive the signal, return -1.

Input
The first line contains three integers N, M, and K (1 ≤ N ≤ 10^4, 0 ≤ M ≤ 5×10^4, 1 ≤ K ≤ N) — the number of nodes, edges, and the source node.

Each of the next M lines contains three integers u, v, and w (1 ≤ u, v ≤ N, u ≠ v, 1 ≤ w ≤ 100) — a directed edge from u to v with travel time w.

Output
Print a single integer — the minimum time for all nodes to receive the signal, or -1 if not all nodes can be reached.

Sample Input 1:
Copy
4 5 1
1 2 1
1 3 4
2 3 2
2 4 6
3 4 3
Sample Output 1:
Copy
6
The graph looks like:

Copy
          1        6
   1 ---------> 2 ---------> 4
   |            |             ^
   |    4       | 2       3   |
   +----------> 3 -----------+
From node 1: dist[1]=0, dist[2]=1, dist[3]=3 (via 1→2→3), dist[4]=6 (via 1→2→3→4). Maximum distance = 6.

Sample Input 2:
Copy
3 2 1
1 2 5
1 3 10
Sample Output 2:
Copy
10
The graph looks like:

Copy
       5         10
  1 -------> 2   1 -------> 3
From node 1: dist[2]=5, dist[3]=10. Maximum = 10.


 """

import sys
from collections import defaultdict,deque
import heapq
input = sys.stdin.readline

def solve():
    ## Take input
    n,m,k = map(int,input().split())
    graph = defaultdict(list)

    ## make a edges
    for _ in range(m):
        u,v,w = map(int,input().split())
        graph[u].append((v,w))
    ## step 2
    dist = {}
    for i in range(1, n+1):
        dist[i] = float('inf')
    dist[k] = 0
    ## make a heap
    heap = [(0,k)]
    while heap:
        distination, node = heapq.heappop(heap)
        if distination > dist[node]:
            continue
        for neigbor, weight in graph[node]:
            new_dist = dist[node] + weight
            if new_dist < dist[neigbor]:
                dist[neigbor] = new_dist
                heapq.heappush(heap, (new_dist, neigbor))
    max_dist = max(dist.values())

    if max_dist == float('inf'):
        print(-1)
    else:
        print(max_dist)
solve()