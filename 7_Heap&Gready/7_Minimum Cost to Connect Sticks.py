## Minimum Cost to Connect Sticks

"""
You have n sticks with given lengths. You must connect all sticks into one by repeatedly joining any two sticks. The cost of connecting two sticks is the sum of their lengths. Return the minimum total cost to connect all sticks into one.

Input
The first line contains an integer n (1 ≤ n ≤ 10^4).

The second line contains n integers representing the stick lengths (1 ≤ sticks[i] ≤ 10^4).

Output
Print a single integer — the minimum cost to connect all sticks. If there is only one stick, print 0.

Sample Input 1:
4
2 4 3 1
Sample Output 1:
19
Connect 1 and 2 → cost 3, sticks = [3, 4, 3]. Connect 3 and 3 → cost 6, sticks = [4, 6]. Connect 4 and 6 → cost 10, sticks = [10]. Total = 3 + 6 + 10 = 19.
"""