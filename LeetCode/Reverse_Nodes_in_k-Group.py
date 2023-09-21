# https://leetcode.com/problems/reverse-nodes-in-k-group/
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
        new_tail = head
        while head:
            head_next = head.next
            head.next = new_head
            new_head = head
            head = head_next
        return new_head, new_tail

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_head = None
        cur_node = head
        prev_tail = None
        next_node = None

        while True:
            temp_node = cur_node
            counter = 1
            while temp_node and counter != k:
                temp_node = temp_node.next
                counter += 1
            
            if temp_node:
                next_node = temp_node.next
                temp_node.next = None
                temp_head, temp_tail = self.reverseList(cur_node)
                cur_node = next_node
                if not new_head:
                    new_head = temp_head
                else:
                    prev_tail.next = temp_head
                
                prev_tail = temp_tail
                prev_tail.next = cur_node
            else:
                break
        return new_head

head = [1,2,3,4,5]
head = list_to_listnode(head)
k = 2
# Output: [2,1,4,3,5]
sol = Solution()
result = sol.reverseKGroup(head, k)
display_listnode(result)
