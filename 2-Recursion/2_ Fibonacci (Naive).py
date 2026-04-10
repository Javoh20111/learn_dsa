## Fibonacci (Naive)

"""
Define the Fibonacci sequence as F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n >= 2. Compute F(n).

Input
The input consists of a single integer n.

Output
Print F(n).

Constraints
0 <= n <= 30
Notes
Recursion is encouraged and will not be penalized by the judge.
Sample Input 1:
Copy
0
Sample Output 1:
Copy
0
F(0) = 0.

Sample Input 2:
Copy
1
Sample Output 2:
Copy
1
F(1) = 1.
"""

n = int(input())

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)
print(fibonacci(n))