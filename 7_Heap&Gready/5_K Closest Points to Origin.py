"""
Given an array of n points on the X-Y plane and an integer k, find the k closest points to the origin (0, 0).

The distance between a point (x, y) and the origin is sqrt(x^2 + y^2). The answer is guaranteed to be unique (no ties at the kth boundary).

Output the k closest points sorted by their distance to the origin in ascending order. If two points have the same distance, sort by x-coordinate first, then by y-coordinate.

Input
The first line contains two integers n and k (1 ≤ k ≤ n ≤ 10^4).

Each of the next n lines contains two integers x and y (-10^4 ≤ x, y ≤ 10^4).

Output
Print k lines, each containing two space-separated integers x y, representing the k closest points sorted by distance.

Sample Input 1:
3 2
1 3
-2 2
5 8
Sample Output 1:
-2 2
1 3
Distances: sqrt(10), sqrt(8), sqrt(89). The 2 closest are (-2, 2) with distance sqrt(8) and (1, 3) with distance sqrt(10).
"""