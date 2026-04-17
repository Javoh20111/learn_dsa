## 6. Longest Increasing Subsequence
""" 
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
Input
The first line contains an integer n (1 <= n <= 5000) — the number of elements in the array.
The second line contains n space-separated integers nums[i] (-10^9 <= nums[i] <= 10^9).
Output
Print a single integer — the length of the longest strictly increasing subsequence.
Sample Input 1:
Copy

8
10 9 2 5 3 7 101 18
Sample Output 1:
Copy

4
One possible longest increasing subsequence is [2, 3, 7, 101], which has length 4. Another valid one is [2, 5, 7, 101].
Copy

Index:  0    1    2    3    4    5    6     7
Value: 10    9    2    5    3    7   101   18

       10    9    2    5    3    7   101   18
                  |         |    |    |
                  2 ------> 3 -> 7 -> 101      LIS length = 4
                  |    |         |
                  2 -> 5 ------> 7 -> 101      LIS length = 4
Sample Input 2:
Copy

6
0 1 0 3 2 3
 """

def squence(n,arr):
    length = [1]*n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                length[i] = max(length[i],length[j]+1)
    print(max(length))

n = int(input())
arr = list(map(int,input().split()))
squence(n,arr)