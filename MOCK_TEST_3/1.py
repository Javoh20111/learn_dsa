"""
Given two integer arrays g and s where g[i] is the greed factor of the i-th child and s[j] is the size of the j-th cookie. Your goal is to maximize the number of content children by assigning cookies to them.

Each child can receive at most one cookie, and a child i will be content only if they receive a cookie j such that s[j] >= g[i] (i.e., the cookie size is at least as large as the child's greed factor).

Input
The first line contains an integer n (1 <= n <= 10^5) --- the number of children.

The second line contains n space-separated integers g[1], g[2], ..., g[n] (1 <= g[i] <= 10^9) --- the greed factors of the children.

The third line contains an integer m (1 <= m <= 10^5) --- the number of cookies.

The fourth line contains m space-separated integers s[1], s[2], ..., s[m] (1 <= s[j] <= 10^9) --- the sizes of the cookies.

Subtasks:

Subtask 1 (3 points): n, m <= 100
Subtask 2 (4 points): n, m <= 10000
Subtask 3 (3 points): n, m <= 10^5
Output
Print a single integer --- the maximum number of content children.

Sample Input 1:
Copy
3
1 2 3
3
1 1 3
Sample Output 1:
Copy
2
Cookie of size 1 goes to the child with greed factor 1, and cookie of size 3 goes to the child with greed factor 3. The child with greed factor 2 cannot be satisfied (the remaining cookie has size 1, which is too small). Maximum content children: 2.


"""

n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()
m = int(input())
arr2 = list(map(int, input().split()))
arr2.sort()

i,j,count = 0,0,0

while i < len(arr1) and j < len(arr2):
    if arr2[j] >= arr1[i]:
        count+=1
        i+=1
    j+=1
print(count)

