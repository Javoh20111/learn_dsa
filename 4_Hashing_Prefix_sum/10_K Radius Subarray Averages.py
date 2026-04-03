## K Radius Subarray Averages

""" 
For each index i in an array, compute the average of the subarray of length 2k + 1 centered at i. If there are fewer than k elements before or after i, the answer is -1 for that index.

Input
The first line contains two integers n and k (1 <= n <= 100000, 0 <= k <= n).

The second line contains n integers a_1, a_2, ..., a_n (0 <= a_i <= 100000).

Output
Print n space-separated integers where the i-th number is the k-radius average for index i. Averages are integer divisions (floor).

Sample Input 1:
7 1
7 4 3 9 1 8 5
Sample Output 1:
-1 4 5 4 6 4 -1
Each average uses a window of length 3.
 """


n, k = map(int, input().split())
arr = list(map(int, input().split()))
length = len(arr)
result = []

for i in range(length):
    if (i-k) < 0 or (i+k+1) > length:
        result.append(-1)
    else:
        cal = sum(arr[i-k:i+k+1])//(2*k+1)
        result.append(cal)
print(*result)
