# https://leetcode.com/problems/same-tree/
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
     

# p = [1,2,3]
# q = [1,2,3]
# p = [1,2]
# q = [1,None,2]
# p = [1,2,1]
# q = [1,1,2]
p = [1]
q = [1,None,2]
p = list_to_treenode(p)
q = list_to_treenode(q)
sol = Solution()
result = sol.isSameTree(p, q)
print(result)

