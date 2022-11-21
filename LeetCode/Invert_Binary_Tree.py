# https://leetcode.com/problems/invert-binary-tree/
# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Recursion
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse(node):
            if node is not None:
                node.left, node.right = node.right, node.left
                reverse(node.left)
                reverse(node.right)
        
        reverse(root)
        return root

    # Non-recursion
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def is_valid(node):
            return True if node and node not in visited else False
            
        cur_node = root
        visited = set()
        parent_stack = deque()
        while is_valid(cur_node):
            if is_valid(cur_node.left):
                parent_stack.append(cur_node)
                cur_node = cur_node.left
            elif is_valid(cur_node.right):
                parent_stack.append(cur_node)
                cur_node = cur_node.right
            else:
                visited.add(cur_node)
                cur_node.left, cur_node.right = cur_node.right, cur_node.left
                if len(parent_stack) == 0:
                    break
                cur_node = parent_stack.pop()

        return root


root = [4,2,7,1,3,6,9]
sol = Solution()
result = sol.invertTree(root)
print(result)
