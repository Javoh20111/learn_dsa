## 4. House Robber

""" 
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. The constraint is that adjacent houses have security systems connected — if two adjacent houses are robbed on the same night, the police will be alerted.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Input
The first line contains an integer n (1 ≤ n ≤ 10^5) — the number of houses.

The second line contains n space-separated integers nums[i] (0 ≤ nums[i] ≤ 10^4) — the amount of money in each house.

Output
Print the maximum amount of money you can rob without robbing two adjacent houses.

Sample Input 1:
Copy
4
1 2 3 1
Sample Output 1:
Copy
4
The houses and the optimal rob/skip decisions:

Copy
House:    0     1     2     3
       +-----+-----+-----+-----+
Money: |  1  |  2  |  3  |  1  |
       +-----+-----+-----+-----+
         ROB   skip  ROB   skip
          1           3
                         Total = 1 + 3 = 4
Robbing houses 0 and 2 gives 1 + 3 = 4. We cannot rob house 1 or 3 alongside their neighbors without triggering the alarm. Alternative: robbing houses 1 and 3 gives 2 + 1 = 3, which is less.
 """

def lets_rob(n, arr):
    profit = [0] * (n+1)

    profit[0] = 0
    profit[1] = arr[0]

    for i in range(2, n+1):
        rob = arr[i-1] + profit[i-2]
        skip = profit[i-1]
        profit[i] = max(rob, skip)


    print(max(profit[n], profit[n-1]))
n = int(input())
arr = list(map(int, input().split()))
lets_rob(n,arr)