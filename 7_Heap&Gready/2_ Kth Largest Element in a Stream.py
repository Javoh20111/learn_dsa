## Kth Largest Element in a Stream

"""
You are given an integer k, an initial array of integers, and a sequence of new elements to add. After adding each new element, report the kth largest element in the current collection.

The kth largest element is the kth element when the collection is sorted in non-increasing order. Duplicate values are counted separately.

Input
The first line contains two integers n and k (0 ≤ n ≤ 10^4, 1 ≤ k ≤ n + 1), where n is the size of the initial array.

The second line contains n integers — the initial array elements (-10^4 ≤ a[i] ≤ 10^4). If n = 0, this line contains a single 0.

The third line contains an integer m (1 ≤ m ≤ 10^4) — the number of add operations.

Each of the next m lines contains a single integer — the element to add (-10^4 ≤ val ≤ 10^4).

Output
Print m lines. After each add operation, print the kth largest element.

Sample Input 1:
4 3
4 5 8 2
3
3
5
10
Sample Output 1:
4
5
5
Initial: [4, 5, 8, 2]. Add 3 → [2, 3, 4, 5, 8], 3rd largest = 4. Add 5 → [2, 3, 4, 5, 5, 8], 3rd largest = 5. Add 10 → [2, 3, 4, 5, 5, 8, 10], 3rd largest = 5.
"""

