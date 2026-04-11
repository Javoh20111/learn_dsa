## Max Area of Island

""" 
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Input
The first line contains two integers m and n (1 ≤ m, n ≤ 50) — the number of rows and columns.

Each of the next m lines contains n integers, each either 0 or 1, separated by spaces.

Output
Print a single integer — the maximum area of an island.

Sample Input 1:
Copy
4 5
0 0 1 0 0
0 0 0 0 0
0 1 1 0 1
0 0 1 0 1
Sample Output 1:
Copy
3
The grid visualization (land cells marked with #, water with .):

Copy
  . . # . .
  . . . . .
  . # # . #
  . . # . #
The largest island has cells at positions (2,1), (2,2), and (3,2), forming an L-shape with area 3. The two # cells in column 4 form a separate island of area 2.


 """

from collections import defaultdict,deque
import sys
input = sys.stdin.readline

def solve():
  ## Take input
  n,m = map(int, input().split())
  grid = list()

  for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
  
  ## make direction
  directions = [(0,1),(0,-1),(1,0),(-1,0)]
  visited = set()
  stack = deque()
  maxi = 0



  ## make dfs
  def dfs(new_row, new_col):
    nonlocal maxi
    stack.append((new_row, new_col))
    count = 0
    while stack:
      row, col = stack.pop()
      if (row, col) in visited:
        continue
      visited.add((row, col))
      count+=1
      for dr,dc in directions:
        new_row = dr+row
        new_col = dc+col
        if 0<=new_row<n and 0<=new_col<m:
          if grid[new_row][new_col] == 1:
            if (new_row,new_col) not in visited:
              stack.append((new_row,new_col))
    maxi = max(maxi, count)

  
  ## make a loop to check all nodes
  for row in range(n):
    for col in range(m):
      if grid[row][col] == 1 and (row,col) not in visited:
        dfs(row,col)
  print(maxi)
solve()