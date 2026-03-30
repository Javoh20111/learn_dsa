""" 
You are given a sum of integers 1, 2, and 3 written as a string separated by + signs. Rearrange the numbers so that the sum is in nondecreasing order.

Input
The only line contains a string s consisting of digits 1, 2, and 3 separated by + signs. The length of s is at most 2*10^5.

Output
Print the rearranged sum in nondecreasing order, using the same + separator.

Sample Input 1:
3+2+1

Sample Output 1:
1+2+3
"""


arr = list(map(int,input().split('+')))
arr.sort()

def sort_in_place(arr):
    return '+'.join(list(map(str,arr)))
print(sort_in_place(arr))