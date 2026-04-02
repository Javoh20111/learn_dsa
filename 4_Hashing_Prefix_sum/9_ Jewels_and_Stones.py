## Jewels and Stones

""" 
You are given two strings: jewels and stones. Each character in jewels represents a jewel type. Count how many characters in stones are also jewels.

Input
The first line contains the string jewels (1 <= |jewels| <= 50).

The second line contains the string stones (1 <= |stones| <= 50).

Both strings consist of English letters.

Output
Print the number of stones that are jewels.

Sample Input 1:
aA
aAAbbbb
Sample Output 1:
3
a and A are jewels and appear three times in stones.
 """

from collections import Counter
jewels = list(input().strip())
stones = list(input().strip())

target = Counter(jewels)
count = Counter(stones)
total=0
for key, val in target.items():
    if key in count:
        total+=count[key]
print(total)