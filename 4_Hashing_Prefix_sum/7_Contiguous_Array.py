## Contiguous Array

""" 
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Input
The first line contains an integer n (1 <= n <= 100000).

The second line contains n integers a_1, a_2, ..., a_n where each a_i is 0 or 1.

Output
Print the maximum length of a contiguous subarray with equal number of zeros and ones.

Sample Input 1:
2
0 1
Sample Output 1:
2
The whole array has one 0 and one 1.
"""

from collections import Counter
import math

n = int(input())
arr = list(map(int, input().split()))

count = Counter(arr)
count1 = math.inf
if len(arr) == 1:
    print(0)
else:

    for key, val in count.items():
        count1 = min(count1, val)
    print(val*2)