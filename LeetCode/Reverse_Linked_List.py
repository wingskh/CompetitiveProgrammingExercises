# https://leetcode.com/problems/reverse-linked-list/
from typing import Optional
import sys
sys.path.append('../')
from Useful_Function.ListNode import display_listnode, list_to_listnode

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        new_head = None
        while head:
            head_next = head.next
            head.next = new_head
            new_head = head
            head = head_next

        return new_head



head = [1,2,3,4,5]
# head = [1,2]
# head = []
head = list_to_listnode(head)
# Output: [5,4,3,2,1]
sol = Solution()
result = sol.reverseList(head)
display_listnode(result)
