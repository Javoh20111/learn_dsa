## Reachable Nodes with Restrictions

""" 
There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given a 2D integer array edges of length n - 1, where edges[i] = [a_i, b_i] indicates that there is an edge between nodes a_i and b_i in the tree. You are also given an integer array restricted which represents restricted nodes.

Return the number of nodes you can reach from node 0 without visiting a restricted node at any point.

Note that node 0 will not be a restricted node.

Input
The first line contains two integers n and r (2 ≤ n ≤ 10^5, 0 ≤ r ≤ n - 1) — the number of nodes and the number of restricted nodes.

Each of the next n - 1 lines contains two integers a and b (0 ≤ a, b ≤ n - 1) — the endpoints of an edge.

The last line contains r integers — the restricted nodes. If r = 0, this line is empty.

Output
Print a single integer — the number of nodes reachable from node 0 without visiting any restricted node.

Sample Input 1:
Copy
7 1
0 1
1 2
3 1
4 0
0 5
5 6
4
Sample Output 1:
Copy
6
The tree looks like (restricted node marked with X):

Copy
        0
      / | \\
     1 [4]X 5
    / \       \\
   2   3       6
Node 4 is restricted. Starting from node 0, we can reach nodes {0, 1, 2, 3, 5, 6} by traversing edges without visiting node 4. That gives 6 reachable nodes.
 """

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def solve():
    ## take input 
    n, r = map(int,input().split())
    edges = []

    for _ in range(n-1):
        a_i, b_i = map(int,input().split())
        edges.append([a_i, b_i])
    

    restricted = set(map(int,input().split()))

    ## make a graph
    graph = defaultdict(list)
    for a_i, b_i in edges:
        graph[a_i].append(b_i)
        graph[b_i].append(a_i)

    ## create a dfs
    stack = deque()
    stack.append(0)
    visited = set()


    while stack:
        node = stack.pop()
        if node in visited:
            continue
        if node in restricted:
            continue
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
    print(len(visited))

solve()