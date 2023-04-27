# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        def dfs(node):
            if node.left is not None:
                dfs(node.left)
            nonlocal result
            result.append(node.val)
            if node.right is not None:
                dfs(node.right)

        dfs(root)
        return result[k-1]


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
     

root = [5,3,6,2,4,None,None,1]
k = 3
root = list_to_treenode(root)
sol = Solution()
result = sol.kthSmallest(root, k)
print(result)
