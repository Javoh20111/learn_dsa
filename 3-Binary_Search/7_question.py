"""
You are given an array of n integers. For each query [l, r], determine how many elements of the array have values between l and r, inclusive.

Input
The first line contains an integer n (1 <= n <= 10^5). The second line contains n integers a_i (-10^9 <= a_i <= 10^9). The third line contains an integer k (1 <= k <= 10^5) - the number of queries. Each of the next k lines contains two integers l and r (-10^9 <= l <= r <= 10^9).

Output
Print k integers - the answers for the queries, one per line.

Sample Input 1:
Copy
5
10 1 10 3 4
4
1 10
2 9
3 4
2 2
Sample Output 1:
Copy
5
2
2
0
Counts elements in each inclusive range.
"""


""" n = int(input())
arr = list(map(int, input().split()))
k = int(input())
pairs = []
for i in range(k):
    l,r = map(int,input().split())
    pairs.append([l,r])

def validate(arr,pairs):
    l = 0
    r = 1
    for pair in pairs:
        count = 0
        for element in arr:
            if pair[l] <= element and element <= pair[r]:
                count += 1
        print(count)

validate(arr,pairs) """   # ----> Not good.

import bisect

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

k = int(input())

for _ in range(k):
    l, r = map(int, input().split())
    
    left = bisect.bisect_left(arr, l)
    right = bisect.bisect_right(arr, r)
    
    print(right - left)