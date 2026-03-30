""" 
You are given a list of n integers. Count how many distinct values appear in the list.

Input
The first line contains an integer n (1 <= n <= 2*10^5). The second line contains n integers a_i (1 <= a_i <= 10^9).

Output
Print the number of distinct values in the list.

Sample Input 1:
Copy
5
2 3 2 2 3
 """


n = int(input())
arr = set(map(int, input().split()))

def find_distict(arr):
    return arr

print(find_distict(arr))