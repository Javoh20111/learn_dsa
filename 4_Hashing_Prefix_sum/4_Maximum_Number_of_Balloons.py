## Maximum Number of Balloons

""" 
Given a string, determine how many times the word balloon can be formed using its letters. Each letter can be used at most once.

Input
The only line contains a string s (1 <= |s| <= 10000) consisting of lowercase English letters.

Output
Print the maximum number of times the word balloon can be formed.

Sample Input 1:
nlaebolko
Sample Output 1:
1
The letters can form one balloon.
 """


from collections import Counter
import math
s = list(map(str, input().strip()))

count1 = Counter(s)
target = Counter('balloon')
count = math.inf
for key, val in target.items():
    count = min(count, count1[key]//target[key])
print(count)

