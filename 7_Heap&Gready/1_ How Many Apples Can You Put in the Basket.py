## How Many Apples Can You Put in the Basket

"""
You have n apples, each with a given weight. A basket can hold a total weight of at most 5000 units.

Return the maximum number of apples you can put in the basket.

Input
The first line contains an integer n (1 ≤ n ≤ 10^3).

The second line contains n integers representing the weight of each apple (1 ≤ weight[i] ≤ 10^3).

Output
Print a single integer — the maximum number of apples that fit in the basket.

Sample Input 1:
5
1000 2000 1500 3000 500
Sample Output 1:
4
Sort by weight: [500, 1000, 1500, 2000, 3000]. Take 500 + 1000 + 1500 + 2000 = 5000 ≤ 5000. Adding the next apple (3000) would give 8000, which exceeds 5000. Answer: 4 apples.


"""

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
count = 0
total = 0

for i in arr:
    total += i 
    if total <= 5000:
        count+=1
print(count)