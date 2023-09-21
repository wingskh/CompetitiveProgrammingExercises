# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        
        count = 1
        cur_node = head
        while cur_node.next:
            cur_node = cur_node.next
            count += 1

        cut_pt = count - n
        cur_node = head
        count = 1
        if cut_pt == 0:
            head = head.next
        else:
            while count != cut_pt:
                cur_node = cur_node.next
                count += 1

        cur_node.next = cur_node.next.next

        return head

# head = [1,2,3,4,5]
# n = 2
head = [1]
n = 1
# head = [1,2]
# n = 2
head = list_to_listnode(head)
sol = Solution()
result = sol.removeNthFromEnd(head, n)
# print(result)
display_listnode(result)
