## 	Next Greater Element I

"""
You are given two integer arrays nums1 and nums2 where:
    all elements in both arrays are distinct
    nums1 is a subset of nums2
For each value in nums1, find its next greater element in nums2:
    locate that value in nums2
    scan to the right until you find a strictly larger value
    if none exists, answer is -1
Input
    First line: two integers n and m
    Second line: n distinct integers for nums1
    Third line: m distinct integers for nums2
    Constraints:

1 <= n <= m <= 2 * 10^5
-10^9 <= nums1[i], nums2[i] <= 10^9
nums1 is a subset of nums2
Output
Print n integers where the i-th value is the next greater element of nums1[i] in nums2.

Sample Input 1:
2 4
4 1
1 3 4 2
Sample Output 1:
-1 3
"""
from collections import deque

n, m = map(int, input().split())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

nums1idx = {n:i for i,n in enumerate(nums1)}
res = [-1] * n

for i in range(m):
    if nums2[i] not in nums1idx:
        continue
    for j in range(i+1, m): 
        if nums2[j] > nums2[i]:
            indx = nums1idx[nums2[i]]
            res[indx] = nums2[j]
            break
print(*res)