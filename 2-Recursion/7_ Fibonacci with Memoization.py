## Fibonacci with Memoization
"""
Compute the nth Fibonacci number using memoization.

Input
The input consists of a single integer n.

Output
Print F(n) mod 10^9 + 7.

Constraints
0 <= n <= 100000
Notes
Recursion is encouraged and will not be penalized by the judge.
Sample Input 1:
0
Sample Output 1:
0
F(0) = 0.

Sample Input 2:
10
Sample Output 2:
55
F(10) = 55.
"""
import sys
sys.setrecursionlimit(200000)
def fibo_with_memo(n,cashe):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        if n in cashe:
            return cashe[n]
        elif n not in cashe:
            cashe[n] = (fibo_with_memo(n-2,cashe) + fibo_with_memo(n-1,cashe))%1000000007
            return cashe[n]
n = int(input())
cashe = dict()
print(fibo_with_memo(n,cashe))