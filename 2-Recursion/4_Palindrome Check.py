## Palindrome Check

""" 
Check whether a string is a palindrome.

Input
The input consists of a single line containing the string s (lowercase letters).

Output
Print YES if s is a palindrome, otherwise print NO.

Constraints
1 <= |s| <= 2000
Notes
Recursion is encouraged and will not be penalized by the judge.
Sample Input 1:
racecar
Sample Output 1:
YES
racecar reads the same forwards and backwards.

Sample Input 2:
abca
Sample Output 2:
NO
The string differs when reversed.

Sample Input 3:
aa
Sample Output 3:
YES
Both characters match.

Source
Original.
 """

def check_palindrome(s,l,r):
    if len(s) == 1 or l >= r:
        return 'YES'
    if s[l] != s[r]:
        return 'NO'
    else:
        return check_palindrome(s,l+1, r-1)

        

s = list(input().strip())
l, r = 0, len(s)-1
print(check_palindrome(s,l,r))
