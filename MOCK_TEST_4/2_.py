""" 
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An anagram is a word formed by rearranging the letters of another, using all the original letters exactly once.

Input
Two lines, each containing a string — s on the first line and t on the second (1 ≤ |s|, |t| ≤ 5 × 10^4). Both strings consist of lowercase English letters only.

Output
Print true if t is an anagram of s, otherwise print false.

Subtasks:

Subtask 1 (3 points): |s|, |t| ≤ 10
Subtask 2 (4 points): |s|, |t| ≤ 1000
Subtask 3 (3 points): |s|, |t| ≤ 50000
Sample Input 1:
Copy
anagram
nagaram
Sample Output 1:
Copy
true
Both strings have the same character frequencies:

Copy
Letter : a  n  g  r  m
anagram: 3  1  1  1  1
nagaram: 3  1  1  1  1
Every letter appears the same number of times, so nagaram is an anagram of anagram.

Sample Input 2:
Copy
rat
car
Sample Output 2:
Copy
false
Comparing character frequencies:

Copy
Letter: r  a  t  c
rat   : 1  1  1  0
car   : 1  1  0  1
rat has a t but no c; car has a c but no t. The frequencies differ, so they are not anagrams.

Sample Input 3:
Copy
listen
silent
Sample Output 3:
Copy
true
Both strings consist of the same 6 letters {l, i, s, t, e, n}, each appearing exactly once — just in a different order.

Source
This problem is based on LeetCode 242: Valid Anagram.
 """
from collections import Counter
s = list(input().strip())
g = list(input().strip())
con_s = Counter(s)
con_g = Counter(g)
res= []
for key, val in con_s.items():
    if key not in con_g or val != con_g[key]:
        res.append(res)
        break
if len(res) != 1:
    print('true')
else:
    print('false')
