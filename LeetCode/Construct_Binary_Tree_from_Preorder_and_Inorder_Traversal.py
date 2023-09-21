# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            INDEX = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[INDEX])
            root.left = self.buildTree(preorder, inorder[:INDEX])
            root.right = self.buildTree(preorder, inorder[INDEX+1:])
			
            return root
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            inorder_index = inorder.index(preorder.pop(0))
            head = TreeNode(inorder[inorder_index])
            head.left = self.buildTree(preorder, inorder[:inorder_index])
            head.right = self.buildTree(preorder, inorder[inorder_index+1:])
            return head
            

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# preorder = list_to_treenode(preorder)
# inorder = list_to_treenode(inorder)
sol = Solution()
result = sol.buildTree(preorder, inorder)
print(result)
