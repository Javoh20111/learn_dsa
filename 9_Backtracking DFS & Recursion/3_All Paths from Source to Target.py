## All Paths from Source to Target

"""
Given a directed acyclic graph (DAG) with n nodes labeled from 0 to n-1, find all possible paths from node 0 to node n-1.

Return all paths in any order.

Input
The first line contains an integer n (2 ≤ n ≤ 15) — the number of nodes.

Each of the next n-1 lines describes the adjacency list of node i (for i = 0, 1, ..., n-2): a space-separated list of nodes that i has directed edges to. Node n-1 is the target and has no outgoing edges, so its adjacency list is not given.

Output
Print all paths from node 0 to node n-1, one path per line. Each path is a sequence of node indices separated by spaces. Print the paths in lexicographic order.

Sample Input 1:
Copy
4
1 2
3
3
Sample Output 1:
Copy
0 1 3
0 2 3
"""

def solve():
    ## take input
    n = int(input())

    ## make graph
    graph=list()
    for i in range(n-1):
        line = list(map(int,input().split()))
        graph.append(line)
    graph.append([])

    res = []

    ## define backtracking
    def bkt(node, path):
        if node == n-1:
            res.append(path[:])
            return
        for neighbor in graph[node]:
            path.append(neighbor)
            bkt(neighbor, path)
            path.pop()
    bkt(0,[0])

    ## print subsets
    res.sort()
    for path in res:
        print(*path)
solve()

