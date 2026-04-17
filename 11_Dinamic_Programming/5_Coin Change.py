## 5. Coin Change

""" 
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1. You may assume that you have an infinite number of each kind of coin.

Input
The first line contains two integers n and amount (1 ≤ n ≤ 12, 0 ≤ amount ≤ 10^4), where n is the number of coin denominations and amount is the target amount.

The second line contains n space-separated integers coins[i] (1 ≤ coins[i] ≤ 10^4), representing the denominations. All coin values are distinct.

Output
Print a single integer: the minimum number of coins needed to make up the given amount, or -1 if it is impossible.

Sample Input 1:
Copy
3 11
1 2 5
Sample Output 1:
Copy
3
We need to make amount 11 using coins [1, 2, 5]. The optimal solution uses 5 + 5 + 1 = 11 with 3 coins.

Other combinations require more coins, for example: 5 + 2 + 2 + 2 = 11 (4 coins), 2 + 2 + 2 + 2 + 2 + 1 = 11 (6 coins).
 """

def coin_exchange(n, amount, coins):
    dp = [float('inf')]*(amount+1)
    dp[0] = 0

    for cur_coin in range(1, amount+1):
        for coin in coins:
            if coin <= cur_coin:
                dp[cur_coin] = min(dp[cur_coin], dp[cur_coin - coin]+1)

    if dp[amount] == float('inf'):
        print(-1)
    else:
        print(dp[amount])

n, amount = map(int,input().split())
coins = list(map(int,input().split()))
coin_exchange(n, amount, coins)
