## Maximum 69 Number

"""
You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9 or 9 becomes 6).

Input
A single line containing the integer num (1 ≤ num ≤ 10^4, consisting only of digits 6 and 9).

Output
Print the maximum number achievable by changing at most one digit.

Sample Input 1:
9669
Sample Output 1:
9969
Changing the first 6 (second digit) to 9 gives 9969, which is the maximum. Changing the other 6 would give 9699, which is smaller.
"""

n = int(input())
dev = 10000
for i in range(4):
    dev /= 10
    res = (n // dev) % 10 
    if res == 6:
        final_res = int(n+(dev*3))
        break
print(final_res)