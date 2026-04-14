## 01. Fibonacci

""" 
Given an integer n, find the n-th Fibonacci number modulo 10^9 + 7.

The Fibonacci sequence is defined as:

F(1) = 1
F(2) = 1
F(n) = F(n-1) + F(n-2) for n > 2
Since the answer can be very large, print it modulo 10^9 + 7 (1000000007).

Input
A single integer n (1 ≤ n ≤ 10^6).

Output
Print the n-th Fibonacci number modulo 10^9 + 7.

Sample Input 1:
6
Sample Output 1:
8
The Fibonacci sequence builds up as follows. Each value is the sum of the two preceding values:

Index:  1   2   3   4   5   6
      +---+---+---+---+---+---+
F(n): | 1 | 1 | 2 | 3 | 5 | 8 |
      +---+---+---+---+---+---+
            \   \ |   \ |   \ |
             +-->sum  sum   sum
So F(6) = F(5) + F(4) = 5 + 3 = 8.

 """

def fibonacci(n):
    mod = 1000000007

    if n == 0:
        return 0
    if n == 1:
        return 1

    prev2 = 0
    prev1 = 1

    for i in range(2, n+1):
        current = (prev2+prev1)%mod
        prev2 = prev1
        prev1 = current

    return prev1

n = int(input())
print(fibonacci(n))
