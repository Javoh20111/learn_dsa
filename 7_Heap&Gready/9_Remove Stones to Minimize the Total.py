## Remove Stones to Minimize the Total

"""
You are given an array of n integers piles where piles[i] is the number of stones in the ith pile, and an integer k.

In one operation, you choose any pile piles[i] and remove floor(piles[i] / 2) stones from it (the pile becomes piles[i] - floor(piles[i] / 2)).

Apply the operation exactly k times. Return the minimum possible total number of stones remaining after the operations.

Input
The first line contains two integers n and k (1 ≤ n ≤ 10^5, 1 ≤ k ≤ 10^5).

The second line contains n integers piles[i] (1 ≤ piles[i] ≤ 10^4).

Output
Print a single integer — the minimum possible total number of stones remaining.

Sample Input 1:
3 2
5 4 9
Sample Output 1:
12
Pick pile with 9 stones, remove floor(9/2) = 4, pile becomes 5. Piles = [5, 4, 5]. Pick pile with 5 stones, remove floor(5/2) = 2, pile becomes 3. Piles = [3, 4, 5]. Total = 12.
"""
import math
from heapq import heapify, heappop, heappushpop, heappush
n, k = map(int, input().split())
arr = list(map(int, input().split()))

max_heap = [-x for x in arr]
heapify(max_heap)

for i in range(k):
    piles = heappop(max_heap)
    pile = piles + (-math.ceil(piles/2))
    heappush(max_heap, pile)
print(-sum(max_heap))

