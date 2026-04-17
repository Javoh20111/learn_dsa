""" 
You are given an integer array cost where cost[i] is the cost of the i-th step on a staircase. Once you pay the cost, you can either climb one or two steps. You can either start from the step with index 0, or the step with index 1. Return the minimum cost to reach the top of the floor (past the last element).

Input
The first line contains an integer n (2 ≤ n ≤ 10^5) — the number of steps.

The second line contains n space-separated integers cost[i] (0 ≤ cost[i] ≤ 999) — the cost of each step.

Output
Print the minimum cost to reach the top of the floor.

Sample Input 1:
Copy
3
10 15 20
Sample Output 1:
Copy
15
The array and the optimal path:

Copy
Index:    0     1     2     TOP
       +----+----+----+
cost:  | 10 | 15 | 20 |  --> (goal)
       +----+----+----+
              *----------->*
         start here     reach top!
         (index 1)      (jump 2)
Start at index 1, pay cost[1] = 15, then jump 2 steps to reach the top. Total cost: 15.

Starting at index 0 would cost at least 10 + 20 = 30 (go 0 -> 2 -> top), which is worse.

Sample Input 2:
Copy
10
1 100 1 1 1 100 1 1 100 1
Sample Output 2:
Copy
6
Copy
Index:     0    1    2    3    4    5    6    7    8    9
        +----+----+----+----+----+----+----+----+----+----+
cost:   |  1 |100 |  1 |  1 |  1 |100 |  1 |  1 |100 |  1 |
        +----+----+----+----+----+----+----+----+----+----+
The optimal path visits indices: 0 -> 2 -> 4 -> 6 -> 7 -> 9 -> top, paying 1+1+1+1+1+1 = 6. Notice how the path avoids the expensive steps (100) by jumping over them.
 """

""" def find_min_cost(n, arr):
    cost = [0] + arr

    dist = {}
    for i in range(n+1):
        dist[i] = float('inf')
    dist[0] = 0

    for i in range(1, n+1):
        if i - 1 >= 0:
            dist[i] = min(dist[i], dist[i-1]+cost[i])
        if i - 2 >= 0:
            dist[i] = min(dist[i], dist[i-2]+cost[i])

    ans = min(dist[n-1], dist[n])

    if ans == float('inf'):
        print(-1)
    else:
        print(ans)


n = int(input())
arr = list(map(int,input().split()))
find_min_cost(n,arr) """

def find_min_cost(n, arr):
    costs = [0]*(n+1)

    for i in range(2, n+1):
        costs[i] = min((costs[i-1] + arr[i-1]), (costs[i-2] + arr[i-2]))
    print(costs[n])

n = int(input())
arr = list(map(int,input().split()))
find_min_cost(n,arr)