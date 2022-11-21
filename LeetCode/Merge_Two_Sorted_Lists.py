# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        root = ListNode()
        parent_node = root
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                parent_node.val = list1.val
                list1 = list1.next
            else:
                parent_node.val = list2.val
                list2 = list2.next
            if not list1 or not list2:
                break
            parent_node.next = ListNode()
            parent_node = parent_node.next
        
        parent_node.next = list1 if list2 is None else list2
        
        return root

        

def list_to_listnode(array):
    if len(array) == 0:
        return ListNode()
    root = ListNode(val=array[0])
    parent_node = root
    for i in array[1:]:
        cur_node = ListNode(val=i)
        parent_node.next = cur_node
        parent_node = cur_node
    return root

def print_listnode(root):
    result = []
    while root is not None:
        result.append(root.val)
        root = root.next
    return result

list1 = [1,2,4]
list2 = [1,3,4]

list1 = list_to_listnode(list1)
list2 = list_to_listnode(list2)
sol = Solution()
result = sol.mergeTwoLists(list1, list2)
print(print_listnode(result))