## Find Players With Zero or One Losses

"""
You are given a list of matches where each match is represented by a winner and a loser. Find all players who have zero losses and all players who have exactly one loss.

Input
The first line contains an integer m (1 <= m <= 100000).

The next m lines each contain two integers winner and loser (1 <= winner, loser <= 100000, winner != loser).

Output
Print two lines:

Line 1: all players with zero losses in increasing order, separated by spaces, or EMPTY if none.
Line 2: all players with exactly one loss in increasing order, separated by spaces, or EMPTY if none.
Sample Input 1:
10
1 3
2 3
3 6
5 6
5 7
4 5
4 8
4 9
10 4
10 9
Sample Output 1:
1 2 10
4 5 7 8
Players 1, 2, and 10 never lose; players 4, 5, 7, and 8 lose exactly once.
"""

from collections import Counter
import bisect

winners = []
losers = []
res1 = []
res2 = []

n = int(input())
for i in range(0,n):
    w,l = map(int, input().split())
    winners.append(w)
    losers.append(l)

counted_winners = Counter(winners)
counted_losers = Counter(losers)

for key, val in counted_winners.items():
    if key not in counted_losers:
        bisect.insort(res1, key)
for key, val in counted_losers.items():
    if val == 1:
        bisect.insort(res2, key)
print(*res1)
print(*res2)



