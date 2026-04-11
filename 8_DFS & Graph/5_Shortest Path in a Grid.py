## Shortest Path in a Grid

""" 
You are given an m x n grid where each cell is either 0 (empty) or 1 (wall). You start at the top-left cell (0, 0) and want to reach the bottom-right cell (m - 1, n - 1).

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the grid.

Return the minimum number of steps to reach the bottom-right cell from the top-left cell, or -1 if no such path exists. The starting and ending cells are guaranteed to be empty.

Input
The first line contains two integers m and n (1 ≤ m, n ≤ 500) — the number of rows and columns.

Each of the next m lines contains n integers, each either 0 or 1, separated by spaces.

Output
Print a single integer — the minimum number of steps to reach (m - 1, n - 1) from (0, 0), or -1 if impossible.

Sample Input 1:
3 3
0 0 0
0 1 0
0 0 0
Sample Output 1:
4
The grid visualization (. = empty, # = wall, S = start, E = end):

  S . .
  . # .
  . . E
The shortest path goes around the wall: (0,0) → (0,1) → (0,2) → (1,2) → (2,2), taking 4 steps.
 """

from collections import defaultdict,deque
import sys
input = sys.stdin.readline

def solve():
    ## take input
    m,n = map(int,input().split())
    grid = list()

    ## make a grid
    for row in range(m):
        row = list(map(int,input().split()))
        grid.append(row)

    finish = (m-1, n-1)

    ## Make a destinations
    destinations = [(0,1),(0,-1),(1,0),(-1,0)]
    visited = set()
    stack = deque()
    count = 0

    ## Make bfs
    stack.append((0,0,0))
    while stack:
        row,col,steps = stack.popleft()
        if (row, col) == (m-1,n-1):
            print(steps)
            return
        if (row, col) in visited:
            continue

        if grid[row][col] == 1:
            continue
        visited.add((row,col))

        for dr, dc in destinations:
            new_row = dr+row
            new_col = dc+col
            if 0 <= new_row<m and 0<=new_col<n:
                if (new_row,new_col) not in visited:
                    stack.append((new_row,new_col, steps+1))
    print(-1)
solve()


