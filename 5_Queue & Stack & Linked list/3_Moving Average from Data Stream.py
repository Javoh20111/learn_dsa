## Moving Average from Data Stream

"""
Design a moving average calculator with a fixed window size k.

You are given a stream of n integers. For each new integer, compute the average of the last at most k elements seen so far.

If fewer than k elements have been seen, average all seen elements.
Otherwise, average only the most recent k elements.
Input
First line: two integers k and n
Second line: n integers x_i
Constraints:

1 <= k <= 2 * 10^5
1 <= n <= 2 * 10^5
-10^5 <= x_i <= 10^5
Output
Print n floating-point numbers on one line. The i-th number is the moving average after reading x_i. Print each value with exactly 6 digits after the decimal point.

Sample Input 1:
3 4
1 10 3 5
Sample Output 1:
1.000000 5.500000 4.666667 6.000000
"""
from collections import deque
def moving_average(k, arr,stack, result):
    for element in arr:
        stack.append(element)
        if stack and len(stack) > k:
            stack.popleft()
            pre_res = sum(stack)/len(stack)
            result.append(f'{pre_res:.6f}')
        else:
            pre_res = sum(stack)/len(stack)
            result.append(f'{pre_res:.6f}')
    return result


k, n = map(int,input().split())
arr = list(map(int,input().split()))
stack = deque()
result = []
print(*moving_average(k, arr, stack, result))
