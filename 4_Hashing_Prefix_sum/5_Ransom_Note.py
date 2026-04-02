## Ransom Note

""" 
Given two strings ransom and magazine, determine if ransom can be constructed from the letters of magazine. Each letter in magazine can be used at most once.

Input
The first line contains the string ransom (1 <= |ransom| <= 100000).

The second line contains the string magazine (1 <= |magazine| <= 100000).

Both strings consist of lowercase English letters.

Output
Print true if ransom can be constructed, otherwise print false.

Sample Input 1:
a
b
Sample Output 1:
false
b does not contain the letter a.
 """
from collections import Counter

ransom = list(map(str, input().strip()))
magazine = list(map(str, input().strip()))

counted_ransom = Counter(ransom)
counted_magazine = Counter(magazine)
status = "true"

for key, val in counted_ransom.items():
    if key not in magazine or (counted_ransom[key] > counted_magazine[key]):
        status = 'false'

print(status)