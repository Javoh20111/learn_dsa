""" 
You are given an m x n matrix maze (indexed starting at [0, 0]) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrance_row, entrance_col] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

Input
The first line contains two integers m and n (1 ≤ m, n ≤ 100) — the number of rows and columns.

Each of the next m lines contains n characters, each either '.' or '+', separated by spaces.

The last line contains two integers entrance_row and entrance_col (0 ≤ entrance_row < m, 0 ≤ entrance_col < n) — the position of the entrance. The entranceSolved cell is guaranteed to be empty.

Output
Print a single integer — the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

Sample Input 1:
Copy
3 4
+ . + .
. . . .
+ + . +
1 0
Sample Output 1:
Copy
2
 """

from collections import defaultdict,deque
import sys
input = sys.stdin.readline

def solve():
    ## take input
    m,n = map(int, input().split())
    grid = list()

    ## make grid
    for _ in range(m):
        row = input().split()
        grid.append(row)
    
    e_r, e_c = map(int, input().split())

    ## def directions
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    stack = deque()
    visited = set()
    step = 0

    stack.append((e_r, e_c, step))

    ## make bfs
    while stack:
        row, col, step = stack.popleft()
        if (row,col) in visited:
            continue
        if grid[row][col] == '+':
            continue
        visited.add((row,col))
        if (grid[row][col] == '.' and (row == 0 or row == m-1 or col == 0 or col == n-1) and (row != e_r or col != e_c)):
            print(step)
            return
        for dr, ds in directions:
            new_row = row + dr
            new_col = col + ds
            if 0 <= new_row < m and 0 <= new_col < n:
                if (new_row,new_col) not in visited:
                    stack.append((new_row,new_col,step+1))
    print(-1)
solve()