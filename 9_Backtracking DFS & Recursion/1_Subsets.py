""" 
Given an array of n distinct integers nums, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Print the subsets in order of size, then lexicographically.

Input
The first line contains an integer n (1 ≤ n ≤ 10) — the number of elements.

The second line contains n distinct integers nums[i] (-10 ≤ nums[i] ≤ 10), separated by spaces.

Output
Print all subsets, one per line, with elements separated by spaces. Print an empty line for the empty subset. Output subsets ordered first by size (smallest first), then lexicographically within the same size.

Sample Input 1:
3
1 2 3
Sample Output 1:

1
2
3
1 2
1 3
2 3
1 2 3
There are 2^3 = 8 subsets of [1, 2, 3]. The empty set is printed as a blank line first, then size-1 subsets, then size-2 subsets, then the full set.

Tree visualization of the backtracking:

start=[]
├── [1]
│   ├── [1,2]
│   │   └── [1,2,3]
│   └── [1,3]
├── [2]
│   └── [2,3]
└── [3]
 """
import sys
input = sys.stdin.readline

def solve():
    ## Take input
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    ## create a list for storing subsets
    subsets = []

    ## implement backtracking
    def bactracking(start, path):
        subsets.append(path[:])
        for i in range(start, n):
            path.append(arr[i])
            bactracking(i+1, path)
            path.pop()
    bactracking(0, [])

    ## Sort the result by length
    subsets.sort()
    subsets.sort(key=len)

    for s in subsets:
        print(*s)
solve()