# https://leetcode.com/problems/subtree-of-another-tree/
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            if p.val != q.val:
                return False
            else:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        elif not p and not q:
            return True
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = []
        stack.append(root)
        seen = set()
        seen.add(root)

        while len(stack) > 0:
            node = stack.pop(-1)
            if self.isSameTree(node, subRoot):
                return True
                
            if node.left and node.left not in seen:
                    stack.append(node.left)
                    seen.add(node.left)
                    
            if node.right and node.right not in seen:
                stack.append(node.right)
                seen.add(node.right)
            
        return False



def list_to_treenode(elements):
    root_node = TreeNode(val=elements[0])
    nodes = [root_node]
    for i, x in enumerate(elements[1:]):
        if x is None:
            continue
        parent_node = nodes[i // 2]
        is_left = i % 2 == 0
        node = TreeNode(val=x)
        if is_left:
            parent_node.left = node
        else:
            parent_node.right = node
        nodes.append(node)

    return root_node
     

root = [3,4,5,1,2]
subRoot = [4,1,2]
# root = [4,5]
# subRoot = [4,None,5]
root = list_to_treenode(root)
subRoot = list_to_treenode(subRoot)
sol = Solution()
result = sol.isSubtree(root, subRoot)
print(result)

