## Sum of Array by Index

""" 
You are given an array and an index k. Compute the sum of elements from index 0 through k (inclusive).

Input
The first line contains two integers n and k.

The second line contains n integers a[0..n-1].

Output
Print the sum a[0] + a[1] + ... + a[k].

Constraints
1 <= n <= 10^5
-10^9 <= a[i] <= 10^9
0 <= k < n
Notes
Recursion is encouraged and will not be penalized by the judge.
Sample Input 1:
Copy
5 2
1 2 3 4 5
Sample Output 1:
Copy
6
The sum is 1 + 2 + 3 = 6.
 """
import sys
sys.setrecursionlimit(200000)
def sum_of_arr(n, k, s, arr):
    if s > k:
        return 0 
    return arr[s] + sum_of_arr(n, k, s+1, arr)

n, k = map(int, input().split())
s = 0
arr = list(map(int, input().split()))
print(sum_of_arr(n, k, s, arr))