""" 
You are recording network ping requests. Each ping arrives at timestamp t milliseconds.

After each ping, count how many pings have been made in the last 3000 milliseconds (inclusive), i.e. in the range [t - 3000, t].

It is guaranteed that timestamps are strictly increasing.

Input
The first line contains an integer n (1 ≤ n ≤ 10^4) — the number of pings.

The next n lines each contain a single integer t (1 ≤ t ≤ 10^9) — the timestamp of each ping, in strictly increasing order.

Output
For each ping, print the count of pings in the range [t - 3000, t] on a separate line.

Subtasks:

Subtask 1 (3 points): n ≤ 10
Subtask 2 (4 points): n ≤ 100
Subtask 3 (3 points): n ≤ 10000
Sample Input 1:
Copy
4
1
100
3001
3002
Sample Output 1:
Copy
1
2
3
3
Timeline of active pings at each step (window = last 3000 ms):

Copy
t=   1   [-------- window --------]  active: {1}            -> 1
t= 100   [-------- window --------]  active: {1, 100}       -> 2
t=3001   [-------- window --------]  active: {1, 100, 3001} -> 3
t=3002   [-------- window --------]  active: {100, 3001, 3002} -> 3
          ^--- t=1 falls out of [2, 3002]
Sample Input 2:
Copy
3
642
1849
4921
Sample Output 2:
Copy
1
2
1
At t=4921, the window is [1921, 4921]. Both t=642 and t=1849 are below 1921 and fall outside the window — only the current ping remains.

Sample Input 3:
Copy
5
1
100
200
3001
3002
Sample Output 3:
Copy
1
2
3
4
4
At t=3002 the window is [2, 3002]. The ping at t=1 drops out since 1 < 2, leaving four pings in the window: {100, 200, 3001, 3002}.

Source
This problem is based on LeetCode 933: Number of Recent Calls.


 """

""" n = int(input())
pings = []
res = []
for i in range(n):
    count = 0
    t = int(input())
    left = t - 3000
    right = t
    pings.append(t)
    for ping in pings:
        if ping >= left and ping <= right:
            count+=1
    res.append(count)
for i in res:
    print(i) """
import bisect
n = int(input())
pings = []

for i in range(n):
    count = 0
    t = int(input())
    pings.append(t)

for ping in pings:
    left_limit = ping - 3000
    left = bisect.bisect_left(pings,left_limit)
    right = bisect.bisect_right(pings, ping)
    print(right-left)
