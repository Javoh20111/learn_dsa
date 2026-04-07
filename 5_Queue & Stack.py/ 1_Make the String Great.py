## Make the String Great

""" 
A string is called good if it has no adjacent pair of characters where one is a lowercase letter and the other is the same letter in uppercase.

For example, aA and Bb are bad adjacent pairs and must be removed.

You may repeatedly remove such adjacent bad pairs until no more can be removed. Return the final good string.

Input
A single line containing string s.

Constraints:
1 <= |s| <= 2 * 10^5
s consists only of uppercase and lowercase English letters
Output
Print the final good string after all possible removals. If the result is empty, print an empty line.

Sample Input 1:
leEeetcode
Sample Output 1:
leetcode
"""

from collections import deque
mas = deque()
string = input()

for ch in string:
    if mas and mas[-1] == ch.swapcase():
        mas.pop()
    else:
        mas.append(ch)
print(''.join(mas))