## Path with Maximum Probability

""" 
You are given an undirected weighted graph with N nodes and M edges. Each edge has a probability of success associated with it.

Given two nodes S and T, find the path from S to T that has the maximum probability of success. The probability of a path is the product of probabilities of all edges along the path.

Input
The first line contains two integers N and M (1 ≤ N ≤ 10^4, 0 ≤ M ≤ 5×10^4) — the number of nodes and edges.

The second line contains two integers S and T (1 ≤ S, T ≤ N, S ≠ T) — the source and target nodes.

Each of the next M lines contains two integers u, v and a real number p (1 ≤ u, v ≤ N, u ≠ v, 0 < p ≤ 1) — an undirected edge between u and v with success probability p. The probability p is given with at most 5 decimal places.

Output
Print the maximum probability of success from S to T, with exactly 5 decimal places. If there is no path, print 0.00000.

Sample Input 1:
3 3
1 3
1 2 0.50000
2 3 0.50000
1 3 0.20000
Sample Output 1:
0.25000
The graph looks like:

       0.5        0.5
  1 --------- 2 --------- 3
  |                        |
  +--------0.2-------------+
Path 1→2→3 has probability 0.5 × 0.5 = 0.25. Path 1→3 has probability 0.2. Maximum probability = 0.25.
 """
import sys
input = sys.stdin.readline
from collections import defaultdict,deque
import heapq

def solve():
    ## take input
    n,m = map(int,input().split())
    s,t = map(int,input().split())
    graph = defaultdict(list)

    ## make graph
    for _ in range(m):
        group = input().split()
        u,v = int(group[0]),int(group[1])
        w = float(group[2])
        graph[u].append((v,w))
        graph[v].append((u,w))

    ## create a dist
    dist = {}
    for i in range(1,n+1):
        dist[i] = 0.00000
    dist[s] = 1.0

    ## create a heap
    heap = [(-1.0, s)]
    while heap:
        prob, node = heapq.heappop(heap)
        prob = -prob

        if prob < dist[node]:
            continue

        if node == t:
            print(f'{dist[t]:.5f}')
            return

        for neighbor, weight in graph[node]:
            new_prob = dist[node] * weight
            if new_prob > dist[neighbor]:
                dist[neighbor] = new_prob
                heapq.heappush(heap, (-new_prob, neighbor))
    print('0.00000')
solve()
