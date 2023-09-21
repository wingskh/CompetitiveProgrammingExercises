# https://leetcode.com/problems/linked-list-cycle/
from typing import Optional
import sys
sys.path.append('../')
from Useful_Function.ListNode import list_to_listnode

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Method 1: Hash Table
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()

        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        
        return False
    
    # Method 2: Two-Pointer (Floyd's Cycle-Finding Algorithm)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast_pointer = slow_pointer = head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if fast_pointer == slow_pointer:
                return True

        return False
    


head = [3,2,0,-4]
pos = 1
head = [1,2]
pos = 0
head = [1]
pos = -1
head = list_to_listnode(head)
sol = Solution()
result = sol.hasCycle(head)
print(result)
