## Find Maximum in Array (Recursive)

""" 
Find the maximum value in an array.

Input
The first line contains an integer n.

The second line contains n integers a[0..n-1].

Output
Print the maximum value in the array.

Constraints
1 <= n <= 10^4
-10^9 <= a[i] <= 10^9
Notes
Recursion is encouraged and will not be penalized by the judge.
Sample Input 1:
5
1 3 2 9 4
Sample Output 1:
9
The maximum value is 9.
 """

def find_max(n,arr):
    if n == 1:
        return arr[0]
    return max(arr[n-1], find_max(n-1, arr))

n = int(input())
arr = list(map(int, input().split()))
print(find_max(n, arr))
