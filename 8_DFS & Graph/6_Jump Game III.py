## Jump Game III

""" 
Given an array of non-negative integers arr, you are initially positioned at index start of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.

Notice that you can not jump outside of the array at any point.

Input
The first line contains two integers n and start (1 ≤ n ≤ 5 * 10^4, 0 ≤ start < n) — the size of the array and the starting index.

The second line contains n non-negative integers arr[0], arr[1], ..., arr[n-1] (0 ≤ arr[i] < n).

Output
Print true if you can reach any index with value 0, or false otherwise.

Sample Input 1:
7 5
4 2 3 0 3 1 0
Sample Output 1:
true
The jump graph (arrows show possible jumps):

  Index: 0   1   2   3   4   5   6
  Value: 4   2   3  [0]  3   1  [0]

  Path:  5 ---> 4 ---> 1 ---> 3
        (1)    (3)    (2)    (0) FOUND!
Starting at index 5 (value 1), jump to index 4 (value 3), then jump to index 1 (value 2), then jump to index 3 (value 0). We reached an index with value 0.
 """

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def solve():
    ## Take input
    n, start = map(int,input().split())
    arr = list(map(int,input().split()))

    ## make directions
    directions = []
    stack = deque()
    stack.append(start)
    visited = set()

    while stack:
        i = stack.popleft()
        if arr[i] == 0:
            print('true')
            return
        if i in visited:
            continue
        visited.add(i)
        left = i - arr[i]
        right = i + arr[i]
        if 0<=left<n:
            if left not in visited:
                stack.append(left)
        if 0<=right<n:
            if right not in visited:
                stack.append(right)
    print('false')
solve()