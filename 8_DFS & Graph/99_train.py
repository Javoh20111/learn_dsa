""" def dfs(start, graph):
    visited = set()

    def explore(node):
        print(f'Visiting node:{node}')
        visited.add(node)

        for neigbor in graph[node]:
            if neigbor not in visited:
                explore(neigbor)

    explore(start)
    return visited



graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

print(f'nodes visited: {dfs(0, graph)}') """


from collections import defaultdict,deque
import sys
input = sys.stdin.readline

def solve():
    ## take input
    n, m = map(int, input().split())
    ## make a graph
    graph = defaultdict(list)
    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    r = int(input())
    ## make dfs and variables to track
    stack = deque()
    visited = set()

    stack.append((0,0))

    while stack:
        node,count = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        if node == r:
            continue
        for neigbor in graph[node]:
            if neigbor not in visited:
                stack.append((visited, count + 1))
    print(count)
solve()