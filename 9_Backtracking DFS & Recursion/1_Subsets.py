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

def generate_subsets(arr):
    res = []
    arr.sort()
    def backtrack(start, current):
        res.append(current[:])
        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i + 1, current)
            current.pop()
    backtrack(0, [])
    res.sort(key=lambda x: (len(x), x))
    return res
 
 
n = int(input())
arr = list(map(int, input().split()))
 
subsets = generate_subsets(arr)
for subset in subsets:
    print(' '.join(map(str, subset)))
