from collections import deque
n =int(input())
arr = list(map(int,input().split()))
stack = deque()
count = 0

for i in arr:
    stack.append(i)
    if stack and stack[-1] == 0:
        stack.pop()
        count += 1

for i in range(count):
    stack.append(0)
print(*stack)