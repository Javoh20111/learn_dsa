""" 
A sentence is a pangram if it contains every lowercase English letter at least once.
Given a sentence, determine whether it is a pangram.

Input
The only line contains a string sentence of lowercase English letters (1 <= |sentence| <= 1000).

Output
Print true if the sentence is a pangram, otherwise print false.

Sample Input 1:
thequickbrownfoxjumpsoverthelazydog
Sample Output 1:
true
All 26 letters appear at least once.

Sample Input 2:
leetcode
Sample Output 2:
false
Several letters are missing.
 """

import string
alp = set(string.ascii_lowercase)
sentence = set(input())
if alp == sentence:
    print('true')
else:
    print('false')