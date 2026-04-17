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



def solve(s):
    length = len(s)
    if s[0] == '0':
        print(0)
        return
    temp = [0] * (length+1)
    temp[0] = 1
    temp[1] = 1

    for i in range(2, length+1):
        o_d = int(s[i-1])
        t_d = int(s[i-2: i])

        if 1<= o_d <= 9:
            temp[i] += temp[i-1]
        if 10 <= t_d <=26:
            temp[i]+=temp[i-2]
    if temp[length] == 0:
        print(0)
    else:
        print(temp[length])


s = input().strip()
solve(s)
