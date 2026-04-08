## Reverse Linked List II

""" 
Given the head of a singly linked list and two integers left and right (1 <= left <= right <= n), reverse the nodes from position left to position right (1-indexed), and keep the rest unchanged.

Input
First line: integer n (number of nodes)
Second line: n integers representing node values in order
Third line: two integers left and right
Constraints:

1 <= n <= 2 * 10^5
-10^9 <= value_i <= 10^9
1 <= left <= right <= n
Output
Print the linked list after reversing the sublist [left, right].

Sample Input 1:
5
1 2 3 4 5
2 4
Sample Output 1:
1 4 3 2 5
 """
class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
n = int(input())
arr = list(map(int, input().split()))
l, r = map(int, input().split())
 
head = LinkedList(arr[0])
curr = head
for val in arr[1:]:
    curr.next = LinkedList(val)
    curr = curr.next
 
def reverse_between(head, l, r):
    if not head or l == r:
        return head
 
    dummy = LinkedList(0, head)
    prev = dummy
 
    for _ in range(l - 1):
        prev = prev.next
 
    curr = prev.next
    for _ in range(r - l):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp
 
    return dummy.next
 
result = reverse_between(head, l, r)
output = []
curr = result
while curr:
    output.append(str(curr.val))
    curr = curr.next
 
print(' '.join(output))