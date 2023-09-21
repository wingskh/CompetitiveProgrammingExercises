# https://leetcode.com/problems/binary-tree-level-order-traversal/
from typing import Optional, List
import sys
sys.path.append('../')
from Useful_Function.TreeNode import list_to_treenode
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = deque()
        queue.append((root, 0))
        result = []
        while queue:
            node, level = queue.popleft()
            if level + 1  > len(result):
                result.append([])
            result[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return result

root = [3,9,20,None,None,15,7]
# Output: [[3],[9,20],[15,7]]
root = [3,9,20,None,None,15,7,11,12,13,14]
# Output: [[3],[9,20],[15,7],[11,12,13,14]]
root = list_to_treenode(root)
sol = Solution()
result = sol.levelOrder(root)
print(result)
