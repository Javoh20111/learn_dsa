## Largest Unique Number

""" 
Given an integer array, find the largest number that occurs exactly once. If no such number exists, print -1.

Input
The first line contains an integer n (1 <= n <= 1000).

The second line contains n integers a_1, a_2, ..., a_n (0 <= a_i <= 1000).

Output
Print the largest unique number, or -1 if none exists.

Sample Input 1:
9
5 7 3 9 4 9 8 3 1
Sample Output 1:
8
The unique numbers are 5, 7, 4, 8, 1; the largest is 8.
 """

from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

counted = Counter(arr)
m = -1
for key,val in counted.items():
    if val == 1:
        m = max(m, key)
print(m)

