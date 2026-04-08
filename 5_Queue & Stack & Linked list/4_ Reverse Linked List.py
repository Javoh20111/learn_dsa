## Reverse Linked List

"""
Given the head of a singly linked list, reverse the list and return the new head.

In this judge format, output the full reversed list.

Input
First line: integer n (number of nodes)
Second line: n integers representing node values in order
Constraints:

1 <= n <= 2 * 10^5
-10^9 <= value_i <= 10^9
Output
Print the n node values of the reversed linked list.

Sample Input 1:
5
1 2 3 4 5
Sample Output 1:
5 4 3 2 1
"""

class LinkedList:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

n = int(input())
arr = list(map(int, input().split()))

head = LinkedList(arr[-1])
curr = head

res = []
for value in range(len(arr)-2,-1,-1):
    curr.next = LinkedList(arr[value])
    curr = curr.next

curr = head
while curr:
    res.append(str(curr.val))
    curr = curr.next
print(*res)


