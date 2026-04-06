## Reduce Array Size to the Half
""" You are given an integer array of n elements. You can choose a set of integers and remove all occurrences of those integers from the array.

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
Frequencies: 3 appears 4 times, 5 appears 3 times, 2 appears 2 times, 7 appears 1 time. Need to remove at least 5 elements. Choose {3}: removes 4 (not enough). Choose {3, 5}: removes 7 ≥ 5. Answer = 2. """