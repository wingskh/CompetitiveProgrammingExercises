# https://leetcode.com/problems/copy-list-with-random-pointer/
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ori_to_new_node_mapping = {None:None}

        ori_node = head
        while ori_node:
            ori_to_new_node_mapping[ori_node] = Node(ori_node.val)
            ori_node = ori_node.next
        
        ori_node = head
        while ori_node:
            new_node = ori_to_new_node_mapping[ori_node]
            new_node.next = ori_to_new_node_mapping[ori_node.next]
            new_node.random = ori_to_new_node_mapping[ori_node.random]
            ori_node = ori_node.next
        
        return ori_to_new_node_mapping[head]
 

head = [[7,None],[13,0],[11,4],[10,2],[1,0]]
sol = Solution()
result = sol.copyRandomList(head)

