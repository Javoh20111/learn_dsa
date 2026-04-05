## Maximum Units on a Truck

""" 
You are putting boxes on a truck. You are given n box types, where the ith box type has numberOfBoxes boxes available and each box contains numberOfUnits units.

The truck can carry at most truckSize boxes in total. You want to maximize the total number of units loaded onto the truck.

Return the maximum total number of units that can be put on the truck.

Input
The first line contains two integers n and truckSize (1 ≤ n ≤ 10^3, 1 ≤ truckSize ≤ 10^6).

Each of the next n lines contains two integers numberOfBoxes and numberOfUnitsPerBox (1 ≤ numberOfBoxes ≤ 10^3, 1 ≤ numberOfUnitsPerBox ≤ 10^3).

Output
Print a single integer — the maximum total number of units on the truck.

Sample Input 1:
3 4
1 3
2 2
3 1
Sample Output 1:
8
Sort by units per box descending: [(1, 3), (2, 2), (3, 1)]. Take 1 box of 3 units = 3, remaining capacity = 3. Take 2 boxes of 2 units = 4, remaining = 1. Take 1 box of 1 unit = 1, remaining = 0. Total = 3 + 4 + 1 = 8.
"""