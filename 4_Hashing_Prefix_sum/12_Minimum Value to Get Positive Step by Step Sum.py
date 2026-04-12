## Minimum Value to Get Positive Step by Step Sum

""" 
Given an integer array, choose the minimum positive starting value start such that the running sum start + a_1 + ... + a_i is always at least 1.

Input
The first line contains an integer n (1 <= n <= 100).

The second line contains n integers a_1, a_2, ..., a_n (-100 <= a_i <= 100).

Output
Print the minimum positive starting value.

Sample Input 1:
Copy
5
-3 2 -3 4 2
Sample Output 1:
Copy
5
Starting at 5 keeps the running sum positive.
 """

n = int(input())
arr = list(map(int,input().split()))

min_sum = 0
running = 0

for x in arr:
    running+=x
    min_sum = min(min_sum, running)

print(max(1, 1-min_sum))