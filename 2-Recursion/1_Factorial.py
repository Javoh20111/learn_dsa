""" 
Given a non-negative integer n, compute n! (the factorial of n).

Input
The input consists of a single integer n.

Output
Print the value of n!.

Constraints
0 <= n <= 20
Notes
Recursion is encouraged and will not be penalized by the judge.
Sample Input 1:
Copy
0
Sample Output 1:
Copy
1
By definition, 0! = 1.
 """

def foctorial(n):
    if n == 0:
        return 1
    else:
        return n * foctorial(n-1)

n = int(input())
print(foctorial(n))