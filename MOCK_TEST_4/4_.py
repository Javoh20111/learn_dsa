""" 
Letters A to Z are encoded as numbers 1 to 26:

Copy
A=1, B=2, C=3, ..., I=9, J=10, K=11, ..., Z=26
Given a string of digits, count the number of ways it can be decoded back into letters.

A digit '0' alone is invalid. A two-digit group like '06' is also invalid because it has a leading zero (it is not the same as '6').

Input
A single line containing a non-empty string s (1 ≤ |s| ≤ 100) consisting of digits 0–9.

Output
Print a single integer — the number of ways to decode the string. Print 0 if there is no valid decoding.

Subtasks:

Subtask 1 (5 points): |s| ≤ 5
Subtask 2 (5 points): |s| ≤ 30
Subtask 3 (5 points): |s| ≤ 100
Sample Input 1:
Copy
12
Sample Output 1:
Copy
2
The string "12" can be split in two different ways:

Copy
"1" + "2"  →  A + B  =  "AB"
"12"       →  L      =  "L"
Both splits are valid, so the answer is 2.

Sample Input 2:
Copy
226
Sample Output 2:
Copy
3
Three valid decodings exist:

Copy
"2" + "2" + "6"  →  B + B + F  =  "BBF"
"22" + "6"       →  V + F      =  "VF"
"2" + "26"       →  B + Z      =  "BZ"
Sample Input 3:
Copy
06
Sample Output 3:
Copy
0
"06" cannot be treated as the number 6 because it has a leading zero. No valid decoding exists.

Source
This problem is based on LeetCode 91: Decode Ways.
 """



import string
n = int(input())

upper_letters = list(string.ascii_uppercase)
dictionary = dict()

count = 1
for i in upper_letters:
    dictionary[i] = count
    count+=1

