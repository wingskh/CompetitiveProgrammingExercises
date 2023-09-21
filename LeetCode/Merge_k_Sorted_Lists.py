# https://leetcode.com/problems/merge-k-sorted-lists/
from typing import List, Optional
import sys
sys.path.append('../')
from Useful_Function.ListNode import display_listnode, list_to_listnode
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = deque(lists)
        while len(lists) > 1:
            list1 = lists.popleft()
            list2 = lists.popleft()
            temp_result = None
            temp_head = None
            temp_node = None
            
            while list1 and list2:
                if list1.val < list2.val:
                    temp_node = list1
                    list1 = list1.next
                else:
                    temp_node = list2
                    list2 = list2.next

                temp_node.next = None
                if temp_result is None:
                    temp_result = temp_node
                    temp_head = temp_result
                else:
                    temp_result.next = temp_node
                    temp_result = temp_result.next
            
            if list1 is not None or list2 is not None:
                if temp_result is None:
                    temp_result = list1 if list2 is None else list2
                    temp_head = temp_result
                else:
                    temp_result.next = list1 if list2 is None else list2

            lists.append(temp_head)

        return None if len(lists) == 0 else lists[0]
    
    
lists = [[1,4,5],[1,3,4],[2,6]]
lists = [[],[1]]
lists = [list_to_listnode(x) if len(x) > 0 else None for x in lists]
# Output: [1,1,2,3,4,4,5,6]
sol = Solution()
result = sol.mergeKLists(lists)
display_listnode(result)
