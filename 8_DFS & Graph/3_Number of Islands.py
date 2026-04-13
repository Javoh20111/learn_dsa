""" 
Given an m x n 2D binary grid grid which represents a map of 1's (land) and 0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent land cells horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

Input
The first line contains two integers m and n (1 ≤ m, n ≤ 300) — the number of rows and columns.

Each of the next m lines contains n integers, each either 0 or 1, separated by spaces.

Output
Print a single integer — the number of islands.

Sample Input 1:
Copy
4 5
1 1 1 1 0
1 1 0 1 0
1 1 0 0 0
0 0 0 0 0
Sample Output 1:
Copy
1
The grid visualization (land #, water .):

Copy
  # # # # .
  # # . # .
  # # . . .
  . . . . .
All land cells are connected into a single island.
 """

from collections import defaultdict,deque
import sys
input = sys.stdin.readline

def solve():
    ## Take input
    m,n = map(int, input().split())
    grid = []

    ## create a grid
    for _ in range(m):
        row = list(map(int,input().split()))
        grid.append(row)

    ## add directions
    visited = set()
    stack = deque()
    directions = [(0,1),(0,-1),(1,0),(-1,0)]

    ## Create dfs
    def dfs(start_row, start_col):
        stack.append((start_row, start_col))
        while stack:
            row, col = stack.pop()
            if (row,col) in visited:
                continue
            visited.add((row, col))
            for dr,dc in directions:
                new_row = row+dr
                new_col = col+dc
                if 0 <=new_row < m and 0 <= new_col < n:
                    if grid[new_row][new_col] == 1:
                        if (new_row,new_col) not in visited:
                            stack.append((new_row,new_col))

    ## make a loop to find islands
    count = 0
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 1 and (row, col) not in visited:
                dfs(row,col)
                count+=1
    print(count)

solve()


