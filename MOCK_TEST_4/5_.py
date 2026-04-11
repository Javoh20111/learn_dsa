""" 
Given an n x n binary matrix, find the length of the shortest clear path from the top-left cell (0, 0) to the bottom-right cell (n-1, n-1).

A clear path visits only cells containing 0 and moves 8-directionally (horizontally, vertically, or diagonally to any adjacent cell). The length of the path is the number of cells visited, including start and end.

If no clear path exists, return -1.

Input
The first line contains an integer n (1 ≤ n ≤ 100).

Each of the next n lines contains n space-separated integers, each 0 or 1.

Output
Print a single integer — the length of the shortest clear path, or -1 if none exists.

Subtasks:

Subtask 1 (5 points): n ≤ 5
Subtask 2 (5 points): n ≤ 20
Subtask 3 (5 points): n ≤ 100
Sample Input 1:
Copy
3
0 0 0
1 1 0
1 1 0
Sample Output 1:
Copy
4
The grid (. = open, # = blocked):

Copy
. . .
# # .
# # .
The shortest path visits 4 cells:

Copy
S . .
# # .
# # E   S=(0,0), E=(2,2)
Path: (0,0) → (0,1) → (0,2) → (1,2) → (2,2) — 4 cells visited (note: the diagonal step from (1,2) to (2,2) counts as one move).

Sample Input 2:
Copy
3
0 1 0
1 1 0
1 1 0
Sample Output 2:
Copy
-1
The grid:

Copy
S # .
# # .
# # E
From (0,0), all 8 neighbours are either blocked (#) or out of bounds. There is no path to (2,2).

Sample Input 3:
Copy
1
0
Sample Output 3:
Copy
1
The grid has a single cell which is both start and end. The path length is 1.

Source
This problem is based on LeetCode 1091: Shortest Path in Binary Matrix.
 """

from collections import deque
import sys
input = sys.stdin.readline

def solve():
    ## take input
    n = int(input())
    grid = list()

    # make grid
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)

    ## make directions
    directions = [(0,1),
                  (0,-1),
                  (1,0),
                  (-1,0),
                  (-1,-1),
                  (-1,1),
                  (1,-1),
                  (1,1)]
    stack = deque()
    visited = set()
    ## make bfs
    stack.append((0,0,1))
    while stack:
        row, col, step = stack.popleft()
        if (row,col) in visited:
            continue
        if grid[row][col] == 1:
            continue
        visited.add((row,col))
        if row == n-1 and col == n-1:
            print(step)
            return
        for dr,dc in directions:
            new_row = dr + row
            new_col = dc + col
            if 0<=new_row<n and 0<=new_col<n:
                if (new_row, new_col) not in visited:
                    stack.append((new_row, new_col, step+1))
    print(-1)
solve()