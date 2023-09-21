# https://leetcode.com/problems/maximum-depth-of-binary-tree/
from typing import Optional
import sys
sys.path.append('../')
from Useful_Function.TreeNode import list_to_treenode

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Least Time Complexity
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def preorder(root, height):
            if not root:
                return height
            return max(preorder(root.left, height + 1), preorder(root.right, height + 1))
        return preorder(root, 0)
    
    # Least Space Complexity
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_height = 0
        if not root: return 0

        stack = [(root, 1)]
        while stack:
            node, height = stack.pop()
            max_height = max(max_height, height)
            if node.left:
                stack.append((node.left, height + 1))
            if node.right:
                stack.append((node.right, height + 1))

        return max_height

root = [3,9,20,None,None,15,7]
root = list_to_treenode(root)
sol = Solution()
result = sol.maxDepth(root)
print(result)
