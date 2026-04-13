"""Reduce Array Size to the Half.

You are given an integer array of n elements. You can choose a set of integers and remove all occurrences of those integers from the array.

Return the minimum size of the set so that at least half of the elements of the array are removed.

Input
The first line contains an integer n (2 ≤ n ≤ 10^5, n is even).

The second line contains n integers arr[i] (1 ≤ arr[i] ≤ 10^5).

Output
Print a single integer — the minimum number of distinct values to choose so that at least n/2 elements are removed.

Sample Input 1:
Copy
10
3 3 3 3 5 5 5 2 2 7
Sample Output 1:
Copy
2
Frequencies: 3 appears 4 times, 5 appears 3 times, 2 appears 2 times, 7 appears 1 time. Need to remove at least 5 elements. Choose {3}: removes 4 (not enough). Choose {3, 5}: removes 7 ≥ 5. Answer = 2.

Sample Input 2:
Copy
6
1 1 2 2 3 3
Sample Output 2:
Copy
2
Each value appears twice. Need to remove at least 3 elements. Choosing one value removes 2 (not enough). Choosing two values removes 4 ≥ 3. Answer = 2.

"""

from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

counted = Counter(arr)

freqs=[]
for key,val in counted.items():
    freqs.append(val)

freqs.sort(reverse=True)

target=n//2
removed=0
chosen=0

for freq in freqs:
    removed+= freq
    chosen+= 1
    if removed >= target:
        break
print(chosen)


