## Subset Sum

""" 
Given an array of n positive integers and a target value sum, determine if there is a subset of the array with a sum equal to the given sum.

Input
The first line contains two integers n and sum (1 ≤ n ≤ 20, 1 ≤ sum ≤ 10^6) — the number of elements and the target sum.

The second line contains n positive integers arr[i] (1 ≤ arr[i] ≤ 10^5), separated by spaces.

Output
Print YES if there exists a subset of the array whose elements sum to sum, otherwise print NO.

Sample Input 1:
6 9
3 34 4 12 5 2
Sample Output 1:
YES
The subset {4, 5} has sum 4 + 5 = 9.

Backtracking tree (include/exclude each element):

             []  sum=9
            / \
         [3]    []
         s=6    s=9
        / \     / \
   [3,34] [3] [34]  []
   skip   s=6 skip  s=9
          ...         ...
The algorithm explores including or excluding each element, pruning branches where the running sum exceeds the target.
 """

 
def solve():
    n, sum = map(int,input().split())
    arr = list(map(int,input().split()))

    def bkt_sum(ind, rem):
        if rem == 0:
            return True
        if ind == n:
            return False
        if rem < 0:
            return False
        
        if bkt_sum(ind+1 , rem - arr[ind]):
            return True
        if bkt_sum(ind+1, rem):
            return True
        
        return False
    
    print("YES" if bkt_sum(0, sum) else "NO")

solve()