""" 
Given a real number a and a non-negative integer b, compute a^b.

Input
A single line containing a real number a and a non-negative integer b.

Output
Print a^b rounded to 5 decimal places.

Constraints
-100.0 ≤ a ≤ 100.0 (at most 1 decimal place)
0 ≤ b ≤ 10^9
The result is guaranteed to fit within standard double-precision floating-point range.
Subtasks:

Subtask 1 (3 points): |a| ≤ 10.0, b ≤ 100
Subtask 2 (4 points): -100.0 ≤ a ≤ 100.0, b ≤ 10^5
Subtask 3 (3 points): -100.0 ≤ a ≤ 100.0, b ≤ 10^9
Notes
Recursion is encouraged and will not be penalized by the judge.
a^0 = 1.00000 for any value of a.
Sample Input 1:
Copy
2.0 10
Sample Output 1:
Copy
1024.00000
2.0 is multiplied by itself. At each recursive step the exponent halves:

pow(2.0, 10) → pow(2.0, 5)^2
pow(2.0, 5) → 2.0 * pow(2.0, 4)
pow(2.0, 4) → pow(2.0, 2)^2 → ... → 1024.00000
Sample Input 2:
Copy
-2.0 5
Sample Output 2:
Copy
-32.00000
The base is negative and the exponent is odd, so the result is negative. The recursive halving still applies — note how the sign is carried through each multiplication step.

Sample Input 3:
Copy
0.5 1000000000
Sample Output 3:
Copy
0.00000
The exponent is 10^9, far too large for a naive loop. A recursive approach reduces this to ~30 steps by repeatedly halving the exponent. Since 0.5 < 1, the value shrinks toward zero with each multiplication, becoming negligibly small.
 """

a,b = map(float, input().split())
MOD = 1000000007
def recursion(a,b, mod=MOD):
    if b == 0:
        return 1      ## 2 10
    if b % 2 == 1:
        return a * recursion(a, b-1, MOD)
    else:
        return recursion(a*a, b//2, mod)
print(f'{recursion(a,b, mod=MOD):.5f}')