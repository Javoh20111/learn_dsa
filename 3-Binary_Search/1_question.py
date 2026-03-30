""" 
Given a sorted array of integers and a target value, return the index of the target if it is present. Otherwise, return -1.

Input
The first line contains an integer n (1 <= n <= 2*10^5). The second line contains n sorted integers a_i (-10^9 <= a_i <= 10^9). The third line contains the target integer t.

Output
Print the index (0-based) of t in the array, or -1 if it is not present.

Sample Input 1:
Copy
6
-1 0 3 5 9 12
9 
"""


import bisect

n = int(input())
arr = list(map(int, input().split()))
target = int(input())


def find_element(n, arr, target):
    pos = bisect.bisect_left(arr, target)
    if pos < n and arr[pos] == target:
        return pos
    else:
        return -1

print(find_element(n, arr, target))