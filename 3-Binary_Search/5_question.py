""" 
You are given an integer array. Sort it in nondecreasing order.

Input
The first line contains an integer n (1 <= n <= 2*10^5). The second line contains n integers a_i (-10^9 <= a_i <= 10^9).

Output
Print the sorted array in one line.

Sample Input 1:
5
5 2 3 1 4
Sample Output 1:
1 2 3 4 5
The output is the array in nondecreasing order.
 """

n = int(input())
arr = list(map(int, input().split()))


def divide_two(arr):
    if len(arr) == 1:
        return arr
    middle = len(arr) // 2
    left = divide_two(arr[:middle])
    right = divide_two(arr[middle:])
    return merger(left, right)


def merger(left, right):
    l = 0
    r = 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r+=1
    result.extend(left[l:])
    result.extend(right[r:])
    return result

print(divide_two(arr))