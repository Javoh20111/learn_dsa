## Running Sum of 1d Array

""" 
Given an integer array, compute its running sum where each element is the sum of all elements up to that index.

Input
The first line contains an integer n (1 <= n <= 1000).

The second line contains n integers a_1, a_2, ..., a_n (-10^6 <= a_i <= 10^6).

Output
Print the running sum array as n space-separated integers.

Sample Input 1:
4
1 2 3 4
Sample Output 1:
1 3 6 10
Each position accumulates the sum of previous values.
 """

from itertools import accumulate

n = int(input())
arr = list(map(int, input().split()))
print(*list(accumulate(arr)))
