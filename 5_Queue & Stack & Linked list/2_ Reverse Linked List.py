## Middle of the Linked List

""" 
Given the head of a singly linked list, return the middle node.
If the list has two middle nodes, return the second middle node.
In this judge format, print the values from the returned middle node to the end of the list.

Input
First line: integer n (number of nodes)
Second line: n integers representing node values in order
Constraints:

1 <= n <= 2 * 10^5
-10^5 <= value_i <= 10^5
Output
Print the linked list values starting from the middle node to the end.

Sample Input 1:
5
1 2 3 4 5
Sample Output 1:
3 4 5

"""

class LinkedList:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

n = int(input())
arr = list(map(int, input().split()))

head = LinkedList(arr[0])
curr = head

for value in arr[1:]:
    curr.next = LinkedList(value)
    curr = curr.next

slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

curr = slow
half = []

while curr:
    half.append(str(curr.val))
    curr = curr.next
print(*half)


