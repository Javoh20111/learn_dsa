## Longest Substring Without Repeating Characters

"""
Given a string, find the length of the longest substring without repeating characters.

Input
The only line contains a string s (1 <= |s| <= 100000).

The string consists of ASCII characters without spaces.

Output
Print the length of the longest substring with all distinct characters.

Sample Input 1:
Copy
abcabcbb
Sample Output 1:
Copy
3
The answer is abc with length 3.
"""
s = input().strip()
n = len(s)

left = 0
max_len = 0
chars_in_window = set()

for right in range(n):
    while s[right] in chars_in_window:
        chars_in_window.remove(s[left])
        left += 1
    chars_in_window.add(s[right])
    max_len = max(max_len, right - left + 1)
print(max_len)