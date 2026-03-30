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

letters = list(input().strip())

def count_balloon(letters):
    available = Counter(letters)
    required = Counter('balloon')

    max_balloons = math.inf

    for char in required:
        max_balloons = min(max_balloons, available[char]//required[char])
        return max_balloons
print(count_balloon(letters))