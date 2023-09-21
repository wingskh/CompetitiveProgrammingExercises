# https://leetcode.com/problems/reorder-list/
from typing import Optional
import sys
sys.path.append('../')
from Useful_Function.ListNode import display_listnode
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle
        if not (head.next and head.next.next): return
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second_head = slow.next
        next_node = slow.next and slow.next.next
        second_head.next = slow.next = None

        while next_node:
            second_head, next_node = next_node, second_head
            second_head.next, next_node = next_node, second_head.next

        # reorder
        while second_head:
            next_node = head.next
            head.next = second_head
            head = head.next
            second_head = next_node

head = [1,2,3,4, 5]
head = [1]
head_list = None
prev_node = None
for h in head:
    if head_list is None:
        head_list = ListNode(h)
        prev_node = head_list
    else:
        cur_node = ListNode(h)
        prev_node.next = cur_node
        prev_node = prev_node.next

# Output: [1,4,2,3]

sol = Solution()
sol.reorderList(head_list)
display_listnode(head_list)
