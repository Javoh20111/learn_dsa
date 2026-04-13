""" 
There are n cities (labeled 0 to n-1) connected by directed flights, each with a price. Find the cheapest price to travel from city src to city dst using at most k stops.

A stop is an intermediate city. At most k stops means at most k+1 flights.

If no such route exists, return -1.

Input
The first line contains five integers: n m src dst k

n (2 ≤ n ≤ 100) — number of cities
m (1 ≤ m ≤ 500) — number of flights
src — source city
dst — destination city
k (0 ≤ k ≤ n-2) — maximum stops allowed
The next m lines each contain three integers u v w — a flight from city u to city v costing w (1 ≤ w ≤ 10^4).

Output
Print a single integer — the minimum cost, or -1 if no valid route exists.

Subtasks:

Subtask 1 (7 points): n ≤ 10, m ≤ 20, k ≤ 5
Subtask 2 (8 points): n ≤ 30, m ≤ 100
Subtask 3 (10 points): n ≤ 100, m ≤ 500
Sample Input 1:
Copy
4 5 0 3 1
0 1 100
1 2 100
2 0 100
1 3 600
0 3 700
Sample Output 1:
Copy
700
The flight network:

Copy
        100        600
   0 -------> 1 -------> 3
   |           |          ^
   |    100    v    100   |
   +---------> 2 ---------+
   |                      |
   +------- 700 ----------+
With at most 1 stop, two routes reach city 3:

0 → 3 (direct, 0 stops): cost 700
0 → 1 → 3 (1 stop): cost 100 + 600 = 700
Both cost 700; the answer is 700.

Sample Input 2:
Copy
3 3 0 2 1
0 1 100
1 2 100
0 2 500
Sample Output 2:
Copy
200
The flight network:

Copy
        100        100
   0 -------> 1 -------> 2
   |                     ^
   +-------- 500 --------+
With at most 1 stop:

0 → 2 (direct, 0 stops): cost 500
0 → 1 → 2 (1 stop): cost 100 + 100 = 200 ← cheaper
Sample Input 3:
Copy
3 3 0 2 0
0 1 100
1 2 100
0 2 500
Sample Output 3:
Copy
500
With 0 stops, only direct flights are allowed. The only direct flight from 0 to 2 costs 500. The route 0 → 1 → 2 requires 1 stop and is not permitted.

Source
This problem is based on LeetCode 787: Cheapest Flights Within K Stops.


 """
import heapq
from collections import defaultdict,deque
def solve():
    ## take input
    n,m,src,dst,k = map(int,input().split())
    ## make a graph
    edges = []
    for _ in range(m):
        u,v,w = map(int,input().split())
        edges.append((u,v,w))

    dist = {}
    for i in range(n):
        dist[i] = float('inf')
    dist[src] = 0

    ##Bellman-Ford algorithm
    for _ in range(k+1):
        temp = dist.copy()
        for u,v,w in edges:
            if dist[u] != float('inf'):
                temp[v] = min(temp[v], dist[u]+ w)
        dist = temp  


    if dist[dst] == float('inf'):
        print(-1)
    else:
        print(dist[dst])
solve()