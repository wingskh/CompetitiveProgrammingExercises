# https://leetcode.com/problems/binary-tree-maximum-path-sum/
import sys
sys.path.append('../')
from Useful_Function.TreeNode import list_to_treenode
from typing import Optional
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def path_sum(self, root):
        if not root:
            return 0
        left_sum = max(0, self.path_sum(root.left))
        right_sum = max(0, self.path_sum(root.right))
        self.max_sum = max(self.max_sum, left_sum + right_sum + root.val)
        return max(left_sum, right_sum) + root.val
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -math.inf
        self.path_sum(root)
        return self.max_sum

root = [-10,9,20,None,None,15,7]
root = list_to_treenode(root)
sol = Solution()
result = sol.maxPathSum(root)
print(result)
