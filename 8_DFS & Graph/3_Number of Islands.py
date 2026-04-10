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