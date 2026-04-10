## Maximum Subarray Sum (Brute Force)

""" 
Find the maximum sum over all contiguous subarrays using a brute-force approach.

Input
The first line contains an integer n.

The second line contains n integers a[0..n-1].

Output
Print the maximum subarray sum.

Constraints
1 <= n <= 2000
-10^9 <= a[i] <= 10^9
Sample Input 1:
5
1 -2 3 4 -1
Sample Output 1:
7
The best subarray is 3 4 with sum 7.
 """
def sub_sum(n,arr, max_sum):
    for i in range(n):
        cashe = 0
        for j in range(i, n):
            cashe += arr[j]
            max_sum = max(max_sum, cashe)
    return max_sum

n = int(input())
arr = list(map(int, input().split()))
max_sum = -10**10

print(sub_sum(n,arr, max_sum))