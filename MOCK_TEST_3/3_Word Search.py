""" Given an m x n grid of characters and a string word, return whether the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same cell may not be used more than once.

Input
The first line contains two integers m and n (1 <= m, n <= 200) --- the dimensions of the board.

The next m lines each contain n space-separated lowercase English letters --- the board.

The last line contains a string word (1 <= |word| <= 15) consisting of lowercase English letters.

Subtasks:

Subtask 1 (7 points): m, n <= 6, |word| <= 5
Subtask 2 (8 points): m, n <= 50, |word| <= 10
Subtask 3 (10 points): m, n <= 200, |word| <= 15
Output
Print true if the word exists in the grid, otherwise print false.

Sample Input 1:
Copy
3 4
a b c e
s f c s
a d e e
abcced
Sample Output 1:
Copy
true
The path is: a(0,0) -> b(0,1) -> c(0,2) -> c(1,2) -> e(2,2) -> d(2,1). Each step moves to an adjacent cell and no cell is reused.

 """

def solve():
    ## Take input
    m,n = map(int,input().split())
    grid = []
    for _ in range(n):
        row = list(map(str,input().split()))
        grid.append(row)

    directions = 
solve()