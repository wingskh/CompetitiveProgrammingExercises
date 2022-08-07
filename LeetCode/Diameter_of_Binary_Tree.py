# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        def dfs(node):
            if node is None:
                return 0

            left_child = dfs(node.left)
            right_child = dfs(node.right)
            self.diameter = max(self.diameter, left_child + right_child)
            return max(left_child, right_child) + 1
        dfs(root)
        return self.diameter


def list_to_treenode(elements):
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


node_list = [1,None,2]
node_list = [4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2]
root = list_to_treenode(node_list)

sol = Solution()
print(sol.diameterOfBinaryTree(root))
# 