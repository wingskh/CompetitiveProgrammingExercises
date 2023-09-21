# https://leetcode.com/problems/add-two-numbers/
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def addANumber(sum):
            nonlocal overflow, cur_node
            if sum > 9:
                cur_node.next = ListNode(sum % 10)
                overflow = 1
            else:
                cur_node.next = ListNode(sum)
                overflow = 0

        result = ListNode(-1)
        cur_node = result
        overflow = 0
        while l1 and l2:
            sum = l1.val + l2.val
            sum += overflow
            addANumber(sum)
            cur_node = cur_node.next
            l1 = l1.next
            l2 = l2.next

        l3 = l1 if l2 is None else l2
        while l3:
            sum = l3.val + overflow
            addANumber(sum)
            cur_node = cur_node.next
            l3 = l3.next

        if overflow:
            cur_node.next = ListNode(1)
        
        return result.next


l1 = [2,4,3]
l2 = [5,6,4]
# [7,0,8]
l1 = [0]
l2 = [0]
# [0]
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
# [8,9,9,9,0,0,0,1]
l1 = list_to_listnode(l1)
l2 = list_to_listnode(l2)
sol = Solution()
result = sol.addTwoNumbers(l1, l2)
display_listnode(result)
