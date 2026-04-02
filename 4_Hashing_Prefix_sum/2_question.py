## Counting Elements

""" 
Given an integer array, count how many elements x have x + 1 also present in the array. If there are duplicates in the array, count them separately.

Input
The first line contains an integer n (1 <= n <= 1000).

The second line contains n integers a_1, a_2, ..., a_n (0 <= a_i <= 1000).

Output
Print the count of elements x such that x + 1 is present in the array.

Sample Input 1:
3
1 2 3
Sample Output 1:
2
1 and 2 are counted because 2 and 3 exist.
 """

n = int(input())
arr = list(map(int, input().split()))
copy_arr = set(arr[:])

count = 0
for i in arr:
    if i+1 in copy_arr:
        count+=1

print(count)