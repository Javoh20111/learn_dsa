"""
You are given an undirected weighted graph with N nodes and M edges. Find the shortest distance from node 1 to node N.

Input
The first line contains two integers N and M (2 ≤ N ≤ 10^5, 0 ≤ M ≤ 2×10^5) — the number of nodes and edges.

Each of the next M lines contains three integers u, v, and w (1 ≤ u, v ≤ N, u ≠ v, 1 ≤ w ≤ 10^9) — an undirected edge between nodes u and v with weight w.

Output
Print a single integer — the shortest distance from node 1 to node N. If there is no path, print -1.

Sample Input 1:
5 6
1 2 2
1 3 4
2 3 1
2 4 7
3 5 3
4 5 1
Sample Output 1:
6
The graph looks like:

        2         7
   1 ------- 2 ------- 4
   |         |          |
   |   4     | 1     1  |
   +-------- 3     +----+
              |     |
              +--3--5
Paths from 1 to 5:

1→3→5: 4 + 3 = 7
1→2→4→5: 2 + 7 + 1 = 10
1→2→3→5: 2 + 1 + 3 = 6 Shortest distance = 6.
 """
import heapq
from collections import deque,defaultdict
def solve():
    ## Take input
    n,m = map(int,input().split())
    graph = defaultdict(list)
    ## Make undirected graph
    for _ in range(m):
        u,v,w = map(int,input().split())
        graph[u].append((v,w))
        graph[v].append((u,w))
    ## maybe use Dajkister algorith
    dist = dict()
    for i in range(1,n+1):
        dist[i] = float('inf') ## create a table with inf values 
    dist[1] = 0 ## -->first node costs 0

    heap = [(0,1)] ## --> distance and node position
    while heap:
        distance, node = heapq.heappop(heap)

        if distance > dist[node]:
            continue

        if node == n:
            print(dist[n])
            return
        for neigbor, weight in graph[node]:
            new_des = dist[node] + weight
            if new_des < dist[neigbor]:
                dist[neigbor] = new_des
                heapq.heappush(heap, (new_des, neigbor))
    print(-1)
    ## Give a note whereas we can learn it or not
    ## Yes we can learn it. It is very similar to week 8 problems. Like finding shortest path with directions
solve()