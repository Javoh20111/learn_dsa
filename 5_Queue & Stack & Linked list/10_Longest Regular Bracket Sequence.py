## Longest Regular Bracket Sequence

"""
Given a string s consisting only of '(' and ')', find:

the length of the longest correct (well-formed) bracket substring
how many substrings of that maximum length exist
A correct bracket substring is contiguous and must form a valid parenthesis sequence.

If no non-empty correct bracket substring exists, output 0 1.

Input
A single line containing string s.

Constraints:

1 <= |s| <= 2 * 10^5
s[i] is either '(' or ')'
Output
Print two integers:

L: maximum length of a correct bracket substring
C: number of substrings with length L
Sample Input 1:
(()())
Sample Output 1:
6 1"""
from collections import deque
string = list(input().strip())
r_b = '('
l_b = ')'
stack = deque()
length = 1

for b in string:
    if stack and b == l_b and (stack[-1] == l_b or stack[-1] == None):
        length = 1
    if stack and stack[-1] == r_b and b == 'l_b':
        stack.pop()
        length += 1
    else:
        stack.append(b)
