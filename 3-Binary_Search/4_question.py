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
 """
from collections import Counter
import math

s = list(input().strip())

