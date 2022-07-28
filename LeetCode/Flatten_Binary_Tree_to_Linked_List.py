# https://leetcode.com/problems/filling-bookcase-shelves/
def from_list(elements):
    root_node = TreeNode(val=elements[0])
    nodes = [root_node]
    for i, x in enumerate(elements[1:]):
        if x is None:
            continue
        parent_node = nodes[i // 2]
        is_left = (i % 2 == 0)
        node = TreeNode(val=x)
        if is_left:
            parent_node.left = node
        else:
            parent_node.right = node
        nodes.append(node)

    return root_node

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root):
        self.stack.append(root.val)
        if root.left is not None:
            self.dfs(root.left)

        if root.right is not None:
            self.dfs(root.right)
        
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is not None:
            self.stack = []
            self.dfs(root)
            head = root
            for i in self.stack[1:]:
                head.left = None
                node = TreeNode(val=i)
                head.right = node
                head = node


node_list = [1,2,5,3,4,None,6]
root = from_list(node_list)

sol = Solution()
print(sol.flatten(root))
