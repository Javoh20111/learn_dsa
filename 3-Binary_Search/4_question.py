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
""" from collections import Counter
import math

letters = list(input().strip())

def count_balloon(letters):
    available = Counter(letters)
    required = Counter('balloon')

    max_balloons = math.inf

    for char in required:
        max_balloons = min(max_balloons, available[char]//required[char])
        return max_balloons
print(count_balloon(letters)) """


""" 
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be inserted in order.

Input
The first line contains an integer n (1 <= n <= 2*10^5). The second line contains n distinct sorted integers a_i (-10^9 <= a_i <= 10^9). The third line contains the target integer t.

Output
Print the insertion index (0-based).

Sample Input 1:
4
1 3 5 6
5
Sample Output 1:
2
The target 5 is at index 2.
 """

import bisect

n = int(input())
arr = list(map(int, input().split()))
target = int(input())

def binary_insert(arr, target):
    pos = bisect.bisect_left(arr, target)
    return pos
print(binary_insert(arr,target))
