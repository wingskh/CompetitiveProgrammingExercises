# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
import sys
sys.path.append('../')
from Useful_Function.TreeNode import list_to_treenode
from collections import deque
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return []
        nums_of_good = 0
        queue = deque()
        queue.append((root, -math.inf))

        while queue:
            node, acc_max = queue.popleft()
            if node.val >= acc_max:
                nums_of_good += 1
            acc_max = max(acc_max, node.val)
            if node.left:
                queue.append((node.left, acc_max))
            if node.right:
                queue.append((node.right, acc_max))

        return nums_of_good

root = [3,1,4,3,None,1,5]
# Output: 4
root = [-1,5,-2,4,4,2,-2,None,None,-4,None,-2,3,None,-2,0,None,-1,None,-3,None,-4,-3,3,None,None,None,None,None,None,None,3,-3]
# Output: 5
root = list_to_treenode(root)
sol = Solution()
result = sol.goodNodes(root)
print(result)
