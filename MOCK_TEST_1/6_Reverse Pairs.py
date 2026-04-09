## Reverse Pairs
""" 
Given an integer array, count the number of pairs (i, j) such that i < j and a_i > 2 * a_j.

Input
The first line contains an integer n (1 <= n <= 2*10^5).

The second line contains n integers a_i (-10^9 <= a_i <= 10^9).

Output
Print the number of reverse pairs. The answer fits in 64-bit signed integer.

Sample Input 1:
5
1 3 2 3 1
Sample Output 1:
2
Sample Input 2:
4
2 4 3 5 1
 """

## brute forse didnt work. What else do we have
""" n = int(input())
arr = list(map(int, input().split()))
count = 0
for i in range(len(arr)):
    for j in range(1,len(arr)):
        if i < j and arr[i] > (arr[j] * 2):
            count += 1
print(count) """


