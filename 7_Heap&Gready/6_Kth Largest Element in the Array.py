"""
Given an integer array and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Input
The first line contains two integers n and k (1 ≤ k ≤ n ≤ 10^5).

The second line contains n integers nums[i] (-10^4 ≤ nums[i] ≤ 10^4).

Output
Print a single integer — the kth largest element.

Sample Input 1:
6 2
3 2 1 5 6 4
Sample Output 1:
5
Sorted in descending order: [6, 5, 4, 3, 2, 1]. The 2nd largest is 5.
"""
from heapq import heapify, heappop, nlargest
n,k = map(int, input().split())
arr = list(map(int, input().split()))
heapify(arr)

print(nlargest(k, arr)[-1])

