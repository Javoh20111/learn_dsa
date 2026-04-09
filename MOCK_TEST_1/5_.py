## Merge Intervals

""" 
Given a list of intervals, merge all overlapping intervals and return the resulting list sorted by start time.

Input
The first line contains an integer m (1 <= m <= 2*10^5).

Each of the next m lines contains two integers l and r (-10^9 <= l <= r <= 10^9) describing an interval [l, r].

Output
On the first line, print the number of merged intervals k. Then print the merged intervals in increasing order of start, one per line. Intervals are merged if the next interval starts at or before the current interval ends.

Sample Input 1:
4
1 3
2 6
8 10
15 18
Sample Output 1:
3
1 6
8 10
15 18
 """

n = int(input())
pairs = list()

for _ in range(n):
    l,r = map(int,input().split())
    pairs.append((l,r))

pairs.sort()

mer = list()
for l,r in pairs:
    if not mer:
        mer.append([l,r])
    else:
        p_l, p_r = mer[-1]

        if l <= p_r:
            mer[-1][1] = max(p_r, r)
        else:
            mer.append([l,r])
print(len(mer))
for l,r in mer:
    print(l,r)